from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get('/')
def greet():
    return ("Hi welcome to the platform")

products = [
    Product(id=1,name="Laptop",description="Gaming Laptop",price=1499,qty=20),
    Product(id=2,name="Mobile",description="Budget Mobile", price=499,qty=30),
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"error" : ("No product found with ID " + str(id))}

@app.post("/products")
def add_product(product: Product):
    products.append(product)
    return {"message " : "Product Added Successfully"}

@app.put("/products")
def update_product(id : int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return {"message" : "product updated succesfully"}
    return {"message " : "No product fount with ID " + str(id)}
