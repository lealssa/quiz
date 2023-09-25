import time

from fastapi import status, HTTPException, Depends, APIRouter

import schemas, domain, dependency, database

router = APIRouter()

@router.get("", response_model=schemas.PerguntaQuiz)
async def get_pergunta_quiz(quiz: domain.Quiz = Depends(dependency.get_quiz), db: database.SessionLocal = Depends(dependency.get_db)):
    time.sleep(0.5)
    try:
        db_pergunta = quiz.get_pergunta_aleatoria(db)    
        return db_pergunta
    except domain.PerguntaNaoEncontradaError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))