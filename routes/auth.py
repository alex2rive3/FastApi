from fastapi import APIRouter, Header
from models.user_model import User
from config.token import write_token, validate_token
from fastapi.responses import JSONResponse
auth_routes = APIRouter()


@auth_routes.post("/login")
def login(user: User):
    print(user.dict())
    if user.name == "Alex Rolando":
        return write_token(user.dict())
    else:
        return JSONResponse(content={"menssage": "User not Found"}, status_code=404)


@auth_routes.post("/verify/token")
def verify_token(Authorization: str = Header(None)):
    token = Authorization.split(" ")[1]
    return validate_token(token, output=True)
