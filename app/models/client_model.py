import uuid
from sqlalchemy import Column, ForeignKey, String, Boolean, DateTime
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(UNIQUEIDENTIFIER, primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    cpf = Column(String(11), nullable=False, unique=True)
    phone = Column(String(15), nullable=False, unique=True)
    address_id = Column(UNIQUEIDENTIFIER, ForeignKey("addresses.id"), nullable=False, unique=True)
    password = Column(String(25), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now)

    wallet = relationship("Wallet", back_populates="client", uselist=False, cascade="all, delete-orphan")
    address = relationship("Address", back_populates="clients")
    history_matches = relationship("HistoryMatch", back_populates="client")
    transactions = relationship("Transaction", back_populates="client")

    
