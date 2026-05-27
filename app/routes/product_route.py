from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from app.database import SessionLocal
from app.models.product_model import Product
from app.schemas.product_schema import (
    ProductCreate,
    ProductResponse
)
from app.schemas.product_schema import ProductUpdate

from app.auth.auth_bearer import get_current_user
from app.auth.role_checker import admin_required

router = APIRouter()

# Dependencia DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE
@router.post("/products")
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    new_product = Product(
        name=product.name,
        price=product.price,
        stock=product.stock
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

# READ ALL
@router.get("/products", response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

# READ ONE
@router.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return db.query(Product).filter(
        Product.id == product_id
    ).first()

# DELETE
@router.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    
    admin_required(user)

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    db.delete(product)
    db.commit()

    return {"message": "Producto eliminado"}

# UPDATE
@router.put("/products/{product_id}")
def update_product(
    product_id: int,
    updated_product: ProductUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    
    admin_required(user)

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:
        return {"message": "Producto no encontrado"}

    product.name = updated_product.name
    product.price = updated_product.price
    product.stock = updated_product.stock

    db.commit()

    return {"message": "Producto actualizado"}