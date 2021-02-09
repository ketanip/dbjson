import json, os, shutil
from config import *

class FiloError(Exception):
    pass

class fileIO():

    def __init__(self) -> None:
        pass

    def write(self, filename: str, data: str) -> None:
        data_file = open(filename, "wt")
        data_file.write(data)
        data_file.close()
    
    def read(self, filename: str) -> str:
        data_file = open(filename, "rt")
        data = data_file.read()
        data_file.close()
        return data
    
    def deleteDir(self, filename: str):
        shutil.rmtree(filename)

    def writeJson(self, filename: str, data: dict) -> None:
        data = json.dumps(data)
        self.write(filename, data)
    
    def readJson(self, filename: str) -> dict:
        data = self.read(filename)
        data = json.loads(data)
        return data

    def getOrMakeDir(self, filename:str, filetype:str="collection") -> None:
        file_exists = os.path.exists(filename)
        if file_exists:
            os.chdir(filename)
        else:
            os.mkdir(filename)
            os.chdir(filename)
           
            if filetype == "collection":
                pass

            elif filetype == "record":
                data = {}
                self.writeJson(data_file, data)      

    def baseReset(self):
        os.chdir(data_dir)
    
    def getDir(self, filename: str) -> None:
        try:
            os.chdir(filename)
        except Exception:
            raise FiloError(f"{filename} Record Or Collection Does Not Exists.")

