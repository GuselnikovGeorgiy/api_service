from dataclasses import dataclass
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection

from app.storage.models import UserDataGet, UserDataInsert
from app.storage.utils import split_query, calculate_connection_duration, validate_json_data


@dataclass
class MongoDBClient:
    mongo_db_client: AsyncIOMotorClient
    mongo_db_name: str
    mongo_collection_name: str

    def _get_collection(self) -> AsyncIOMotorCollection:
        return self.mongo_db_client[self.mongo_db_name][self.mongo_collection_name]

    async def find_user_data(self, filter_params: dict) -> list[UserDataGet]:
        limit = filter_params.get("limit")
        filter_query = split_query(filter_params)
        cursor = self._get_collection().find(filter_query)
        if limit is not None:
            cursor = cursor.limit(limit)
        result = await cursor.to_list(length=None)
        for document in result:
            if "_id" in document:
                document["_id"] = str(document["_id"])
        return result

    async def insert_user_data(self, user_data: UserDataInsert) -> dict:
        document = user_data.dict()
        document['ip_address'] = str(document['ip_address'])
        document = calculate_connection_duration(document)
        result = await self._get_collection().insert_one(document)
        return {"id": str(result.inserted_id)}

    async def insert_list_of_user_data(self, user_data: list[UserDataInsert]) -> list[dict]:
        documents = []
        for document in user_data:
            document = document.dict()
            document['ip_address'] = str(document['ip_address'])
            documents.append(calculate_connection_duration(document))

        result = await self._get_collection().insert_many(documents)
        return [{"id": str(document_id)} for document_id in result.inserted_ids]

    async def insert_from_json_file(self, user_data: list[dict]) -> list[dict]:
        validated_data = validate_json_data(user_data)
        documents = [calculate_connection_duration(user_data) for user_data in validated_data]
        for document in documents:
            document['ip_address'] = str(document['ip_address'])
        result = await self._get_collection().insert_many(documents)
        return [{"id": str(document_id)} for document_id in result.inserted_ids]


db_client = MongoDBClient(
    mongo_db_client=AsyncIOMotorClient("mongodb://mongodb:27017", serverSelectionTimeoutMS=3000),
    mongo_db_name="user_data_storage",
    mongo_collection_name="user_data",
)
