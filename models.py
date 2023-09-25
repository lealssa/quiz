from uuid import uuid4
from typing import List, Optional
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TEXT
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    pass
    
class Pergunta(Base):
    
    __tablename__ = "perguntas"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    uuid: Mapped[str] = mapped_column(index=True, unique=True, default=lambda: uuid4().hex)
    texto_pergunta: Mapped[str] = mapped_column(TEXT, unique=True)
    opcoes: Mapped[List["OpcaoPergunta"]] = relationship("OpcaoPergunta", back_populates="pergunta", cascade="all, delete")

class OpcaoPergunta(Base):
    
    __tablename__ = "opcoes_pergunta"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    uuid: Mapped[str] = mapped_column(index=True, unique=True, default=lambda: uuid4().hex)
    texto_opcao: Mapped[str] = mapped_column(TEXT)
    explicacao: Mapped[Optional[str]] = mapped_column(TEXT)
    opcao_correta: Mapped[bool] = mapped_column(default=False)
    
    pergunta_id: Mapped[int] = mapped_column(ForeignKey("perguntas.id"))
    pergunta: Mapped["Pergunta"] = relationship("Pergunta", back_populates="opcoes")