import json
import time
from datetime import datetime

DATA_FILE = "train_data.json"

def read_sensor_data():
    '''
    The code written in this part is required to read the location
    and speed data from the sensor that will be chosen for our 
    operations
    '''
    location = "latitude, longitude"
    speed = "speed in mph"
    timestamp = datetime.now()

    current_loc_speed = {
        "location": location, 
        "speed": speed,
        "timestamp": timestamp.strftime("%m-%d-%y, %H:%M:%S")
        }

    return current_loc_speed


def read_data_file(): 
    file = open(DATA_FILE)
    json_data = json.load(file)
    file.close()

    return json_data


def write_loc_speed_data(new_json_data):
    with open(DATA_FILE, "w") as data_file: 
        json.dump(new_json_data, data_file)
        data_file.close()


while True: 
    current_sensor_data = read_sensor_data()
    current_json_data = read_data_file()
    current_json_data["loc_speed"].append(current_sensor_data)
    write_loc_speed_data(current_json_data)
    print("Data has been written.")
    time.sleep(30)