# AI-Powered-Voice-Bot-Customer-Support-Automation
Production-ready Voice Bot system that handles customer support queries using Speech Recognition, NLP-based Intent Classification, and Text-to-Speech synthesis.

---

## 📌 Project Objective

To build an end-to-end ML pipeline that:

- Accepts user voice input (WAV)
- Converts speech to text (ASR)
- Classifies user intent
- Generates contextual responses
- Converts response text to speech
- Returns audio output via REST API

This project demonstrates real-world ML system design, modular architecture, and production deployment practices.

---

## 🏗 System Architecture

User Audio (WAV)  
↓  
Whisper ASR  
↓  
BERT Intent Classifier  
↓  
Structured Response Layer  
↓  
Coqui TTS  
↓  
Audio Output (WAV)

---

## 🛠 Tech Stack

- Python
- FastAPI
- PyTorch
- Hugging Face Transformers (BERT)
- Whisper (ASR)
- Coqui TTS
- Scikit-learn
- JiWER (WER metric)
- Docker

---

## 🎯 Key Features

- ✅ Whisper-based speech recognition
- ✅ Fine-tuned BERT intent classifier (10 intents)
- ✅ Confidence score output
- ✅ Hallucination-safe structured responses
- ✅ Natural speech synthesis
- ✅ REST API deployment (FastAPI)
- ✅ Evaluation metrics (WER, Accuracy, F1-score)
- ✅ Modular production architecture

---

## 📂 Project Structure

ai-voicebot-customer-support/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── services/
│   ├── utils/
│   └── models/
│
├── training/
│   ├── train_intent_model.py
│   └── dataset.csv
│
├── results/
├── demo/
├── requirements.txt
├── Dockerfile
└── README.md

---

## 🧠 Supported Intents

1. order_status  
2. cancel_order  
3. refund_request  
4. subscription_issue  
5. payment_issue  
6. delivery_delay  
7. account_update  
8. technical_support  
9. complaint  
10. greeting  

---

## 📊 Model Evaluation

### ASR
- Word Error Rate (WER): ~8–12%

### Intent Classification
- Accuracy: ~90%
- Precision / Recall balanced
- F1-score: ~0.9
- Confusion matrix available in `/results`

---

## 🚀 API Endpoints

| Endpoint | Description |
|-----------|------------|
| `/voicebot` | Full Audio → Audio Pipeline |
| `/transcribe` | Audio → Text |
| `/predict-intent` | Text → Intent |
| `/generate-response` | Intent → Text |
| `/synthesize` | Text → Audio |

---

## ▶️ Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/ai-voicebot-customer-support.git
cd ai-voicebot-customer-support
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Start Server

```bash
uvicorn app.main:app --reload
```

### 4️⃣ Open API Docs

http://127.0.0.1:8000/docs

---

## 🐳 Docker Deployment

Build image:

```bash
docker build -t ai-voicebot .
```

Run container:

```bash
docker run -p 8000:8000 ai-voicebot
```

---

## ⚡ Performance

- End-to-end latency: 3–5 seconds (local inference)
- Optimized model loading
- Modular service-based design
- Clean memory management

---

## 🔐 Production Design Principles

- Separation of ASR, NLP, TTS layers
- Config-driven model loading
- Confidence threshold filtering
- Logging & exception handling
- No scattered hardcoded responses

---

## 📈 Future Improvements

- Real-time streaming ASR
- Multi-language support
- Context-aware multi-turn conversations
- Cloud deployment (AWS/GCP)
- GPU optimization

---

## 👨‍💻 Author

Lakshay Tomar  
Aspiring ML Engineer | Data Analyst  

---

⭐ If you found this useful, consider starring the repository.
