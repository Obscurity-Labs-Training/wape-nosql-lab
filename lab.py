from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.nosql_lab_db

# Example 1: Find all users
def find_all_users():
    users = db.Users.find({})
    for user in users:
        print(user)

# Example 2: Insert a new user
def insert_new_user():
    db.Users.insert_one({ "name": "Bob Martin", "email": "bob@example.com", "age": 28 })
    print("New user inserted.")

# Example 3: Update an existing user's email
def update_user_email():
    db.Users.update_one({ "name": "John Doe" }, { "$set": { "email": "john.doe@newdomain.com" } })
    print("John Doe's email updated.")

# Example 4: Delete a user
def delete_user():
    db.Users.delete_one({ "name": "Alice Brown" })
    print("Alice Brown deleted.")

if __name__ == "__main__":
    print("Choose an operation:")
    print("1. Find all users")
    print("2. Insert a new user")
    print("3. Update John Doe's email")
    print("4. Delete Alice Brown")
    
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == "1":
        find_all_users()
    elif choice == "2":
        insert_new_user()
    elif choice == "3":
        update_user_email()
    elif choice == "4":
        delete_user()
    else:
        print("Invalid choice.")
