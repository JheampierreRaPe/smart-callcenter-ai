from pydantic import BaseModel
from app.enums.call_status import CallStatus

class CallCreate(BaseModel):

    call_id: str

    agent: str

    customer: str

    status: CallStatus = CallStatus.RINGING
