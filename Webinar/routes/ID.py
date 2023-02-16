from fastapi import APIRouter, Response
from typing import List
import datetime

from models.models import ID as id
from views.ID import ID 

router = APIRouter(
    prefix='/records',
)

@router.get('')
async def get_list_of_records( # Получить список записей
    from_data: datetime.date,
    to: datetime.date = datetime.datetime.now().date()
):
    return await ID.get_list_of_records_from_webinar(from_data, to)

@router.delete('')
async def delete_records( # Удалить список записей
    recordID: List[str]
):
    return await ID.Delete_records_from_webinar(recordID)

@router.post('/conversions')
async def get_list_of_records( # Поставить записи на конвертацию
    recordID: List[str]
):
    return await ID.Start_conversion(recordID)

@router.get('/conversions')
async def Check_conversion_status( # Проверить статус конвертации
    conversionID: str
):
    return await ID.Check_conversion_status(conversionID)

@router.post('/check')
def Update(
):
    return ID.Update()