from pydantic import BaseModel

from app.enums.call_status import CallStatus


class StatusUpdate(BaseModel):

    status: CallStatus
