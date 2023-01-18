from fastapi import FastAPI
from .comics import Comics

app = FastAPI(title="FastAPI by NoName")


@app.get('/')
def home():
    return {'Запуск выполнен':'успешно'}


@app.get('/{id}')
def test_project(test: int, q: int = None):
    return {'key': id, 'q': q}

#/"Укажите целое число"?q= "Укажите в виде строки"

@app.get('/id/{id}/auto/{auto}')
def id_and_auto(id: int, auto: str):
    return {'id': id, 'auto': auto}


@app.post('/Comics')
def createcomics(item: Comics):
    return item