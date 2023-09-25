import locale
locale.setlocale(locale.LC_TIME, 'pt_BR')

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="assets"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse, tags=['HTML'])
async def index(request: Request):
    return templates.TemplateResponse('index.html', context={ 'request': request })

from database import engine
import models

models.Base.metadata.create_all(bind=engine)

from routers import quiz, pergunta

app.include_router(pergunta.router, prefix='/api/perguntas', tags=['Pergunta'])
app.include_router(quiz.router, prefix='/api/quiz', tags=['Quiz'])