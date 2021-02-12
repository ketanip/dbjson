import os

"""
Just a simple config file.
"""


base_dir = os.getcwd()
data_temp = "__temp__.json"
data_file = "__data__.json"
config_data = "__config__.json"
data_dir  = os.path.join(base_dir, "__data__")
collections_dir  = os.path.join(data_dir, "__collections__")