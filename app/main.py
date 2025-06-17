from fastapi import FastAPI
from app.api.auth_routes import router as auth_router
from app.api.plan_food_routes import router as plan_food_router
from app.core.cors import configure_cors
from app.db.session import engine
from app.db.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

configure_cors(app)

app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
app.include_router(plan_food_router, prefix="/api", tags=["plan_food"])