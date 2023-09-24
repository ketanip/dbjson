
<p align="center" width="100%">
    <img width="33%" src="https://i.imgur.com/gbT5IKBm.jpg">
</p>

# 👨‍💻 Getting Started with DBJson

### Installation

```bash
pip install dbjson
```

### Example 
```python
from dbjson import DB
# Use the syntax below if you plan to include raw code in your project.
# from dbjson.db import DB 

# Initializing DB class from dbjson.main
db = DB()

# Test Data
data = {
  "id": 1,
  "first_name": "Vivyan",
  "last_name": "Treherne",
  "email": "vtreherne0@jigsy.com",
  "ip_address": "94.254.247.240"
}
collection = "users"

# Adding Record
data = db.createRecord(collection, data)
print(data)
# Response -> {'__id__': 'f00ae4e3ca8c3e318a68acc460e5f401', '__data__': {'id': 1, 'first_name': 'Vivyan', 'last_name': 'Treherne', 'email': 'vtreherne0@jigsy.com', 'ip_address': '94.254.247.240'}}

# Updating Record
record_key = "f00ae4e3ca8c3e318a68acc460e5f401"
to_update = [
    {"email": "jhon@email.com"},
    {"ip_address": "google.com"}
]
data = db.updateRecord(collection, "f00ae4e3ca8c3e318a68acc460e5f401", to_update)
print(data)
# Response -> {'id': 1, 'first_name': 'Vivyan', 'last_name': 'Treherne', 'email': 'jhon@email.com', 'ip_address': 'google.com'}

# Deleting Record
db.removeRecord(collection, record_key)
```

---

# 🤔 What is DBJson?

Read the [DBJson docs here](https://ketanip.github.io/dbjson/) .

DBJson is a straightforward flat file database system that securely houses its data within the filesystem, utilizing a combination of folders and JSON files. It is important to emphasize that DBJson is NOT INTENDED FOR PRODUCTION USE. However, it serves as an ideal solution for scenarios in which the creation of a formal schema and the execution of supplementary tasks typically associated with Object-Relational Mapping (ORM) frameworks, such as SQLAlchemy, seem overly laborious or unnecessary.


### Data is structured as follows:

**Collections**: Contains records.
**Records**: Contains key-value pairs.
**Key-Value Pair**: (Key: str, Value: dictionary).

### 🌟 What are its Features?
DBJson facilitates the core operations of Create, Read, Update, and Delete (CRUD) on data, making it a versatile tool for managing information efficiently and effectively.

### 💼 What Can it Do?

It can perform all the basic operations that a database can do, including:

1. Creating records
2. Reading records
3. Updating records
4. Deleting records
5. Filtering records

### 🤷‍♂️ Why Was it Made?

Sometimes, setting up a database, creating database models, and dealing with all that stuff can be a hassle. For small, fun projects, I prefer key-value pair databases. Since I couldn't find one in Python, I decided to create DBJson for myself.

Hope you find it useful. 😊

Read the [DBJson docs here](https://ketanip.github.io/dbjson/) .
