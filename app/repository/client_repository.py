import uuid
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from typing import Optional, List
from uuid import UUID

from app.models.client_model import Client
from app.schemas.user_schema import UserSchema


class ClientRepository:

    @staticmethod
    def get_all(db: Session) -> List[Client]:
        return db.query(Client).filter(Client.is_active == True).all()

    @staticmethod
    def get_by_id(db: Session, client_id: UUID) -> Optional[Client]:
        return (
            db.query(Client)
            .filter(Client.is_active == True, Client.id == client_id)
            .first()
        )

    @staticmethod
    def get_by_email(db: Session, email: str) -> Optional[Client]:
        return (
            db.query(Client)
            .filter(Client.is_active == True, Client.email == email)
            .first()
        )

    @staticmethod
    def get_by_cpf(db: Session, cpf: str) -> Optional[Client]:
        return (
            db.query(Client).filter(Client.is_active == True, Client.cpf == cpf).first()
        )

    @staticmethod
    def get_by_phone(db: Session, phone: str) -> Optional[Client]:
        return (
            db.query(Client)
            .filter(Client.is_active == True, Client.phone == phone)
            .first()
        )

    @staticmethod
    def create(db: Session, address_id: uuid.UUID, client: UserSchema) -> Client:
        try:
            existing_client = ClientRepository.get_by_email(db, client.email)
            if existing_client:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT, detail="Client already exists"
                )
            new_client = Client(
                name=client.name,
                email=client.email,
                cpf=client.cpf,
                address_id=address_id,
                phone=client.phone,
            )
            db.add(new_client)
            db.commit()
            db.refresh(new_client)
            return new_client
        except IntegrityError as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=f"Erro de integridade: {str(e)}"
            ) from e

    @staticmethod 
    def update(db: Session, client_id: UUID, client: UserSchema) -> Client:
            clientDb = ClientRepository.get_by_id(db, client_id)
            if not clientDb:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="Client not found"
                )
            if client.name is not None:
                clientDb.name = client.name
            if client.email is not None and clientDb.email != client.email:
                existing_client = ClientRepository.get_by_email(db, client.email)
                if existing_client and existing_client.id != clientDb.id:
                    raise HTTPException(
                        status_code=status.HTTP_409_CONFLICT, detail="Client already exists"
                    )
                clientDb.email = client.email
            if client.cpf is not None and clientDb.cpf != client.cpf:
                existing_client = ClientRepository.get_by_cpf(db, client.cpf)
                if existing_client and existing_client.id != clientDb.id:
                    raise HTTPException(
                        status_code=status.HTTP_409_CONFLICT, detail="Client already exists"
                    )
                clientDb.cpf = client.cpf
            if client.phone is not None and clientDb.phone != client.phone:
                existing_client = ClientRepository.get_by_phone(db, client.phone)
                if existing_client and existing_client.id != clientDb.id:
                    raise HTTPException(
                        status_code=status.HTTP_409_CONFLICT, detail="Client already exists"
                    )
                clientDb.phone = client.phone
            if client.is_active is not None:
                clientDb.is_active = client.is_active
            try: 
                db.commit()
                db.refresh(clientDb)
                return clientDb
            except IntegrityError as e:
                db.rollback()
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, detail=f"Erro de integridade: {str(e)}"
                ) from e

    @staticmethod
    def delete(db: Session, client_id: UUID) -> bool:
        clientDb = ClientRepository.get_by_id(db, client_id)
        if not clientDb:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Client not found"
            )
            
        clientDb.is_active = False
        db.commit()
        return True
