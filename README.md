## What is JsonDBB ?

This is a simple flat file database which stores its data in a JSON file.
It is NOT INTENTED TO USE IN PRODUCTION.
It can be used times when you are too lazy to write a schema and do other stuff for a ORM like SQLAlchemy.

Data is structured as follows:
    Collections
    ---- records
    ---- ---- key value pair ( key: str, value: dictionary )

### What can it Do ?

It can do all the basic things that a database can do, which includes:
    1. creating records
    2. reading records
    3. updating records
    4. deleting records

### Why was it made ?

Sometimes I am to lazy to setup database make database models and all that stuff, and I like key-value pair databases for small fun projects. So I could not find in python so I decided to make one for myself.

### Usage

To use this database you can import it as follows,

```python
from JsonDBB import DB
db = DB("db.json")
```
Above we have imported `DB` Object from `JsonDBB` and then inatalized it by passing the name of the file in which we want to store data.

#### Adding new record

To add new record we use `newrecord`.It creates new reocrds in a given collection. It also creates collection if it doesnt exists.

Inputs: ( collection: str, record: dictionary)
Returns: ( record: dictionary )

```python

from main import DB

db = DB("db.json")
my_data = {
    "name": "Jhon Doe",
    "email": "jhon@example.com",
}
collection = "users"

record = db.newrecord(collection, my_data)
print(record)

# {'04a4e6b1-050e-4b5c-ad30-b75c8de7fc2f': {'name': 'Jhon Doe', 'email': 'jhon@example.com'}}

```

#### Reading a Record

To read a record we use `readrecord`. It finds and returns the record in given collections if it exists, otherwise it raises error "Record not found".

Inputs: ( collection: str, record_key: str )
Returns: ( record: dictionary )

```python

from main import DB

db = DB("db.json")

collection = "users"
record_key = "04a4e6b1-050e-4b5c-ad30-b75c8de7fc2f"

record = db.readrecord(collection, record_key)
print(record)

# {'name': 'Jhon Doe', 'email': 'jhon@example.com'}

```

#### Deleting a Record

To delete a record we use `deleterecord`. It finds and deletes the record if it exists, otherwise it raises error "Record not found".

Inputs: ( collection: str, record_key: str )
Returns: Notinh

```python

from main import DB

db = DB("db.json")

collection = "users"
record_key = "04a4e6b1-050e-4b5c-ad30-b75c8de7fc2f"

db.deleterecord(collection, record_key)

```

#### Adding a key to a record.

To delete a record we use `addkey`. It finds and add the record if it doesn't exists, otherwise if it exists it overwrites it.
Inputs: ( collection: str, record_key: str, keyvalpair: str )
Returns: ( record: dictionary )

```python

from main import DB

db = DB("db.json")

collection = "users"
record_key = "04a4e6b1-050e-4b5c-ad30-b75c8de7fc2f"
keys_to_add = [
    {
        "key": "Value"
    },
    {
        "packages_used": ["uuid", "json"]
    },
    {
        "key1": {
            "a": "big",
            "json": "object"
        }
    }

]

for key_value_pair in keys_to_add:
    record = db.addkey(collection, record_key, key_value_pair)

```


#### Removing a key from a record.

To delete a record we use `removekey`. It finds and deletes the key in the record if it exists, otherwise it raises error "Record not found".
Inputs: ( collection: str, record_key: str, keytoremove: str )
Returns: Nothing

```python

from main import DB

db = DB("db.json")

collection = "users"
record_key = "04a4e6b1-050e-4b5c-ad30-b75c8de7fc2f"
key_to_remove = "packages_used"
db.addkey(collection, record_key, key_to_remove)

```

### Future Plans ( Todos )

[] Make it multifile.
[] Introduce Indexing.

And lets see what comes next. 

Hope you guys like it.😊
