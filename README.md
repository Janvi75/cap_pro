
# **EcoGuardian — Multi-Agent Waste Detection & Recycling Optimization**

### *AI-powered visual detection + multi-agent routing system to improve recycling efficiency and reduce waste management costs*

<img src="assets/thumbnail.png" width="760"/>

---

## **📍 Submission Track**

**Concierge / Autonomous Agents**

---

## **🚩 Problem Overview**

Cities worldwide struggle with inefficient waste collection logistics and poor recycling participation. Waste is often collected on fixed schedules rather than based on real demand, leading to:

* unnecessary fuel and labor costs,
* overflowing public bins,
* low recycling capture rates,
* environmental pollution & greenhouse gas emissions.

Manual monitoring and planning are time-consuming, costly, and reactive instead of proactive.

---

## **💡 Solution Summary**

**EcoGuardian** is a **multi-agent system** that automatically:

1. Detects and classifies waste items using computer vision,
2. Computes optimal recycling pickup routes based on detections and location clustering,
3. Generates public-friendly recycling recommendations using a Gemini-powered LLM,
4. Maintains memory of historical pickup patterns to improve future route plans.

The system demonstrates real AI-agent reasoning through orchestration, tool use, optimized workflows, and evaluation metrics.

---

## **🎯 Value Proposition**

| Stakeholder           | Benefit                                            |
| --------------------- | -------------------------------------------------- |
| City waste management | Reduced fuel/time costs through optimized routing  |
| Environmental impact  | Less landfill volume & CO₂ emissions               |
| Community             | Cleaner streets, better recycling participation    |
| Operations teams      | Automated monitoring instead of manual inspections |

**Results shown in demo**:

* Improved route efficiency: *reduction in route length vs baseline static route (measured in meters/time)*
* Improved sorting accuracy: *Precision / Recall / F1 for waste detection & category classification*

---

## **🏗 System Architecture**

```
┌─────────────────────────────────────────────────────────┐
│                     Coordinator Agent                    │
│                      (A2A Orchestrator)                 │
└───────────────┬─────────────────────────────┬───────────┘
                │                             │
                ▼                             ▼
     ┌──────────────────┐          ┌─────────────────────┐
     │ Detection Agent  │   --->   │ Classification Agent │
     │ (Parallel CV)    │          │ (Refinement Loop)   │
     └──────────────────┘          └─────────────────────┘
                │                             │
                └──────────────┬──────────────┘
                               ▼
                     ┌─────────────────────┐
                     │ Routing Agent       │
                     │ (Optimization tool) │
                     └─────────────────────┘
                               │
                               ▼
                     ┌─────────────────────┐
                     │ Recommender Agent   │
                     │ (Gemini LLM)        │
                     └─────────────────────┘
```

---

## **🧠 Agent Concepts Demonstrated (Required ≥3 — we include 5+)**

| Concept                                             | Usage in project                                                                                  |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Multi-Agent System** (parallel, sequential, loop) | Detection Agents run parallel inference; classification sequential refinement loop; routing agent |
| **Tools (custom + built-in)**                       | `image_infer_tool`, `route_optimizer_tool`, Code execution tool                                   |
| **Sessions & Memory**                               | InMemorySessionService + Memory Bank to store pickup history                                      |
| **Long-running operations**                         | Routing scheduler can pause/resume processing                                                     |
| **Observability & Evaluation**                      | Logging, inference timing, precision/recall, route-efficiency metrics                             |

**Bonus:**

* Gemini model for recommendation generation
* Optional deployment via Agent Engine / Cloud Run
* Short 3-minute demo video (linked below)

---

## **📊 Evaluation & Metrics**

| Metric                             | Description                                       |
| ---------------------------------- | ------------------------------------------------- |
| Precision / Recall / F1            | Accuracy of detection and category classification |
| mAP                                | Object recognition performance                    |
| Route efficiency (Δdistance saved) | Optimized route vs baseline static route          |
| System latency                     | Image-to-decision total time                      |

Example Dashboard Output:

* Annotated detection results
* Routing path visualization
* Charts showing time/distance reduction

---

## **📦 Project Structure**

```
EcoGuardian/
│
├── notebooks/
│   └── EcoGuardian_demo.ipynb
│
├── src/
│   ├── agents/
│   │   ├── detection_agent.py
│   │   ├── routing_agent.py
│   │   ├── recommender_agent.py
│   │   └── coordinator.py
│   └── tools/
│       ├── image_infer_tool.py
│       └── route_optimizer_tool.py
│
├── data/              # Sample dataset images
├── tests/             # evaluation scripts
├── assets/            # thumbnail, diagrams
└── README.md
```

---

## **🧪 How to Run**

### **Option A: Kaggle Notebook**

Open and execute `EcoGuardian_demo.ipynb`
*All dependencies auto-installed.*

### **Option B: Local Setup**

```bash
git clone <repo-url>
cd EcoGuardian
pip install -r requirements.txt
python src/run_demo.py
```

### **Dataset**

Uses public waste detection dataset(s) with proper licensing; referenced in notebook.

---

## **🎥 Demo Video**

👉 *3-minute walkthrough with architecture, demo, and results*
[YouTube Demo Link]()

---

## **🚀 Deployment (Optional / Bonus)**

The project includes instructions to deploy inference and routing orchestration using:

* **Agent Engine**
* **Cloud Run**
  (Documentation in `/deployment` folder)

---

## **🔮 Future Enhancements**

* Real-time camera integration
* GPS-driven pickup maps
* Predictive modeling based on seasonal patterns
* Integration with municipal dashboards

---

## **🙌 Acknowledgements**

* Kaggle AI Agentic Course team
* Model/dataset authors
* Open-source contributors

---

## **📄 License**

MIT License (except datasets which follow their own licensing terms)

