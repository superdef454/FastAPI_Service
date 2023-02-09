from fastapi import APIRouter, Response
import datetime

# from models.models import ID
from views.ID import ID 

router = APIRouter(
    prefix='/records',
)

@router.get('/')
def base(
):
    out = {"Ответ сервера":f"{ID.zapros().text}"}
    return out

@router.get('/')
def get_list_of_records(
    from_data: datetime.date,
    to: datetime.date = datetime.datetime.now()
):
    out = {
        "Вернуться записи начиная с":f"{from_data}",
        "И заканчивая":f"{to}"
        }
    return out