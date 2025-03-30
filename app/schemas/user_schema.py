from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, List
from uuid import UUID   

from app.schemas.adrres_schema import AddressSchema
from app.schemas.wallet_schema import WalletResponseSchema
from app.schemas.history_match_schema import HistoryMatchResponseSchema
from app.schemas.transaction_schema import TransactionResponseSchema


class UserBase(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    cpf: str = Field(...)
    phone: str = Field(...)

class UserSchema(BaseModel):
    id: Optional[UUID] = None
    name: str = Field(...)
    email: EmailStr = Field(...)
    cpf: str = Field(...)
    phone: str = Field(...)
    address: Optional[AddressSchema] = None
    wallet: Optional[WalletResponseSchema] = None
    history_matches: Optional[List[HistoryMatchResponseSchema]] = None
    transactions: Optional[List[TransactionResponseSchema]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class UserResponseSchema(BaseModel):
    id: UUID
    name: str = Field(...)
    email: EmailStr = Field(...)
    cpf: str = Field(...)
    phone: str = Field(...)
    address: Optional[AddressSchema] = None
    wallet: Optional[WalletResponseSchema] = None
    history_matches: Optional[List[HistoryMatchResponseSchema]] = None
    transactions: Optional[List[TransactionResponseSchema]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class UserCreateSchema(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    cpf: str = Field(...)
    phone: str = Field(...)
    address: Optional[AddressSchema] = None
    wallet: Optional[WalletResponseSchema] = None
    history_matches: Optional[List[HistoryMatchResponseSchema]] = None
    transactions: Optional[List[TransactionResponseSchema]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class UserUpdateSchema(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    email: Optional[EmailStr] = None
    cpf: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[AddressSchema] = None
    wallet: Optional[WalletResponseSchema] = None
    history_matches: Optional[List[HistoryMatchResponseSchema]] = None
    transactions: Optional[List[TransactionResponseSchema]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

