from fastapi import FastAPI
from app.api.auth_routes import router as auth_router
from app.db.session import engine
from app.db.base import Base
from app.core.cors import configure_cors

Base.metadata.create_all(bind=engine)

app = FastAPI()

configure_cors(app)

app.include_router(auth_router, prefix="/api/auth", tags=["auth"])