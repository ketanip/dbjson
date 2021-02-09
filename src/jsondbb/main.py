import hashlib
from fileio import *
from config import *
from uuid import uuid4
import pydash

filo = fileIO()

class DB:

    def __init__(self) -> None:
        filo.getOrMakeDir(data_dir)


    # COLLECTIONS

    def createCollection(self, collection:str) -> None:
        filo.getOrMakeDir(collection)
        filo.baseReset()

    def removeCollection(self, collection: str) -> None:
        filo.deleteDir(collection)
    

    # RECORDS

    def createRecord(self, collection:str, data: dict, **kwargs) -> None:

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
        filo.getOrMakeDir(collection)
        filo.deleteDir(record)

    def readRecord(self, collection:str , record_key:str) -> dict:
        filo.getDir(collection)
        filo.getDir(record_key)
        record = filo.readJson(data_file)
        record = self.recordInfo(record_key, record)
        filo.baseReset()
        return record

    def updateRecord(self, collection:str , record_key:str, data: list[dict]) -> dict:
        filo.getOrMakeDir(collection)
        filo.getOrMakeDir(record_key, "record")
        record = filo.readJson(data_file)
        
        for updated_data in data:
            record.update(updated_data)

        filo.writeJson(data_file, record)

        return record


    # UTILS

    def makeKey(self, key) -> str:
        key = str(key)
        key = key.encode()
        key = hashlib.md5(key)
        key = key.hexdigest()
        return key

    def scanRecords(self, collection: str, filter:dict,  max_scan:int = 50, limit: int = 10):
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
        data = { "__id__": record_key, "__data__": data}
        return data