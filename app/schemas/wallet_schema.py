from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, List
from uuid import UUID   
from decimal import Decimal

class WalletBase(BaseModel):
    client_id: UUID = Field(...)
    balance: Decimal = Field(...)

class WalletCreateSchema(BaseModel):
    balance: Decimal = Field(...)

class WalletResponseSchema(BaseModel):
    id: UUID
    balance: Decimal
    client: UUID    
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class WalletUpdateSchema(BaseModel):
    balance: Optional[Decimal] = None
