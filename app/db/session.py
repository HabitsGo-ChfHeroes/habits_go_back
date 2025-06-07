from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()