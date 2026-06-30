from pydantic import BaseModel


class CallCreate(BaseModel):

    call_id: str

    agent: str

    customer: str
