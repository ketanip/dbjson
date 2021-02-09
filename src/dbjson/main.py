import hashlib
from .fileio import *
from .config import *
from uuid import uuid4
import pydash

filo = fileIO()

class DB:
    """
        This is the parent class of all the entire DB. It contains all the functions in it it which you may need.
        This contains:
        
        1. createCollection
        2. removeCollection
        3. createRecord
        4. removeRecord
        5. readRecord
        6. updateRecord
        
        and some util functions,

        1. makeKey
        2. scanRecords
        3. recordInfo
    """
    def __init__(self) -> None:
        """
            It checks if the data directory exists and if then it changes working directory to it else it creates on and then moves in it.
        """

        filo.getOrMakeDir(data_dir)


    # COLLECTIONS

    def createCollection(self, collection:str) -> None:
        """
            This function can be used to create a collection. It takes "collection" a string as an argument. It checks if it exists and if it doesn't it creates one.
        """
        filo.getOrMakeDir(collection)
        filo.baseReset()

    def removeCollection(self, collection: str) -> None:
        """
            This function can be used to create a collection. It takes "collection" a string as an argument and checks if it exists and if it then it deletes it along with any data in it permenantly.
        """
        filo.deleteDir(collection)
    

    # RECORDS

    def createRecord(self, collection:str, data: dict, **kwargs) -> None:
        """
            This function creates a record in a given collection, and if it exists it overwrites it with the new data supplied.
        """
        key = kwargs.get("key", None)
        if not key:
            key = str(uuid4())

        key = self.makeKey(key)
        filo.getOrMakeDir(collection)
        filo.getOrMakeDir(key, "record")
        filo.writeJson(data_file, data)
       
        filo.baseReset()

        record = self.recordInfo(key, data)
        return record

    def removeRecord(self, collection: str, record: str) -> None:
        """
            This function deletes a record in a given collection if it exists and if it doesn't it throws an error.
        """
        filo.getDir(collection)
        filo.deleteDir(record)

    def readRecord(self, collection:str , record_key:str) -> dict:
        """
            This function reads a record in a given collection, and if it exists it raises a error.
        """
        filo.getDir(collection)
        filo.getDir(record_key)
        record = filo.readJson(data_file)
        record = self.recordInfo(record_key, record)
        filo.baseReset()
        return record

    def updateRecord(self, collection:str , record_key:str, data: list[dict]) -> dict:
        """
            This function updates a record in a given collection, and if it does exists otherwise it creates one and adds data to it.  
        """
        filo.getOrMakeDir(collection)
        filo.getOrMakeDir(record_key, "record")
        record = filo.readJson(data_file)
        
        for updated_data in data:
            record.update(updated_data)

        filo.writeJson(data_file, record)

        return record


    # UTILS

    def makeKey(self, key) -> str:
        """
            This function can be used to generate a MD5 hash. It is used to generate record names if not provided. One can use to recreate the same again ant use it for quering the data.
        """
        key = str(key)
        key = key.encode()
        key = hashlib.md5(key)
        key = key.hexdigest()
        return key

    def scanRecords(self, collection: str, filter:dict,  max_scan:int = 50, limit: int = 10):
        """
            This function is used to scan recods in a given collection with the criteron provided to it.
        """
        filo.getDir(collection)
        collection_dir = os.getcwd()

        if max_scan == 0:
            all_records = os.listdir()
        else:
            all_records = os.listdir()[:max_scan]

        matches_found = 0
        matches_data  = []

        for record in all_records:
            if matches_found < limit or matches_found == 0:
                data = filo.getDir(record)
                data = filo.readJson(data_file)
                result = pydash.predicates.is_match(data, filter)
                data = { "__id__": record, "__data__": data}
                
                if result:
                    matches_found += 1
                    matches_data.append(data)
            else:
                break

            filo.getDir(collection_dir)

        filo.baseReset()        

        return matches_found, matches_data
            
    def recordInfo(self, record_key:str, data:dict):
        """
            Just a function to genrate record info.
        """
        data = { "__id__": record_key, "__data__": data}
        return data