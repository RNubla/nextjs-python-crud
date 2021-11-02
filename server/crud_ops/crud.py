from sqlalchemy.orm import Session
from db import db_model
from schema import item, user


def get_user(db: Session, user_id: int):
    return db.query(db_model.User).filter(db_model.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(db_model.User).filter(db_model.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_model.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = db_model.User(
        email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(db_model.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: item.ItemCreate, user_id: int):
    db_item = db_model.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
