from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.database import Base, get_db
from app.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def test_full_user_flow():
    register_response = client.post(
        "/auth/register",
        json={
            "email": "test@example.com",
            "full_name": "Test User",
            "password": "password123",
        },
    )
    assert register_response.status_code == 201

    login_response = client.post(
        "/auth/login",
        data={
            "username": "test@example.com",
            "password": "password123",
        },
    )
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    income_response = client.post(
        "/transactions",
        json={
            "amount": 1000,
            "type": "income",
            "category": "Salary",
            "description": "Monthly salary",
        },
        headers=headers,
    )
    assert income_response.status_code == 201

    expense_response = client.post(
        "/transactions",
        json={
            "amount": 250,
            "type": "expense",
            "category": "Food",
            "description": "Groceries",
        },
        headers=headers,
    )
    assert expense_response.status_code == 201

    summary_response = client.get("/analytics/summary", headers=headers)
    assert summary_response.status_code == 200

    summary = summary_response.json()
    assert summary["total_income"] == 1000.0
    assert summary["total_expense"] == 250.0
    assert summary["balance"] == 750.0
