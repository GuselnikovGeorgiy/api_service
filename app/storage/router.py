from fastapi import APIRouter, status, Depends, HTTPException

from app.storage.database import db_client
from app.storage.exceptions import BadDataException
from app.storage.models import UserDataInsert, UserDataGet
from app.storage.schemas import UserDataFilter
from app.storage.services import validate_fetch_params

router = APIRouter(tags=['Storage'], prefix="/user_data")


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    description="Эндпоинт для получения записей из базы данных по параметрам фильтрации",
    summary="Получить список пользователей по фильтрам",
)
async def get_filtered_user_data(
        filter_params: UserDataFilter = Depends(),
) -> list[dict]:
    try:
        _ = validate_fetch_params(
            filter_params.ip_address,
            filter_params.min_longitude,
            filter_params.max_longitude,
            filter_params.min_latitude,
            filter_params.max_latitude,
            filter_params.connect_time_from,
            filter_params.connect_time_to,
            filter_params.disconnect_time_from,
            filter_params.disconnect_time_to,
            filter_params.connection_duration_from,
            filter_params.connection_duration_to,
            filter_params.session_id,
            filter_params.limit,
        )
    except BadDataException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.errors,
        )
    else:
        filter_query = filter_params.dict(exclude_none=True)
        return await db_client.find_user_data(filter_query)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    description="Эндпоинт для добавления записей в базу данных",
    summary="Добавить запись в базу данных",
)
async def insert_user_data(user_data: UserDataInsert) -> dict:
    return await db_client.insert_user_data(user_data)


@router.post(
    "/list",
    status_code=status.HTTP_201_CREATED,
    description="Эндпоинт для добавления нескольких записей в базу данных",
    summary="Добавить список записей в базу данных",
)
async def insert_list_of_user_data(user_data: list[UserDataInsert]) -> list[dict]:
    return await db_client.insert_list_of_user_data(user_data)
