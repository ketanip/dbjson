import json, os, shutil
from .config import *

class FiloError(Exception):
    pass

class fileIO():
    """
    This class was made to remove repetative tasks.
    """
    def __init__(self) -> None:
        pass

    def write(self, filename: str, data: str) -> None:
        """
        This function writes data to a given file. 
        """
        data_file = open(filename, "wt")
        data_file.write(data)
        data_file.close()
    
    def read(self, filename: str) -> str:
        """
        This function reads data from a given file
        """
        data_file = open(filename, "rt")
        data = data_file.read()
        data_file.close()
        return data
    
    def deleteDir(self, filename: str):
        """
        This function removes a directory with all the data in it.
        """
        shutil.rmtree(filename)

    def writeJson(self, filename: str, data: dict) -> None:
        """
        This is a helper function that converts given dictionary to raw text and then writes to a file.
        """
        data = json.dumps(data)
        self.write(filename, data)
    
    def readJson(self, filename: str) -> dict:
        """
        This function reads a file and retuns the data in a form of a dictionary.
        """
        data = self.read(filename)
        data = json.loads(data)
        return data

    def getOrMakeDir(self, filename:str, filetype:str="collection") -> None:
        """
        This function gets or makes the directory, and also has some other features.
        """
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
        """
        Used to change dir to DATA DIR.
        """
        os.chdir(data_dir)
    
    def getDir(self, filename: str) -> None:
        """
        It tries to get the directory if it exists or throws a error.
        """
        try:
            os.chdir(filename)
        except Exception:
            raise FiloError(f"{filename} Record Or Collection Does Not Exists.")

