# This module is written for periodic check and publishing of the data
# present in the cache

import publish_data
import json
import time

CACHE_FILE = "/home/train/train_data/cache.json"

def open_cache():
    file = open(CACHE_FILE)
    cache = json.load(file)
    file.close()

    if hasattr(cache, "cache"):
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
        print("Corrupted cache file.")
        return len(cache["cache"]) == 0
    else:
        return True # Later options to log the details of corrupt cache file


def publish_cache_records():
    if(cache_is_empty()):
         print("cache is empty")
         return
    else:
        cache = open_cache()
        
        for index in range(len(cache["cache"])-1, -1, -1):
            record = cache["cache"].pop(index) # Get the latest record
            update_records_to_cache(cache)
            is_published = publish_data.publish_data(record) # Publish the latest records first (LIFO)
            if(not is_published):
                print("Data has not been published")
                break # Break the loop when the data can't be published
        return 
    

while True:
    publish_cache_records()
    time.sleep(1200)

