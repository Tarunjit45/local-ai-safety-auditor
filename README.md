# 🛡️ Local AI Safety Auditor — Asynchronous Dual-SLM Oversight Loop

[![Python](https://img.shields.io/badge/Language-Python%203.12-blue?style=flat-square&logo=python)](https://python.org)
[![LangChain](https://img.shields.io/badge/Orchestration-LangChain%20Ollama-1C3C3C?style=flat-square&logo=langchain)](https://github.com/langchain-ai/langchain)
[![Ollama](https://img.shields.io/badge/Local%20Inference-Ollama-white?style=flat-square&logo=ollama)](https://ollama.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)

An implementation of **Asynchronous AI Oversight & Safety Verification** running 100% locally on personal hardware using **Small Language Models (SLMs)**. Demonstrates how to build an autonomous self-correcting agent loop that prioritizes user privacy, data security, and zero cloud API dependency.

---

## 🌟 Key Features

* **Dual-SLM Architecture:**
  * 🏃 **Worker Agent (`phi3:mini`):** Streams rapid first-pass answers to user queries with zero latency.
  * 🕵️ **Auditor Agent (`tinydolphin`):** Simultaneously observes the output stream, verifying factual consistency, safety guidelines, and hallucination risks.
* **100% On-Device Privacy:** Requires zero external cloud APIs or subscriptions; all tokens are computed on your local CPU/GPU via Ollama.
* **LangChain Integration:** Leverages `langchain-ollama` streaming primitives for responsive token delivery and oversight.

---

## 📁 Repository Structure

```
local-ai-safety-auditor/
├── auditor.py              # Dual-SLM oversight agent loop & streaming runner
├── requirements.txt        # Dependencies (langchain-ollama, httpx, aiohttp)
├── LICENSE                 # MIT License
└── README.md               # Documentation
```

---

## 🚀 Quick Start

### 1. Prerequisites

* Python 3.10+
* [Ollama](https://ollama.com/) installed and running locally
* Download the SLM weights:
  ```bash
  ollama pull phi3:mini
  ollama pull tinydolphin
  ```

### 2. Installation & Run

```bash
git clone https://github.com/Tarunjit45/local-ai-safety-auditor.git
cd local-ai-safety-auditor

pip install -r requirements.txt
python auditor.py
```

---

## 📄 License
This project is open-source under the [MIT License](LICENSE).
