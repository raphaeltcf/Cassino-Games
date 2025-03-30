import uuid 
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base

class Address(Base):
    __tablename__ = "addresses"

    id = Column(UNIQUEIDENTIFIER, primary_key=True, default=uuid.uuid4)
    address = Column(String(255), nullable=False)
    city = Column(String(100), nullable=False)
    state = Column(String(100), nullable=False)
    zip_code = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now)
    
    client = relationship("Client", back_populates="addresses", cascade="all, delete-orphan")
