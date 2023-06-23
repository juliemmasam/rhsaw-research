from dotenv import load_dotenv
import os
from urllib import request
import requests

import json

load_dotenv()

API_URL = os.getenv("API_URL")
CACHE_FILE = os.getenv("CACHE_FILE")


def connection_is_present():
    '''
    This function checks if there is a connection to the API
    '''
    try: 
        request.urlopen(API_URL+"2", timeout=2)
        return True
    except:
        return False


def write_to_cache(train_data):
    '''
    This function writes to the local cache if there is no connection
    to the API
    '''
    cache_file = open(CACHE_FILE)
    cache_data = json.load(cache_file)
    cache_file.close()

    with open(CACHE_FILE, "w") as file: 
        cache_data["cache"].append(train_data)
        json.dump(cache_data, file)
        file.close()

        return True
        

def publish_data(train_data):
    '''
    This function contains the data publication logic
    It first checks the connection availability and either publishes 
    or stores the data in cache
    '''
    if connection_is_present():
        train_id = train_data["train_id"]
        requests.post(url=API_URL+str(train_id), json=train_data)
        return True
    else:
        write_to_cache(train_data)
        return False