from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, List
from uuid import UUID   

class AddressSchema(BaseModel):
    id: Optional[UUID] = None
    client_id: UUID = Field(...)
    address: str = Field(...)
    city: str = Field(...)
    state: str = Field(...)
    zip_code: str = Field(...)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class AddressCreateSchema(BaseModel):
    client_id: UUID = Field(...)
    address: str = Field(...)
    city: str = Field(...)
    state: str = Field(...)
    zip_code: str = Field(...)

class AddressUpdateSchema(BaseModel):
    address: Optional[str] = Field(None, min_length=3, max_length=100)
    city: Optional[str] = Field(None, min_length=3, max_length=100)
    state: Optional[str] = Field(None, min_length=3, max_length=100)
    zip_code: Optional[str] = Field(None, min_length=3, max_length=100)

class AddressDeleteSchema(BaseModel):
    id: UUID = Field(...)

class AddressResponseSchema(BaseModel):
    id: Optional[UUID] = None
    client_id: UUID = Field(...)
    address: str = Field(...)
    city: str = Field(...)
    state: str = Field(...)
    zip_code: str = Field(...)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None