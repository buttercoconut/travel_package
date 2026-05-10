from fastapi import FastAPI
from .routes import package_routes, user_routes

app = FastAPI(title="Travel Package API")
app.include_router(package_routes.router, prefix="/packages", tags=["packages"])
app.include_router(user_routes.router, prefix="/users", tags=["users"])
