from fastapi import APIRouter, Response
from typing import List
import datetime

from models.models import ID as id
from views.ID import ID 

router = APIRouter(
    prefix='/records',
)

@router.get('')
def get_list_of_records( # Получить список записей
    from_data: datetime.date,
    to: datetime.date = datetime.datetime.now()
):
    return ID.get_list_of_records_from_webinar(from_data, to)

@router.delete('')
def delete_records( # Удалить список записей
    recordID: List[str]
):
    return ID.Delete()

@router.post('/conversions')
def get_list_of_records( # Поставить записи на конвертацию
    recordID: List[str]
):
    return ID.Start_conversion(recordID)

@router.get('/conversions')
def Check_conversion_status( # Проверить статус конвертации
    conversionID: str
):
    return ID.Check_conversion_status(conversionID)