# NoSQL Lab - MongoDB

This lab provides hands-on experience with MongoDB, where you'll work with CRUD operations, querying, and data relationships using flat collections. The lab is packaged using Docker for easy setup.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/nosql-lab.git
   cd nosql-lab
   ```

2. **Run the lab environment** using Docker Compose:
   ```bash
   docker-compose up
   ```

3. **Access MongoDB**:
   - MongoDB will be running locally on port `27017`.
   - You can use **MongoDB Compass** or the **Mongo Shell** to interact with it.
     - Example connection string: `mongodb://localhost:27017/nosql_lab_db`

4. **Run Python Scripts (Optional)**:
   - You can run `lab.py` to perform operations in MongoDB:
     ```bash
     python3 lab.py
     ```

5. **Lab Tasks**:
   - Perform various CRUD operations, query data, and more using MongoDB.
   - Refer to the lab instructions for specific tasks.

## Lab Content

- **Collections**: `Users` and `Orders`.
- **Preloaded Data**:
  - Users: John Doe, Jane Smith, Alice Brown.
  - Orders: Laptops, Phones, Tablets.

---

### **6. Hosting and Distribution**

- **Host the Git repository** on a platform like **GitHub** or **GitLab**.
- Share the link with students, and they can clone the repository and run the lab on their local machines with just Docker installed.

---

### **7. Running the Project**

1. **Students clone the repo**:
   ```bash
   git clone https://github.com/your-username/nosql-lab.git
   cd nosql-lab
   ```

2. **Run Docker Compose**:
   ```bash
   docker compose up
   ```

3. **Access MongoDB**:
   - MongoDB will be available on `localhost:27017`.
   - Students can interact with MongoDB using **MongoDB Compass**, **Mongo Shell**, or **Python**.

---
