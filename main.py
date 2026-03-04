from fastapi import FastAPI
from pydantic import BaseModel
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

database_url = os.getenv("MONGO_URI")
client = pymongo.MongoClient(database_url)
db = client["market"]
collection = db["inventory"]

class Product(BaseModel):
    product_name: str
    category: str
    price: float
    quantity_in_stock: int

class StockUpdate(BaseModel):
    new_quantity: int

@app.post("/add_product")
def add_product(product: Product):
    product_dict = product.model_dump()
    collection.insert_one(product_dict)
    
    return {"message": f"'{product.product_name}' has been added to the inventory."}

@app.get("/view_inventory")
def view_inventory():   
    products = list(collection.find({}, {"_id": 0}))
    
    if not products:
        return {"message": "The inventory is currently empty. Try adding some products!"}
    
    return {"inventory": products}  

@app.put("/update_stock")
def update_stock(product_name: str, update_data: StockUpdate):
    
    result = collection.update_one(
        {"product_name": product_name},
        {"$set": {"quantity_in_stock": update_data.new_quantity}}
    )
    
    if result.matched_count == 0:
        return {"message": f"Product '{product_name}' not found in inventory."}
    else:
        return {"message": f"Stock updated successfully for product '{product_name}'."}
    
@app.delete("/delete_product")
def delete_product(product_name: str):
    result = collection.delete_one({"product_name": product_name})
    
    if result.deleted_count == 0:
        return {"message": f"Product '{product_name}' not found in inventory."}
    else:
        return {"message": f"Product '{product_name}' has been deleted from the inventory."}
