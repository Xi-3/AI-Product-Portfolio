🌐 **Language**: [🇨🇳 简体中文](README.md) | [🇺🇸 English](README_EN.md)

# Liu Xiqian | AI Product Manager & Growth Hacker 🚀

> AI Product Manager and Growth Hacker with a deep understanding of underlying algorithm logic. Backed by a solid foundation in Data Science, I am highly proficient in utilizing AI-native programming tools like **Claude Code** and **OpenClaw**. Dedicated to building and operating commercially viable AI product ecosystems and driving data-driven growth.

### 🛠️ Core Tech Stack
<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/Vue.js-4FC08D?style=flat-square&logo=vue.js&logoColor=white" />
  <img src="https://img.shields.io/badge/YOLOv8-00FFFF?style=flat-square&logo=yolo&logoColor=black" />
  <img src="https://img.shields.io/badge/LLM_API-OpenAI_Compatible-412991?style=flat-square" />
  <img src="https://img.shields.io/badge/RAG-TF--IDF_&_Cosine_Similarity-FF9900?style=flat-square" />
  <img src="https://img.shields.io/badge/Growth-A/B_Testing-E34F26?style=flat-square" />
</p>

---

## 🤖 Core Projects: AI Commercialization & R&D

### 1️⃣ PepperGuard AI: Intelligent Agricultural Diagnosis System
**Tags**: `LLM API` `RAG` `FastAPI` `OpenClaw`

**🎯 Business Pain Point**: Underserved agricultural markets lack professional diagnostic channels. Directly applying traditional LLMs often results in severe medical and agricultural hallucinations.
**💡 Product Solution**: Independently designed and deployed a specialized multi-modal knowledge base, closing the loop from a raw AI tool to a consumer-facing diagnostic product.

<table>
  <tr>
    <td width="50%"><img src="https://github.com/Xi-3/AI-Product-Portfolio/blob/main/images/86bb1ccd99fe6031a5bc3edba9519164.png?raw=true" alt="UI 1"></td>
    <td width="50%"><img src="https://github.com/Xi-3/AI-Product-Portfolio/blob/main/images/c553d36af14670803abab31e0555a352.png?raw=true" alt="UI 2"></td>
  </tr>
  <tr>
    <td><img src="https://github.com/Xi-3/AI-Product-Portfolio/blob/main/images/33328754242c3da24dff980a0b4c5fc6.png?raw=true" alt="UI 3"></td>
    <td><img src="https://github.com/Xi-3/AI-Product-Portfolio/blob/main/images/0176029f708d7b72e0e75b1b4f59e509.png?raw=true" alt="UI 4"></td>
  </tr>
</table>

**⚙️ Underlying Logic & Tech:**
* **Lightweight RAG & Hallucination Mitigation**: Engineered a retrieval pipeline utilizing **TF-IDF and cosine similarity** rather than standard dense embeddings. This allows for highly precise matching of symptoms and treatments against the local knowledge base, significantly minimizing LLM hallucinations.
* **Context Injection Mechanism**: Dynamically injected user image features and retrieved structural data as Context into the System Prompt. This guarantees accurate, empathetic, and traceable diagnostic outputs via OpenAI-compatible models.

👉 **[Click to view: PepperGuard AI PRD & System Architecture ↗](./docs/SPEC.md)**

---

### 2️⃣ Pest CV Monitoring & Visual Awareness Dashboard
**Tags**: `YOLOv8` `WebSocket` `Vue3` `Data Visualization`

**🎯 Business Pain Point**: Traditional agricultural monitoring provides real-time video feeds but zero structured data, making 24/7 automated intervention impossible.
**💡 Product Solution**: Spearheaded the end-to-end deployment of edge visual inference models and connected them to a front-end dashboard, establishing a complete "Detection-Warning-Push" IoT data pipeline.

<p align="center">
  <img src="https://github.com/Xi-3/AI-Product-Portfolio/blob/main/images/80381f948708352eae48f7567073b672.png?raw=true" width="49%">
  <img src="https://github.com/Xi-3/AI-Product-Portfolio/blob/main/images/cv.png?raw=true" width="49%">
</p>

**⚙️ Commercial Monitoring Logic:**
* **Dual-Channel Low Latency Streaming**: Separated the transmission architecture—routing video frame streams via MJPEG and structured AI detection results via WebSocket—ensuring millisecond-level responsiveness on the Vue3 dashboard even under poor network conditions.
* **Data-Driven Alert Tiers**: Configured dynamic Normal/Warning/Danger thresholds based on the real-time pest count detected by YOLOv8, supplemented by environmental sensor data to trigger multi-dimensional interventions.

---

## 📈 Growth Hacking: AI-Empowered Social Media Matrix

### 📱 0-to-1 Account Incubation & Monetization Strategy
**Operational Period**: 2025.02 - 2025.05 | **Independently Managed**

**🎯 Objective**: To crack the cold-start algorithm and drive massive organic traffic with zero ad budget by utilizing data-driven insights and AI workflows.

<p align="center">
  <img src="https://github.com/Xi-3/AI-Product-Portfolio/blob/main/images/e87565fba9cccc9bc9acca96f579c597.jpg?raw=true" width="400">
</p>
*（Zero-budget viral video achieving 29K+ views through dynamic A/B testing on the first 3-second hook）*

**💡 Growth Strategy & AI Efficiency:**
* **AI-Reconstructed Workflows**: Proficiently leveraged LLMs and AI tools to deconstruct competitor data, batch-generate viral video scripts (incorporating localized slang and emotional hooks), and automate distribution, drastically shortening the idea-to-monetization cycle.
* **Algorithm Hacking & A/B Testing**: Deeply analyzed recommendation algorithms to conduct robust A/B testing, dynamically optimizing the first 3 seconds (Hook) and Call-to-Action (CTA) structures.
* **Core Milestones**: Generated over **150,000+** total organic impressions, with a single viral video peaking at **29,000+** views, accumulating **200+** deep, high-value user interactions (likes/comments).

👉 **[Click to view: Overseas & Domestic AIGC Viral Short-Video Prompt Framework ↗](./prompts/Douyin_Viral_Script_Generator.md)**
