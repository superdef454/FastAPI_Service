from fastapi import FastAPI

from routes import router

app = FastAPI()
app.include_router(router)

# def check_status(timer = 1 hours)

@app.get('/')
def is_alive():
    return {'Статус сервера': 'Активен'}