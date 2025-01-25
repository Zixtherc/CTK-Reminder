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




# def write_json(filename:str, object_dict: object) -> dict:

#     path_to_file = abspath(join(__file__, "..", "..", "..", "static", "json", f"{filename}"))

#     with open(path_to_file, "w") as file:
#         json.dump(
#             obj = object_dict,
#             fp = file,
#             indent= 4, 
#             ensure_ascii= False#робимо так щоб окрім англ літер , могли записувати кирилицю
#         )