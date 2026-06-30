from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():

    return {
        "service": "Transcription Service"
    }


@router.post("/transcribe")
def transcribe():

    return {
        "transcription": "Hola, gracias por llamar. ¿En qué puedo ayudarle?"
    }
