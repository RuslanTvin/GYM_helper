import json

def load_file_with_progress_json(file_name):
    try:

        with open(file_name,"r") as file:

            return json.load(file)
    except FileNotFoundError:

        dump_file_with_progress_json(file_name,[])
        return []
    
def dump_file_with_progress_json(file_name,what_to_dump):
    with open(file_name,"w") as file:
        json.dump(what_to_dump,file,indent=4)