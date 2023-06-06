from fastapi import APIRouter, Depends
from models.user_model import User
from schemas.user_schema import users_serializer
from bson import ObjectId
from config.token import validate_token
from config.db import collection
user = APIRouter()


@user.get("/protec")
async def protec(user: str = Depends(validate_token)):
    return {"mansaje": "Ruta Protegida"}


@user.get("/getAll", tags=["Users"])
async def find_all_users():
    """Get All Users"""
    users = users_serializer(collection.find())
    return {"status": "OK", "data": users}


@user.get("/getUser/{id}", tags=["Users"])
async def get_one_user(id: str):
    """Get One user By Id"""
    user = users_serializer(collection.find({"_id": ObjectId(id)}))
    return {"status": "Ok", "data": user}


@user.post("/create", tags=["Users"])
async def create_user(user: User):
    """Create new User"""
    _id = collection.insert_one(dict(user))
    user = users_serializer(collection.find({"_id": _id.inserted_id}))
    return {"status": "Ok", "data": user}


@user.put("/update/{id}", tags=["Users"])
async def update_user(id: str, user: User):
    """Update User"""
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        },
        {
            "$set": dict(user)
        })
    user = users_serializer(collection.find({"_id": ObjectId(id)}))
    return {"status": "Ok", "data": user}


@user.delete("/delete/{id}", tags=["Users"])
async def delete_user(id: str):
    """Delete User"""
    collection.find_one_and_delete({"_id": ObjectId(id)})
    users = users_serializer(collection.find())
    return {"status": "Ok", "data": []}
