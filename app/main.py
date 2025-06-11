from fastapi import FastAPI
from app.api.auth_routes import router as auth_router
from app.core.cors import configure_cors
#from app.db.session import engine
#from app.db.base import Base
from app.api import daily_plan_routes
#Base.metadata.create_all(bind=engine)

app = FastAPI()

configure_cors(app)

app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
app.include_router(daily_plan_routes.router)