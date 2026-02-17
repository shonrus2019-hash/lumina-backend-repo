from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.pet import Pet
from app.schemas.pet import PetCreate, PetUpdate, PetResponse

router = APIRouter(prefix="/pets", tags=["pets"])

@router.get("/{user_id}", response_model=PetResponse)
def get_pet(user_id: int, db: Session = Depends(get_db)):
    pet = db.query(Pet).filter(Pet.user_id == user_id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

@router.post("/", response_model=PetResponse)
def create_pet(pet_data: PetCreate, db: Session = Depends(get_db)):
    pet = Pet(**pet_data.dict())  # v1 использует .dict()
    db.add(pet)
    db.commit()
    db.refresh(pet)
    return pet

@router.put("/{user_id}", response_model=PetResponse)
def update_pet(user_id: int, pet_update: PetUpdate, db: Session = Depends(get_db)):
    pet = db.query(Pet).filter(Pet.user_id == user_id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    for field, value in pet_update.model_dump(exclude_unset=True).items():
        setattr(pet, field, value)

    db.commit()
    db.refresh(pet)
    return pet