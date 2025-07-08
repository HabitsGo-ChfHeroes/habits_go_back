from sqlalchemy import Column, Integer, Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.base import Base

class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(Date, nullable=False)

    user = relationship("User", back_populates="plans")
    plan_foods = relationship("PlanFood", back_populates="plan", lazy="selectin")

    __table_args__ = (UniqueConstraint('user_id', 'date', name='_user_date_uc'),)