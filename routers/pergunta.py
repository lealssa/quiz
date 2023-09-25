import time

from typing import List
from fastapi import status, HTTPException, Depends, APIRouter, Response

import schemas, domain, dependency, database, models

router = APIRouter()

@router.get("", response_model=List[schemas.Pergunta])
async def get_perguntas(quiz: domain.Quiz = Depends(dependency.get_quiz), db: database.SessionLocal = Depends(dependency.get_db)):
    time.sleep(0.5)
    db_perguntas = quiz.get_perguntas(db)
    return db_perguntas

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_pergunta(pergunta_in: schemas.PerguntaIn, quiz: domain.Quiz = Depends(dependency.get_quiz), db: database.SessionLocal = Depends(dependency.get_db)):
    try:
        nova_pergunta_dict = pergunta_in.dict()
        nova_pergunta_dict['opcoes'] = [ models.OpcaoPergunta(**x) for x in nova_pergunta_dict['opcoes'] ]
        db_pergunta = models.Pergunta(**nova_pergunta_dict)
        
        quiz.cria_pergunta(db, db_pergunta)
        
        headers = { 'Location': f'/api/perguntas/{db_pergunta.uuid}' }
        
        return Response(status_code=status.HTTP_201_CREATED, headers=headers)
    
    except domain.PerguntaExisteError as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))
    
@router.put("/{uuid_pergunta}", status_code=status.HTTP_204_NO_CONTENT)
async def update_pergunta(uuid_pergunta: str, pergunta_update: schemas.PerguntaUpdate, quiz: domain.Quiz = Depends(dependency.get_quiz), db: database.SessionLocal = Depends(dependency.get_db)):
    try:
        pass
    except domain.PerguntaNaoEncontradaError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))    
    
@router.delete("/{uuid_pergunta}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_pergunta(uuid_pergunta: str, quiz: domain.Quiz = Depends(dependency.get_quiz), db: database.SessionLocal = Depends(dependency.get_db)):
    try:
        quiz.deleta_pergunta_pelo_uuid(db, uuid_pergunta)
    except domain.PerguntaNaoEncontradaError as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(err))