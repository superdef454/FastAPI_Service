# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship
from enum import Enum
from pydantic import BaseModel
import datetime

class video_status(str, Enum):
    none = "none" # Ничего
    converted = "converted" # Конвертируется
    downloaded = "downloaded" # Скачивается
    finished = "finished" # Сохранено
    delete = "delete" # Удалено с сервера webinar

# Таблица ID видео
class ID(BaseModel):
    id: str # 8-и значное число ответ с api
    status: video_status
    title: str
    createAt: datetime.datetime
    link: str # "https://events.webinar.ru/supportservice/2278021/record-new/2319963"
    # Ещё можно добавить id создателя и размер видео

# Отдельная таблица с ID конвертации видео с внешним ключом на само видео (если id конвертации и видео одинаковые, то эта таблица не нужна)
class conversionID(BaseModel):
    conversion_id: str
    # video_id: ID # внешний ключ на видео, как правильно настроить хз

# Я бы ещё добавил таблицу с скаченными видео