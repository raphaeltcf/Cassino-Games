from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, List
from uuid import UUID   
from decimal import Decimal

from app.schemas.user_schema import UserSchema
from app.schemas.games_schema import GameResponseSchema


class HistoryMatchBase(BaseModel):
    client_id: UUID = Field(...)
    match_id: UUID = Field(...)
    value_bet: Decimal = Field(...)
    games_id: UUID = Field(...)


class HistoryMatchSchema(HistoryMatchBase):
    id: Optional[UUID] = None
    client: Optional[UserSchema] = None
    games: Optional[GameResponseSchema] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class HistoryMatchCreateSchema(HistoryMatchBase):
    client_id: UUID = Field(...)
    value_bet: Decimal = Field(...)
    games_id: UUID = Field(...)

class HistoryMatchUpdateSchema(HistoryMatchBase):
    client_id: Optional[UUID] = None
    value_bet: Optional[Decimal] = None
    games_id: Optional[UUID] = None

class HistoryMatchResponseSchema(HistoryMatchSchema):
    id: UUID
    client: UUID
    games: UUID
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
