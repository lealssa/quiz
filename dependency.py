from functools import lru_cache
from database import SessionLocal

import domain

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@lru_cache
def get_quiz():
    quiz = domain.Quiz()
    return quiz