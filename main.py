from fastapi import FastAPI
import models
from dbconfig import SessionLocal, engine
from models import User
from pydantic import BaseModel

app = FastAPI()

models.Base.metadata.create_all(engine)


# pydanctic model for user
class UserRequest(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str
    age: int
    role: str


# get method to get all users
@app.get("/users/", response_model=None)
def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    return users


# get method to get user by id
@app.get("/users/{user_id}", response_model=None)
def get_user(user_id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    print(user)
    db.close()
    return user


# post method to create a user
@app.post("/users/", response_model=UserRequest)
def create_user(user: UserRequest):
    db = SessionLocal()
    db_user = User(firstname=user.firstname, lastname=user.lastname, email=user.email, password=user.password,
                   age=user.age, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# delete method to delete a user
@app.delete("/users/{user_id}", response_model=None)
def delete_user(user_id: int):
    db = SessionLocal()
    db.query(User).filter(User.id == user_id).delete()
    db.commit()
    return None

# update method to update a user
@app.put("/users/{user_id}", response_model=UserRequest)
def update_user(user_id: int, user: UserRequest):
    db = SessionLocal()
    db_user = db.query(User).filter(User.id == user_id).first()
    db_user.firstname = user.firstname
    db_user.lastname = user.lastname
    db_user.email = user.email
    db_user.password = user.password
    db_user.age = user.age
    db_user.role = user.role
    db.commit()
    db.refresh(db_user)
    return db_user


# uvicorn main:app --reload
