from sqlalchemy import func
from sqlalchemy.orm import Session

from app import models, schemas
from app.security import get_password_hash


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=get_password_hash(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    create_audit_log(db, db_user.id, "register", "Пользователь зарегистрирован")
    return db_user


def create_audit_log(db: Session, user_id: int, action: str, details: str | None = None):
    log = models.AuditLog(
        user_id=user_id,
        action=action,
        details=details,
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log


def create_transaction(db: Session, user_id: int, transaction: schemas.TransactionCreate):
    db_transaction = models.Transaction(
        owner_id=user_id,
        amount=transaction.amount,
        type=transaction.type,
        category=transaction.category,
        description=transaction.description,
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def get_user_transactions(db: Session, user_id: int, transaction_type: str | None = None):
    query = db.query(models.Transaction).filter(models.Transaction.owner_id == user_id)
    if transaction_type:
        query = query.filter(models.Transaction.type == transaction_type)
    return query.order_by(models.Transaction.created_at.desc()).all()


def get_transaction(db: Session, transaction_id: int, user_id: int):
    return (
        db.query(models.Transaction)
        .filter(models.Transaction.id == transaction_id, models.Transaction.owner_id == user_id)
        .first()
    )


def update_transaction(db: Session, transaction_id: int, user_id: int, data: schemas.TransactionUpdate):
    transaction = get_transaction(db, transaction_id, user_id)
    if not transaction:
        return None

    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(transaction, field, value)

    db.commit()
    db.refresh(transaction)
    return transaction


def delete_transaction(db: Session, transaction_id: int, user_id: int):
    transaction = get_transaction(db, transaction_id, user_id)
    if not transaction:
        return False

    db.delete(transaction)
    db.commit()
    return True


def get_summary(db: Session, user_id: int):
    total_income = (
        db.query(func.coalesce(func.sum(models.Transaction.amount), 0.0))
        .filter(models.Transaction.owner_id == user_id, models.Transaction.type == "income")
        .scalar()
    )

    total_expense = (
        db.query(func.coalesce(func.sum(models.Transaction.amount), 0.0))
        .filter(models.Transaction.owner_id == user_id, models.Transaction.type == "expense")
        .scalar()
    )

    return {
        "total_income": float(total_income or 0.0),
        "total_expense": float(total_expense or 0.0),
        "balance": float((total_income or 0.0) - (total_expense or 0.0)),
    }


def get_audit_logs(db: Session, user_id: int):
    return (
        db.query(models.AuditLog)
        .filter(models.AuditLog.user_id == user_id)
        .order_by(models.AuditLog.created_at.desc())
        .all()
    )
