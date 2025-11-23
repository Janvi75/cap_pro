Agent Sentinel: Automated Threat Assessment System

Project Overview

Agent Sentinel is a modular, multi-agent system designed for the rapid automation of cybersecurity incident response. It takes a raw security alert ID, synthesizes data from mock security feeds, performs a risk assessment, and generates ready-to-distribute technical and executive reports.

This project is structured as a clear adaptation of the multi-agent system pattern demonstrated in the Google Agent Development Kit (ADK) samples.

Source Reference: The core multi-agent architecture, the use of specialized sub-agents, and the iterative workflow pattern (using MockLoopAgent and validation checkers) are modeled after the cloude-google/agent-shutton repository.

The specific implementation and logic within each agent are original to this project and adapted for the cybersecurity domain.

Architecture

The system is managed by the Interactive Sentinel Orchestrator agent, which delegates tasks sequentially to four specialized sub-agents.

Workflow

Threat Identification: Gather IoCs and known threat actor data. (Uses ThreatIdentifierAgent)

Context Synthesis: Fetch mock logs and reconstruct the attack timeline. (Uses LogContextAgent)

Risk Assessment (Validated Loop): Assign a Severity Score and generate Mitigation Steps. This phase uses a MockLoopAgent to ensure the output format is correct before proceeding. (Uses RiskAssessmentAgent and SeverityScoreValidationChecker)

Report Writing: Generate the final Technical Report and Executive Summary. (Uses ReportWriterAgent)

Export: Save the final reports using a custom tool.

Setup and Running

Ensure you have a Python environment set up.

Place all the generated files in a sentinel_agent directory (preserving the sub_agents subfolder).

Run the main orchestrator script:

python agent.py
