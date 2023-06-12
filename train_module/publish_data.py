from urllib import request
import requests

import json

API_URL = "143.244.147.111:3000/trains/2" # to be changed
CACHE = "/home/train/train_data/cache.json"


def connection_is_present():
    '''
    This function checks if there is a connection to the API
    '''
    try: 
        request.urlopen(API_URL, timeout=2)
        return True
    except:
        return False


def write_to_cache(train_data):
    '''
    This function writes to the local cache if there is no connection
    to the API
    '''
    with open(CACHE, "w") as file: 
        cache = json.load(file)
        new_cache = cache["cache"].append(train_data)
        json.dump(new_cache, file)

        return True
        

def publish_data(train_data):
    '''
    This function contains the data publication logic
    It first checks the connection availability and either publishes 
    or stores the data in cache
    '''
    if connection_is_present():
        requests.post(url=API_URL, json=train_data)
        return True
    else:
        write_to_cache(train_data)
        return False