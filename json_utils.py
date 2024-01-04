import json


def json_read(file):
    f=open(file)
    data=json.load(f)
    f.close()
    return data

def json_write(file,data):
    f=open(file,"w")
    data_to_be_written=json.dumps(data,indent=3)
    f.write(data_to_be_written)
    f.close()
