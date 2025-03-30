from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, List
from uuid import UUID   
from decimal import Decimal

class GameBase(BaseModel):
    name: str = Field(...)
    description: str = Field(...)
    is_active: bool = Field(...)

class GameSchema(GameBase):
    id: Optional[UUID] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class GameCreateSchema(GameBase):
    name: str = Field(...)
    description: str = Field(...)
    is_active: bool = Field(...)

class GameUpdateSchema(GameBase):
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

class GameResponseSchema(GameSchema):
    id: UUID
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None