from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get('/')
def greet():
    return ("Hi welcome to the platform")

products = [
    Product(id=1,name="Laptop",description="Gaming Laptop",price=1499,qty=20),
    Product(id=2,name="Mobile",description="Budget Mobile", price=499,qty=30)
]

@app.get("/products")
def get_all_products():
    return products