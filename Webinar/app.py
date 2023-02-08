from fastapi import FastAPI

from api import router

app = FastAPI()
app.include_router(router)

@app.get('/')
def is_alive():
    return {'Статус сервера': 'True'}