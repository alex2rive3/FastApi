from fastapi import FastAPI
from routes.user_routes import user
from routes.auth import auth_routes
from dotenv import load_dotenv
app = FastAPI()
load_dotenv()
app.include_router(user)
app.include_router(auth_routes, prefix="/api")
