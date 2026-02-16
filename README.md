# 🎙️ AI Voice Assistant
### Powered by OpenAI GPT-5 Nano & IBM Watson

A professional-grade, containerized voice assistant that bridges **OpenAI's GPT-5 Nano** reasoning with **IBM Watson's** enterprise-grade Speech-to-Text (STT) and Text-to-Speech (TTS) engines. 

---

## 🌟 Features

*   **Real-time Transcription**: Converts voice to text using IBM Watson's `en-US_Multimedia` model.
*   **Neural Reasoning**: Leverages the latest **GPT-5 Nano** for high-efficiency, context-aware responses.
*   **High-Fidelity Audio**: Synthesizes natural-sounding voice responses with custom voice selection.
*   **Production Ready**: Fully dockerized with secure `.env` credential management.

---

## 🛠️ Architecture & Tech Stack

| Component | Technology |
| :--- | :--- |
| **Orchestration** | Python 3.10 / Flask |
| **LLM Engine** | OpenAI GPT-5 Nano |
| **Voice Processing** | IBM Watson STT & TTS |
| **Environment** | Docker Desktop & WSL2 |
| **Authentication** | Basic Auth (API Key) & `.env` |

---

## 🚀 Quick Start

### 1. Prerequisites
- [Docker Desktop](https://www.docker.com) installed and running.
- OpenAI API Key.
- IBM Cloud Account (Speech-to-Text & Text-to-Speech instances).

### 2. Configuration
Create a `.env` file in the project root to securely store your secrets:

```env
OPENAI_API_KEY=your_openai_key
WATSON_STT_API_KEY=your_ibm_stt_key
WATSON_STT_URL=your_ibm_stt_url
WATSON_TTS_API_KEY=your_ibm_tts_key
WATSON_TTS_URL=your_ibm_tts_url
```

### 3. Build & Deploy
Build the Docker image locally:

```bash
docker build . -t voice-assistant-ai
```

Launch the container with your environment variables:

```bash
docker run -p 8000:8000 --env-file .env voice-assistant-ai
```

Access the interface at: http://localhost:8000

### 🛡️ Security & Best Practices
Credential Protection: The .env file is excluded from version control via .gitignore to prevent secret leakage.

Stateless Container: The Docker image remains "clean"—it does not store sensitive keys, requiring them to be injected at runtime.

API Error Handling: Functions include checks for missing environment variables to prevent runtime crashes.

### ⚖️ License
This project is licensed under the Apache License 2.0. See the LICENSE file for the full text.

Developed as part of the IBM AI Developer Professional Certificate.
