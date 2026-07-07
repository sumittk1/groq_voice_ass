# 🤖 Jarvis: Real-Time Voice-to-Voice AI Assistant

An ultra-fast, continuous voice-to-voice AI assistant inspired by Iron Man's Jarvis. Built using the **Groq API** for sub-second latency, this project features a continuous listening loop, auto-silence detection, and a reactive 3D hologram web interface.

## ✨ Features

*   **⚡ Ultra-Fast Inference:** Powered by Groq's LPU infrastructure for zero-lag conversational AI.
*   **🎙️ Continuous Duplex Audio:** Click "Initiate Call" once. The system automatically detects when you stop speaking, processes the audio, replies, and immediately goes back to listening.
*   **🌐 3D Hologram UI:** A custom HTML5 Canvas interface that renders a 3D network sphere. The sphere reacts and pulses to the volume/frequencies of the AI's voice in real-time.
*   **📜 Live Chat Transcript:** A transparent side-panel that displays the real-time transcription of both the user and the AI.
*   **🗣️ Multilingual Understanding, English Output:** Instructed via system prompt to understand Hindi, English, and Hinglish, but strictly reply in professional English.

## 🛠️ Tech Stack

*   **Backend:** Python, Flask
*   **Frontend:** HTML5, CSS3, Vanilla JavaScript, Web Audio API (for Silence Detection & Audio Visualization)
*   **Speech-to-Text:** Whisper Large V3 (via Groq)
*   **LLM / Brain:** Meta Llama 3.1 8B Instant (via Groq)
*   **Text-to-Speech:** Canopy Labs Orpheus `orpheus-v1-english` (via Groq)

## 🚀 Prerequisites

1.  Python 3.8+ installed on your system.
2.  A [Groq Developer Account](https://console.groq.com/).
3.  **Crucial Step:** You must manually accept the terms for the Text-to-Speech model. Go to the [Groq Playground](https://console.groq.com/playground), select `canopylabs/orpheus-v1-english` from the model dropdown, and click **Accept Terms**.

## ⚙️ Installation & Setup

**1. Clone the repository or create the project folder:**
```bash
mkdir jarvis-assistant
cd jarvis-assistant
