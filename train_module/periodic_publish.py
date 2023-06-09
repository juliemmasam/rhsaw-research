# This module is written for periodic check and publishing of the data
# present in the cache

import publish_data
import json
import time

from dotenv import load_dotenv
import os

load_dotenv()

CACHE_FILE = os.getenv("CACHE_FILE")

def open_cache():
    file = open(CACHE_FILE)
    cache = json.load(file)
    file.close()

    print(cache)
    if "cache" in cache:
        return cache
    else:
        return "Corrupted File"
    

def update_records_to_cache(unpublished_records):
    with open(CACHE_FILE, "w") as file:
        json.dump(unpublished_records, file)
        file.close()
    return
    

def cache_is_empty():
    cache = open_cache()
    if(cache != "Corrupted File"):
        return len(cache["cache"]) == 0
    else:
        return True # Later options to log the details of corrupt cache file


def publish_cache_records():
    if(cache_is_empty()):
         return
    else:
        cache = open_cache()
        
        for index in range(len(cache["cache"])-1, -1, -1):
            record = cache["cache"].pop(index) # Get the latest record
            update_records_to_cache(cache)
            is_published = publish_data.publish_data(record) # Publish the latest records first (LIFO)
            if(not is_published):
                break # Break the loop when the data can't be published
        return 
    

while True:
    publish_cache_records()
    time.sleep(120) #sleep for two minutes

