from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    full_name: str = Field(min_length=2, max_length=255)
    password: str = Field(min_length=8, max_length=128)


class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str


class TransactionCreate(BaseModel):
    amount: float = Field(gt=0)
    type: Literal["income", "expense"]
    category: str = Field(min_length=2, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)


class TransactionUpdate(BaseModel):
    amount: Optional[float] = Field(default=None, gt=0)
    type: Optional[Literal["income", "expense"]] = None
    category: Optional[str] = Field(default=None, min_length=2, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)


class TransactionOut(BaseModel):
    id: int
    amount: float
    type: str
    category: str
    description: Optional[str]
    created_at: datetime
    owner_id: int

    model_config = ConfigDict(from_attributes=True)


class SummaryOut(BaseModel):
    total_income: float
    total_expense: float
    balance: float


class AuditLogOut(BaseModel):
    id: int
    action: str
    details: Optional[str]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
