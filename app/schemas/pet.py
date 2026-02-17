from pydantic import BaseModel
from typing import Optional

class PetCreate(BaseModel):
    user_id: int
    name: Optional[str] = "Lumina"

class PetUpdate(BaseModel):
    mood: Optional[int] = None
    energy: Optional[int] = None
    hunger: Optional[int] = None

class PetResponse(BaseModel):
    id: int
    user_id: int
    name: str
    status: str
    mood: int
    energy: int
    hunger: int
    personality: str
    level: int

    class Config:
        from_attributes = True