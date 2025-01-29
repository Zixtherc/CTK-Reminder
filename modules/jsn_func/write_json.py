import json
from os.path import abspath , join

def write_json(filename : str, obj_dict : object):
    path_to_file = abspath(join(__file__, '..',  '..', '..', "static", f"{filename}"))

    with open(path_to_file, 'w') as file:
        json.dump(
            obj = obj_dict,
            fp = file,
            indent = 4,
            ensure_ascii = False
        ) 