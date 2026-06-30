from app.repositories.redis_repository import RedisRepository
from app.repositories.mongo_repository import MongoRepository
from datetime import datetime

class CallService:

    def __init__(self):

        self.redis = RedisRepository()
        self.mongo = MongoRepository()


    def create_call(self, call):

        self.redis.save_call(call)

    def get_call(self, call_id: str):

        return self.redis.get_call(call_id)

    def update_status(self, call_id: str, status: str):

        return self.redis.update_status(call_id, status)


    def finish_call(self, call_id: str):

        call = self.redis.get_call(call_id)

        if not call:

            return None
        started_at = datetime.fromisoformat(call["started_at"])

        finished_at = datetime.now()

        duration = int((finished_at - started_at).total_seconds())


        call["_id"] = call_id

        call["status"] = "finished"

        call["finished_at"] = finished_at.isoformat()

        call["duration_seconds"] = duration

        call["audio_file"] = f"recordings/{call_id}.wav"

        self.mongo.save_call(call)

        self.redis.delete_call(call_id)

        return call
