from fastapi import APIRouter

from app.core.database import mongo_client
from app.core.database import redis_db

from app.schemas.call import CallCreate
from app.schemas.status import StatusUpdate
from app.services.call_service import CallService


from app.clients.transcription_client import TranscriptionClient





client = TranscriptionClient()

router = APIRouter()

service = CallService()





@router.get("/test-ai")
def test_ai():

    return client.transcribe()


@router.get("/")
def home():

    return {
        "mensaje": "Gateway funcionando"
    }


@router.get("/ping")
def ping():

    mongo_ok = False
    redis_ok = False

    try:
        mongo_client.admin.command("ping")
        mongo_ok = True
    except:
        pass

    try:
        redis_db.ping()
        redis_ok = True
    except:
        pass

    return {
        "mongodb": mongo_ok,
        "redis": redis_ok
    }

@router.post("/calls")
def create_call(call: CallCreate):

    service.create_call(call)

    return {
        "message": "Call created successfully"
    }


@router.get("/calls/{call_id}")
def get_call(call_id: str):

    call = service.get_call(call_id)

    if not call:
        return {
            "error": "Call not found"
        }

    return {
        "call_id": call_id,
        **call
    }


@router.post("/calls/{call_id}/status")
def update_call_status(call_id: str, data: StatusUpdate):

    updated = service.update_status(call_id, data.status)

    if not updated:
        return {
            "error": "Call not found"
        }

    return {
        "message": "Status updated"
    }


@router.post("/calls/{call_id}/finish")
def finish_call(call_id: str):

    call = service.finish_call(call_id)

    if not call:

        return {
            "error":"Call not found"
        }

    return {
        "message":"Call finished",
        "call":call
    }
