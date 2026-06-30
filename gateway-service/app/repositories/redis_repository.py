from app.core.database import redis_db


class RedisRepository:

    def save_call(self, call):

        redis_db.hset(
            f"call:{call.call_id}",
            mapping={
                "agent": call.agent,
                "customer": call.customer,
                "status": "ringing"
            }
        )
