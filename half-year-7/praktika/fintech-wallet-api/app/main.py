from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, Query, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import Base, engine, get_db
from app.security import create_access_token, get_current_user, verify_password

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FinTech Wallet API",
    description="API для управления финансовыми транзакциями пользователя",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "FinTech Wallet API is running"}


@app.post("/auth/register", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = crud.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Пользователь с таким email уже существует")
    return crud.create_user(db, user)


@app.post("/auth/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный email или пароль",
            headers={"WWW-Authenticate": "Bearer"},
        )

    crud.create_audit_log(db, user.id, "login", "Успешный вход в систему")
    access_token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me", response_model=schemas.UserOut)
def read_users_me(current_user: models.User = Depends(get_current_user)):
    return current_user


@app.post("/transactions", response_model=schemas.TransactionOut, status_code=status.HTTP_201_CREATED)
def create_transaction(
    transaction: schemas.TransactionCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    new_transaction = crud.create_transaction(db, current_user.id, transaction)
    crud.create_audit_log(
        db,
        current_user.id,
        "create_transaction",
        f"Создана транзакция #{new_transaction.id}",
    )
    return new_transaction


@app.get("/transactions", response_model=list[schemas.TransactionOut])
def get_transactions(
    type: Optional[str] = Query(default=None, pattern="^(income|expense)$"),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    return crud.get_user_transactions(db, current_user.id, type)


@app.get("/transactions/{transaction_id}", response_model=schemas.TransactionOut)
def get_transaction(
    transaction_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    transaction = crud.get_transaction(db, transaction_id, current_user.id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Транзакция не найдена")
    return transaction


@app.put("/transactions/{transaction_id}", response_model=schemas.TransactionOut)
def update_transaction(
    transaction_id: int,
    data: schemas.TransactionUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    transaction = crud.update_transaction(db, transaction_id, current_user.id, data)
    if not transaction:
        raise HTTPException(status_code=404, detail="Транзакция не найдена")

    crud.create_audit_log(
        db,
        current_user.id,
        "update_transaction",
        f"Обновлена транзакция #{transaction_id}",
    )
    return transaction


@app.delete("/transactions/{transaction_id}")
def delete_transaction(
    transaction_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    deleted = crud.delete_transaction(db, transaction_id, current_user.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Транзакция не найдена")

    crud.create_audit_log(
        db,
        current_user.id,
        "delete_transaction",
        f"Удалена транзакция #{transaction_id}",
    )
    return {"message": "Транзакция удалена"}


@app.get("/analytics/summary", response_model=schemas.SummaryOut)
def get_summary(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    return crud.get_summary(db, current_user.id)


@app.get("/audit-logs", response_model=list[schemas.AuditLogOut])
def get_audit_logs(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    return crud.get_audit_logs(db, current_user.id)
