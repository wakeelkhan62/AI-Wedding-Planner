# 💍 AI Wedding Planner (Multi-Agent AI System)

An intelligent **AI Wedding Planner** built using **LangChain**, **LangGraph**, **Azure OpenAI**, and **Streamlit**. The system follows a **Multi-Agent Architecture**, where each AI agent is responsible for a specific wedding planning task while a Coordinator Agent manages the overall workflow.

---

# 📌 Project Overview

Planning a wedding involves multiple decisions such as venue selection, budget allocation, catering, decoration, and event scheduling.

Instead of using one large AI model for every task, this project divides responsibilities among specialized AI agents.

The **Coordinator Agent** understands the user's request, decides which specialist agents are required, collects their responses, and generates a complete wedding plan.

The project also supports **conversation memory**, allowing users to modify individual sections of an existing wedding plan without regenerating the entire plan.

---

# 🎯 Objectives

- Demonstrate Multi-Agent AI Architecture
- Showcase LangChain Agent orchestration
- Implement conversation memory using LangGraph
- Build a modular and scalable AI application
- Provide a professional Streamlit interface

---

# 🏗️ System Architecture

```
                     User
                       │
                       ▼
              Coordinator Agent
                       │
 ┌─────────────┬────────────┬─────────────┬──────────────┬─────────────┐
 ▼             ▼            ▼             ▼              ▼
Venue      Budget      Catering     Decoration      Timeline
 Agent       Agent        Agent         Agent          Agent
```

The Coordinator Agent decides which specialist agents are required based on the user's request.

---

# 🤖 AI Agents

## 1. Coordinator Agent

Responsibilities:

- Understand user intent
- Manage conversation flow
- Use conversation memory
- Route requests to specialist agents
- Merge agent responses
- Handle follow-up modifications

---

## 2. Venue Agent

Responsibilities:

- Search wedding venues
- Recommend venues within budget
- Compare venue quality
- Estimate venue pricing

Tools Used:

- Web Search Tool

---

## 3. Budget Agent

Responsibilities:

- Allocate wedding budget
- Calculate category-wise expenses
- Ensure budget consistency

Tools Used:

- Budget Calculation Tool

---

## 4. Catering Agent

Responsibilities:

- Recommend catering companies
- Suggest food menus
- Estimate catering cost

Tools Used:

- Web Search Tool
- Food Cost Estimator

---

## 5. Decoration Agent

Responsibilities:

- Recommend wedding themes
- Suggest floral arrangements
- Stage decoration
- Color palette
- Decoration estimation

Tools Used:

- Web Search Tool

---

## 6. Timeline Agent

Responsibilities:

- Generate a professional wedding schedule
- Organize wedding events chronologically

---

# 🧠 Memory

The project uses **LangGraph Checkpointer Memory**.

Memory enables the system to:

- Remember previous conversation
- Avoid asking duplicate questions
- Support follow-up modifications
- Improve user experience

Example:

User:

> Plan my wedding.

Later:

> Recommend a better venue.

Only the **Venue Agent** is executed.

---

# ✨ Features

- Multi-Agent Architecture
- Coordinator-based Routing
- Conversation Memory
- Follow-up Modification Support
- Professional Streamlit UI
- Web Search Integration
- Budget Calculation
- Structured AI Responses
- Modular Agent Design

---

# 🛠️ Technologies Used

- Python
- LangChain
- LangGraph
- Azure OpenAI
- Streamlit
- Pydantic
- Async Programming

---

# 📁 Project Structure

```
Wedding-Planner-AI/

│

├── agents/
│   ├── coordinator.py
│   ├── venue_agent.py
│   ├── budget_agent.py
│   ├── catering_agent.py
│   ├── decoration_agent.py
│   └── timeline_agent.py
│
├── tools/
│
├── schemas/
│
├── config/
│
├── utils/
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/wakeelkhan62/AI-Wedding-Planner.git
```

Move into the project:

```bash
cd AI-Wedding-Planner
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate virtual environment:

Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run app.py
```

---

# 📸 Screenshots

Add screenshots inside the `assets/` folder.

Example:

```
assets/
│
├── home.png
├── planning.png
└── followup.png
```

---

# 🔮 Future Improvements

- Photography Agent
- Invitation Card Agent
- Makeup Artist Agent
- Entertainment Agent
- Honeymoon Planner
- Real-time Booking APIs
- Payment Integration
- Voice Assistant
- MCP Integration

---

# 👨‍💻 Developer

**Wakeel Ahmad**

BS Computer Science


---

# ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.
