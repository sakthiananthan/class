import json


def read_json():
    with open("data.json") as f:
        return json.load(f)
    
def write_json(data):
    with open("data.json","w") as f:
        json.dump(data,f,indent=3)