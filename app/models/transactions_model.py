import uuid
from sqlalchemy import Column, ForeignKey, Numeric, Boolean, DateTime
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(UNIQUEIDENTIFIER, primary_key=True, default=uuid.uuid4)
    client_id = Column(UNIQUEIDENTIFIER, ForeignKey("clients.id"), nullable=False)
    wallet_id = Column(UNIQUEIDENTIFIER, ForeignKey("wallets.id"), nullable=False)
    value = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now)
    
    client = relationship("Client", back_populates="transactions")
    wallet = relationship("Wallet", back_populates="transactions")
