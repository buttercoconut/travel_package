# main.py
from fastapi import FastAPI
from app.routes import package_routes, auth_routes

app = FastAPI(title="Travel Package API")

app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
app.include_router(package_routes.router, prefix="/packages", tags=["packages"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Travel Package API"}
