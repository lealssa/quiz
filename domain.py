from uuid import uuid4
from typing import List, NoReturn
import database, models
import sqlalchemy
from sqlalchemy import select, func

class PerguntaExisteError(Exception):
    pass

class PerguntaNaoEncontradaError(Exception):
    pass

class Quiz:
    
    def get_pergunta_aleatoria(self, db: database.SessionLocal) -> models.Pergunta: 
        db_pergunta = db.query(models.Pergunta).order_by(func.random()).first()
        if not db_pergunta:
            raise PerguntaNaoEncontradaError('Nenhuma pergunta encontrada.')
        return db_pergunta
    
    def get_perguntas(self, db: database.SessionLocal) -> List[models.Pergunta]:
        return db.query(models.Pergunta).all()
    
    def cria_pergunta(self, db: database.SessionLocal, pergunta: models.Pergunta):
        try:
            db.add(pergunta)
            db.commit()
        except sqlalchemy.exc.IntegrityError as err:
            print(str(err))
            raise PerguntaExisteError('Pergunta já existe.')
        
    def deleta_pergunta_pelo_uuid(self, db: database.SessionLocal, uuid: str) -> NoReturn:
        db_pergunta = db.query(models.Pergunta).filter(models.Pergunta.uuid == uuid).first()
        if not db_pergunta:
            raise PerguntaNaoEncontradaError('Pergunta não encontrada.')
        db.delete(db_pergunta)
        db.commit()
            