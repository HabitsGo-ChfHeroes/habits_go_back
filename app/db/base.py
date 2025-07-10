from sqlalchemy.orm import declarative_base

Base = declarative_base()

from app.models import food_ingredient
from app.models import food
from app.models import ingredient
from app.models import meal
from app.models import plan_food
from app.models import plan
from app.models import user
from app.models import user_ingredient
from app.models import payment
from app.models import user_habit
