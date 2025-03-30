from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, List
from uuid import UUID   
from decimal import Decimal

from app.schemas.user_schema import UserSchema
from app.schemas.wallet_schema import WalletResponseSchema


class TransactionBase(BaseModel):
    client_id: UUID = Field(...)
    wallet_id: UUID = Field(...)
    value: Decimal = Field(...)


class TransactionSchema(TransactionBase):
    id: Optional[UUID] = None
    client: Optional[UserSchema] = None
    wallet: Optional[WalletResponseSchema] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class TransactionCreateSchema(TransactionBase):
    client_id: UUID = Field(...)
    wallet_id: UUID = Field(...)
    value: Decimal = Field(...)


class TransactionUpdateSchema(TransactionBase):
    client_id: Optional[UUID] = None
    wallet_id: Optional[UUID] = None
    value: Optional[Decimal] = None


class TransactionResponseSchema(TransactionSchema):
    id: UUID
    client: UUID
    wallet: UUID
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
