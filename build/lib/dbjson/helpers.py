import json
from uuid import uuid4

def getOrMakeRecord(data, collection, record):
        
        """
        This is a function to get ( or make if it doesn't exists ) a record in a given collection.
        """
        collections = data['collections']
        db_data = collections
        key = str(uuid4())

        if collection in db_data.keys():
            db_data = db_data[collection]
        else:
            db_data.update({collection: {}})
            db_data = db_data[collection]
        
        db_data.update({key: record})
        record = {
            key: record
        }
        return data, record
        
def addkeytorecord(data, collection, record_key, keyvalpair):

    """
        This is a function to add ( or update ) key value pair in a given record in a given collection.
    """

    collections = data['collections']
    db_data = collections

    if collection in db_data.keys():
        db_data = db_data[collection]
    else:
        db_data.update({collection: {}})
        db_data = db_data[collection]
    
    try:
        db_data[record_key].update(keyvalpair)
    
    except Exception:
        db_data.update({record_key: {}})
        db_data[record_key].update(keyvalpair)

    return data, db_data[record_key]

def openDB(filename):
    db = open(filename, "rt")
    db_data = db.read()
    db.close()
    db_data = json.loads(db_data)
    return db_data
            
def closeDB(filename, data):
    db_data = json.dumps(data)
    db      = open(filename, "wt")
    db.write(db_data)
    db.close()

class keyError(Exception):
    """
    Just a error to raise Exceptions.
    """
    pass
