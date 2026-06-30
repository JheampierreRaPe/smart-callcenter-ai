from fastapi import APIRouter

from app.core.database import mongo
from app.core.database import redis_db

from app.schemas.call import CallCreate
from app.services.call_service import CallService

router = APIRouter()

service = CallService()

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
        mongo.admin.command("ping")
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
