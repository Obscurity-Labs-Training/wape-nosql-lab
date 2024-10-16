# NoSQL Lab - MongoDB

This lab provides hands-on experience with MongoDB, where you'll work with CRUD operations, querying, and data relationships using flat collections. The lab is packaged using Docker for easy setup.

## Setup Instructions

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Obscurity-Labs-Training/wape-nosql-lab.git
   cd nosql-lab
   poetry install --no-root
   poetry  shell
   ```
   

2. **Run the lab environment** using Docker Compose:
   ```bash
   docker compose up -d
   ```

3. **MongoDB**:
   - MongoDB will be running locally on port `27017`.

4. **Run Python Scripts**:
   - Inspect each script prior to running it.
   - You can run `lab.py` to perform operations in MongoDB:
     ```bash
     python load_data.py
     python lab.py
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


