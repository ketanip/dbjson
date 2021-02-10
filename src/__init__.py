from dbjson.main import DB

# Instatilizing DB class from dbjson.main
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
# db.removeRecord(collection, record_key)