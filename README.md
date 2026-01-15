# 🛡️ Local-First Multi-Agent Safety Auditor

An implementation of **Asynchronous AI Oversight** using local Small Language Models (SLMs). This project demonstrates how to build a self-correcting agentic loop that prioritizes **AI Safety** and **Privacy** by running entirely on local hardware.

---

## 🚀 The Challenge: The "Agency Gap"
In 2026, the biggest hurdle for AI labs is ensuring autonomous agents don't hallucinate or make unsafe decisions. Most systems rely on a single model. This project solves that by implementing a **"Model-as-a-Judge" (MaaJ)** architecture.

## 🧠 Technical Architecture
The system utilizes a **Tiered Intelligence Strategy**:

1.  **The Generator (Worker):** Powered by `Microsoft Phi-3 Mini`. It handles the primary reasoning and content generation.
2.  **The Auditor (Supervisor):** Powered by `TinyDolphin`. A lightweight, high-speed model that audits the Generator's output in real-time.

### Key Features:
* **Zero-Cost Inference:** Utilizes [Ollama](https://ollama.com) to run models locally (No API tokens required).
* **Agentic Verification:** The Auditor checks for technical accuracy and safety before the user sees the final output.
* **Hardware Optimization:** Optimized for consumer-grade hardware by using Quantized SLMs to prevent VRAM bottlenecks.
* **Streaming UI:** Implements word-by-word streaming to reduce perceived latency.

---

<img width="1438" height="565" alt="Screenshot 2026-01-15 231618" src="https://github.com/user-attachments/assets/b31d27d5-cec8-4575-8e54-52edb8f8f309" />


## 🛠️ Installation & Setup

1. **Prerequisites:** - Install [Ollama](https://ollama.com)
   - Pull the models: `ollama pull phi3:mini` and `ollama pull tinydolphin`

2. **Environment Setup:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   pip install -U langchain-ollama
