from app.core.database import mongo_db


class MongoRepository:

    def save_call(self, call_data: dict):

        mongo_db.calls.insert_one(call_data)
