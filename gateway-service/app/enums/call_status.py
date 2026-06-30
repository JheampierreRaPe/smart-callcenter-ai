from enum import Enum


class CallStatus(str, Enum):

    RINGING = "ringing"

    ANSWERED = "answered"

    IN_PROGRESS = "in_progress"

    FINISHED = "finished"
