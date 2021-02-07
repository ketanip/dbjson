import json, datetime
from uuid import uuid4
from .helpers import *


class DB:

    """
    This is a simple flat file database which stores its data in a JSON file.
    It is NOT INTENTED TO USE IN PRODUCTION.
    It can be used times when you are too lazy to write a schema and do other stuff for a ORM like SQLAlchemy.

    Data is structured as follows:
        Collections
        ---- records
        ---- ---- key value pair ( key: str, value: dictionary )

    """

    def __init__(self, db_file) -> None:
        self.db_file = db_file

        try:
            db = open(db_file, "rt")

        except Exception:
            db = open(db_file, "wt")
            db.write("{}")
            db.close()

        db_data = db.read()

        if not db_data:
            db_data = "{}"

        db_data = json.loads(db_data)

        if "collections" in db_data.keys():
            pass
        else:
            db_data.update({"collections": {}})
            db_data = json.dumps(db_data)

            db = open(db_file, "wt")
            db.write(db_data)
            db.close()

    def newrecord(self, collection: str, record: dict):

        """
        function: newrecord
        inputs: ( collection: str, record: dictionary)
        usage: It creates new reocrds in a given collection. It also creates collection if it doesnt exists.
        returns: ( record: dictionary )
        """

        db_data = openDB(self.db_file)

        db_data, record = getOrMakeRecord(db_data, collection, record)

        closeDB(self.db_file, db_data)

        return record

    def readrecord(self, collection: str, record_key: str):
        
        """
        function: readrecord
        inputs: ( collection: str, record_key: str )
        usage: It finds and returns the record in given collections if it exists, otherwise it raises error "Record not found".
        returns: ( record: dictionary )
        """

        try:
            db_data = openDB(self.db_file)

            data    = db_data["collections"]
            record  = data[collection][record_key]
            return record

        except Exception as err:
            raise keyError("Record not found.")

    def deleterecord(self, collection: str, recordkey: str):
                
        """
        function: deleterecord
        inputs: ( collection: str, record_key: str )
        usage: It finds and deletes the record if it exists, otherwise it raises error "Record not found".
        returns: Nothing
        """

        try:
            db_data = openDB(self.db_file)

            data    = db_data["collections"]
            data[collection].pop(recordkey)

            closeDB(self.db_file, db_data)

        except Exception as err:
            raise keyError("Record not found.")  

    def addkey(self, collection: str, record_key: str, keyvalpair: dict):
                        
        """
        function: addkey
        inputs: ( collection: str, record_key: str, keyvalpair: str )
        usage: It finds and add the record if it doesn't exists, otherwise if it exists it overwrites it.
        returns: ( record: dictionary )
        """

        db_data = openDB(self.db_file)

        db_data, record = addkeytorecord(db_data, collection, record_key, keyvalpair)
        
        closeDB(self.db_file, db_data)

        return record

    def removekey(self, collection: str, record_key: str, keytoremve: str):
                        
        """
        function: deleterecord
        inputs: ( collection: str, record_key: str, keytoremove: str )
        usage: It finds and deletes the key in the record if it exists, otherwise it raises error "Record not found".
        returns: Nothing
        """

        try:
            db_data = openDB(self.db_file)
            data    = db_data["collections"]

            try:
                data[collection][record_key].pop(keytoremve)
            except Exception:
                raise keyError("Key not found.")

            closeDB(self.db_file, db_data)

        except Exception as err:
            raise keyError("Record not found.")