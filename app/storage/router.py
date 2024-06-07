from fastapi import APIRouter, status, Depends

from app.storage.database import db_client
from app.storage.models import UserDataInsert, UserDataGet
from app.storage.schemas import UserDataFilter

router = APIRouter()


@router.get(
    "/user_data",
    status_code=status.HTTP_200_OK,
    description="Эндпоинт для получения записей из базы данных по параметрам фильтрации",
)
async def get_filtered_user_data(
        filter_params: UserDataFilter = Depends(),
) -> list[UserDataGet]:
    filter_query = filter_params.dict(exclude_none=True)
    return await db_client.find_user_data(filter_query)


@router.post(
    "/user_data",
    status_code=status.HTTP_201_CREATED,
    description="Эндпоинт для добавления записей в базу данных",
)
async def insert_user_data(user_data: UserDataInsert) -> dict:
    return await db_client.insert_user_data(user_data)

