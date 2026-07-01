from fastapi import APIRouter
from app.schemas.transcription import TranscriptionRequest

router = APIRouter()


@router.get("/")
def home():

    return {
        "service": "Transcription Service"
    }


@router.post("/transcribe")
def transcribe(request: TranscriptionRequest):

    return {
       "audio_file": request.audio_file,
       "transcription": "Hola, gracias por llamar. ¿En qué puedo ayudarle?"
    }
