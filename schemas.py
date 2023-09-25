from pydantic import BaseModel, ConfigDict
from typing import List
    
class OpcaoPerguntaBase(BaseModel): 
    texto_opcao: str    
    opcao_correta: bool
    explicacao: str | None

class OpcaoPergunta(OpcaoPerguntaBase):
    uuid: str
    
    class Config:
        orm_mode = True
    
class OpcaoPerguntaIn(OpcaoPerguntaBase):
    pass
    
class OpcaoPerguntaUpdate(BaseModel):
    uuid: str | None
    texto_opcao: str | None
    opcao_correta: bool | None
    explicacao: str | None
    
class OpcaoPerguntaQuiz(BaseModel):
    uuid: str
    texto_opcao: str
    
    class Config:
        orm_mode = True        
    
class PerguntaBase(BaseModel):    
    texto_pergunta: str        
    opcoes: List[OpcaoPergunta]

class Pergunta(PerguntaBase):       
    uuid: str 
    
    class Config:
        orm_mode = True    
    
class PerguntaIn(PerguntaBase):
    opcoes: List[OpcaoPerguntaIn]
    
class PerguntaUpdate(BaseModel):
    texto_pergunta: str | None
    opcoes: List[OpcaoPerguntaUpdate] = []    
    
class PerguntaQuiz(Pergunta):
    opcoes: List[OpcaoPerguntaQuiz]
    
    