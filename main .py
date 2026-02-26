# app/main.py

from fastapi import FastAPI, UploadFile, File
import shutil

from app.services.asr_service import ASRService
from app.services.intent_service import IntentService
from app.services.response_service import generate_response
from app.services.tts_service import TTSService

app = FastAPI()

asr = ASRService()
intent_model = IntentService("app/models/intent_model")
tts = TTSService()

@app.post("/voicebot")
async def voicebot(audio: UploadFile = File(...)):

    file_path = "temp.wav"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    text = asr.transcribe(file_path)
    intent_id, confidence = intent_model.predict(text)
    response_text = generate_response(intent_id)
    audio_output = tts.synthesize(response_text)

    return {
        "transcription": text,
        "intent_id": intent_id,
        "confidence": confidence,
        "response": response_text,
        "audio_file": audio_output
    }
