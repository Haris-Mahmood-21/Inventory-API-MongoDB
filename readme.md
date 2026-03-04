# Inventory-API-MongoDB

A robust, RESTful web API for managing an inventory. This project demonstrates backend development using FastAPI and a NoSQL database (MongoDB), completely separating the data layer from the application logic.

# Tech Stack

Framework: FastAPI
Database: MongoDB (via PyMongo)
Data Validation: Pydantic
Environment Management: python-dotenv
Server: Uvicorn

# Features

**Create**: Add new grocery products with automated data validation.
**Read**: Fetch the entire current inventory.
**Update**: Modify the stock quantities of existing items.
**Delete**: Remove discontinued products from the database.
**Secure Setup**: Uses environment variables (.env) to protect database connection strings.

## Installation & Setup

1. **Clone the repository:**
git clone https://github.com/your-username/grocery-api-mongodb.git
cd grocery-api-mongodb

2. **Create and activate a virtual environment:**
python -m venv venv
source venv/bin/activate (On Windows use: venv\Scripts\activate)

3. **Install the dependencies:**
pip install -r requirements.txt

4. **Set up the Database:**
Create a .env file in the root directory.
Add your MongoDB connection string inside it: MONGO_URI=mongodb://localhost:27017/

5. **Run the server:**
uvicorn main:app --reload

## 📡 API Endpoints
Once the server is running, you can view the interactive documentation at http://127.0.0.1:8000/docs.

GET /view_inventory
Description: Returns all items in the inventory.
JSON Body Required: No

POST /add_product
Description: Adds a new product to the database.
JSON Body Required: Yes (Product model)

PUT /update_stock
Description: Updates the quantity of a specific item.
JSON Body Required: Yes (StockUpdate model)

DELETE /delete_product
Description: Deletes an item by product name.
JSON Body Required: No (URL parameter)