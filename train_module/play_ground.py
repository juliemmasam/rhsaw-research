import gps
import json
import time
from datetime import datetime
import publish_data

CONFIG_FILE = "/home/train/config/train_info.json"
DATA_FILE = "/home/train/train_data/train_data.json"

# Initialize the gps session
session = gps.gps()
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)


def read_sensor_data():
    '''
    The code written in this part is required to read the location
    and speed data from the sensor that will be chosen for our 
    operations

    In this first version of the code, we have considered the 
    Adafruit Ultimate GPS sensor
    '''

    # Initialize necessary variables
    timestamp = datetime.now()
    report = {"class": None}
    report_has_data = False

    # Initialize the location and speed data
    location = None
    latitude = None
    longitude = None
    speed = None

    try: 
        report = session.next()
        
        print(report)
    except:
        quit()


    if report["class"] == "TPV":
        report_has_data = True
        if hasattr(report, "lat"):
            latitude = report.lat
        
        if hasattr(report, "lon"):
            longitude = report.lon

        if hasattr(report, "speed"):
            speed = report.speed
        
        location = {"latitude": latitude, "longitude": longitude}
    
    else:
        location = {}

    current_loc_speed = {
        "location": location, 
        "speed": speed,
        "timestamp": timestamp.strftime("%m-%d-%y, %H:%M:%S")
        }

    return (report_has_data, current_loc_speed)


def read_data_file(): 
    file = open(DATA_FILE)
    json_data = json.load(file)
    file.close()

    return json_data


def write_loc_speed_data(new_json_data):
    with open(DATA_FILE, "w") as data_file: 
        json.dump(new_json_data, data_file)
        data_file.close()


def load_configuration_data():
    config_file = open(CONFIG_FILE)
    config_json_file = json.load(config_file)
    config_file.close()
    train_id = config_json_file["TRAIN_ID"]

    return train_id


def prepare_request_body(train_data):
    TRAIN_ID = load_configuration_data()

    req_body = {
        "train_id": TRAIN_ID, 
        "data": train_data
    }

    return req_body


while True: 
    (has_data, current_sensor_data) = read_sensor_data()
    if (has_data):
        current_json_data = read_data_file()
        current_json_data["loc_speed"].append(current_sensor_data)
        write_loc_speed_data(current_sensor_data) # Write the data locally
        data_to_publish = prepare_request_body(current_sensor_data)
        data_is_published = publish_data.publish_data(data_to_publish)
        print("Data has been written.")
        time.sleep(1) # Run the program every after one second of sleep
    
    