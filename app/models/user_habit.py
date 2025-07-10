from sqlalchemy import Column, Integer, Boolean, ForeignKey, Date
from sqlalchemy.orm import relationship
from datetime import date
from app.db.base import Base

class UserHabit(Base):
    __tablename__ = "user_habits"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True, nullable=False)
    exercise_days = Column(Integer, nullable=False)
    smokes = Column(Boolean, nullable=False)
    water_glasses = Column(Integer, nullable=False)
    sleep_7h = Column(Boolean, nullable=False)
    updated_at = Column(Date, nullable=False, default=date.today)

    user = relationship("User", back_populates="habit")
