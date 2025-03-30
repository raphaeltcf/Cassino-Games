from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from typing import Optional, List
from uuid import UUID

from app.models.addres_model import Address
from app.schemas.adrres_schema import AddressSchema

class AddressRepository:
    @staticmethod
    def get_all(db: Session) -> List[Address]:
        return db.query(Address).all()
    
    @staticmethod
    def get_by_id(db: Session, address_id: UUID) -> Optional[Address]:
        return db.query(Address).filter(Address.id == address_id).first()
    
    @staticmethod
    def create(db: Session, address: AddressSchema) -> Address:
        try:
            addrress = Address(
                address=address.address,
                city=address.city,
                state=address.state,
                zip_code=address.zip_code
            )
            db.add(addrress)
            db.commit()
            db.refresh(addrress)
            return address
        except IntegrityError as e:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Address already exists")

