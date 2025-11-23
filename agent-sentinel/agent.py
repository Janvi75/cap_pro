import json
from adk_mocks import MockAgent, MockLoopAgent
from config import AGENT_CONFIG
from tools import SENTINEL_TOOLS, FETCH_LOGS_TOOL # Import the list of tools and one specific tool for context
from sub_agents.validation_checkers import ReportDataValidationChecker
from sub_agents.threat_identifier import ThreatIdentifierAgent
from sub_agents.log_context import LogContextAgent
from sub_agents.risk_assessment import RiskAssessmentAgent
from sub_agents.report_writer import ReportWriterAgent

# --- 6. ORCHESTRATOR AGENT ---

class InteractiveSentinelAgent(MockAgent):
    """The main agent that manages the workflow and delegates tasks."""
    def __init__(self, **kwargs):
        # Tools and Sub-agents are passed to the base class constructor
        super().__init__(
            name="Interactive Sentinel Orchestrator",
            instructions="You are a security orchestration engine that runs the incident response workflow.",
            tools=SENTINEL_TOOLS, # All tools defined in tools.py
            sub_agents=[
                ThreatIdentifierAgent(tools=SENTINEL_TOOLS),
                LogContextAgent(tools=SENTINEL_TOOLS),
                RiskAssessmentAgent(tools=SENTINEL_TOOLS),
                ReportWriterAgent(tools=SENTINEL_TOOLS),
            ],
            **kwargs
        )

    # Main orchestration logic, equivalent to the run_workflow in the original file
    def run_workflow(self, alert_id: str):
        print(f"\n=======================================================")
        print(f"       Agent Sentinel: Incident Response Workflow")
        print(f"  Incident ID: {alert_id} | Initial Time: {AGENT_CONFIG['alert_time']}")
        print(f"=======================================================\n")

        full_context = alert_id
        
        # --- PHASE 1: THREAT IDENTIFICATION (LoopAgent for Validation) ---
        threat_identifier_agent = self.sub_agents[0]
        full_context = MockLoopAgent(threat_identifier_agent.name, threat_identifier_agent.instructions).run(
            full_context, ReportDataValidationChecker(name="Report Data Checker", instructions="Checks if data is complete.")
        )
        if "ERROR" in full_context: return print(full_context)
        print("\n--- PHASE 1 COMPLETE: THREAT IDENTIFIED ---")

        # --- PHASE 2: LOG & CONTEXT SYNTHESIS ---
        full_context = self.sub_agents[1].run(full_context)
        print("\n--- PHASE 2 COMPLETE: CONTEXT ESTABLISHED ---")
        
        # --- PHASE 3: RISK ASSESSMENT (LoopAgent for Validation) ---
        risk_assessment_agent = self.sub_agents[2]
        full_context = risk_assessment_agent.run(
            full_context, risk_assessment_agent.validation_checker
        )
        if "ERROR" in full_context: return print(full_context)
        print("\n--- PHASE 3 COMPLETE: RISK ASSESSED AND MITIGATION READY ---")

        # --- PHASE 4: REPORT GENERATION ---
        report_writer_agent = self.sub_agents[3]
        
        # Manually set context on the final agent before running (a common ADK pattern)
        report_writer_agent.context['alert_id'] = alert_id 
        report_writer_agent.context['threat_intelligence'] = FETCH_LOGS_TOOL(alert_id)['threat_intelligence']
        
        report_json_str = report_writer_agent.run(full_context)
        
        # --- PHASE 5: EXPORT ---
        try:
            reports = json.loads(report_json_str)
            
            # Export the Technical Report (using the tool instance from the Orchestrator's tools list)
            export_tool = self.tools[1]
            report_name = f"incident_report_{alert_id}"
            export_tool(report_name, reports.get("technical_report", "N/A"))

            # Display Executive Summary
            print("\n=======================================================")
            print("         FINAL EXECUTIVE SUMMARY (for Review)")
            print("=======================================================")
            print(reports.get("executive_summary", "Summary not generated."))
            
        except json.JSONDecodeError:
            print(f"ERROR: Final Report Writer did not return valid JSON: {report_json_str}")
        

# --- 7. MAIN EXECUTION ---

if __name__ == "__main__":
    # The hackathon project starts here by initializing and running the Orchestrator
    sentinel_orchestrator = InteractiveSentinelAgent()
    sentinel_orchestrator.run_workflow(alert_id="SEC4567")