from app.repositories.redis_repository import RedisRepository


class CallService:

    def __init__(self):

        self.redis = RedisRepository()


    def create_call(self, call):

        self.redis.save_call(call)
