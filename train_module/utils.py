# This file contains functions for reading from 
# and writing to files, tasks which seem repetitive now
import json

def read_from_file(filepath):
    with open(filepath) as file: 
        file_contents = json.load(file)

    return file_contents


def write_to_file(filepath, file_contents): 
    try:
        with open(filepath, "w") as file: 
            json.dump(file_contents, file)
        return True
    except:
        return False