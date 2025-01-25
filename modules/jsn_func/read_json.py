import json 
from os.path import abspath, join

def read_json(filename: str):
    file_path = abspath(join(__file__, '..',  '..', '..', "static", f"{filename}"))
    with open(file_path, 'r') as file:
        return json.load(file)