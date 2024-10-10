from pymongo import MongoClient

# Connect to MongoDB (make sure MongoDB is running on localhost:27017)
client = MongoClient("mongodb://localhost:27017/")

# Create the database and collections
db = client['nosql_lab_db']

# Data to insert
users = [
    { "name": "John Doe", "email": "john@example.com", "age": 30 },
    { "name": "Jane Smith", "email": "jane@example.com", "age": 25 },
    { "name": "Alice Brown", "email": "alice@example.com", "age": 35 }
]

orders = [
    { "order_id": 1, "user_id": 1, "product_name": "Laptop", "price": 1200 },
    { "order_id": 2, "user_id": 1, "product_name": "Phone", "price": 800 },
    { "order_id": 3, "user_id": 2, "product_name": "Tablet", "price": 500 }
]

# Insert data into collections
db.Users.insert_many(users)
db.Orders.insert_many(orders)

print("Data loaded successfully.")
