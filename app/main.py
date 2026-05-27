from fastapi import FastAPI

from app.database import engine, Base
from app.routes.product_route import router
from app.routes.auth_route import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Stock API",
    version="1.0.0"
)

app.include_router(router)

app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "API funcionando"}

