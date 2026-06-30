from app.core.database import redis_db
from datetime import datetime
from app.enums.call_status import CallStatus


class RedisRepository:

    def save_call(self, call):

        redis_db.hset(
            f"call:{call.call_id}",
            mapping={
                "agent": call.agent,
                "customer": call.customer,
                "status": CallStatus.RINGING.value,
		"started_at": datetime.now().isoformat()
            }
        )

    def get_call(self, call_id: str):

        return redis_db.hgetall(f"call:{call_id}")

    def delete_call(self, call_id: str):

        redis_db.delete(f"call:{call_id}")


    def update_status(self, call_id: str, status: str):

        key = f"call:{call_id}"

        if not redis_db.exists(key):
            return False

        redis_db.hset(key, "status", status)

        return True
