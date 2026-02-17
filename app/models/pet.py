from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from app.database import Base

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, index=True)  # Telegram user ID
    name = Column(String, default="Lumina")
    status = Column(String, default="alive")  # alive, sick, sleeping
    mood = Column(Integer, default=50)
    energy = Column(Integer, default=50)
    hunger = Column(Integer, default=100)  # 0 = голоден, 100 = сыт
    personality = Column(String, default="neutral")  # playful, calm, etc.
    level = Column(Integer, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())