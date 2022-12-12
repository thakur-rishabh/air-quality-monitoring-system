#!/usr/bin/env python3
from google.cloud import pubsub_v1
from oauth2client.client import *
import adafruit_scd4x
import board
import time
import datetime
import json


#Constant
time_duration = 10
i2c = board.I2C()
scd4x = adafruit_scd4x.SCD4X(i2c)
project = "class-project-312"
topic = "real_time_co2"
credential = GoogleCredentials.get_application_default()

# initializing sensor to start collecting
scd4x.start_periodic_measurement()

# json event creation
def json_generate(timestamp, co2_data, temperature):
    sensor_events = {
        'timecollected': timestamp,
        'co2_ppm': co2_data,
        'temperature': temperature
    }
    return json.dumps(sensor_events)

# append json event to file
def save_event_to_file(filename, json_event):
    with open(filename, "a") as f:
        f.write(json_event+"\n")

# main function
def main():
    publisher = pubsub_v1.PublisherClient()
    topic_name = 'projects/'+project+'/topics/'+topic
    last_checked = 0
    while True:
        if scd4x.data_ready:
            if time.time() - last_checked > time_duration:
                last_checked = time.time()
                co2 = scd4x.CO2
                temp = scd4x.temperature
                current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                sensor_json = json_generate(current_time, co2, temp)
                filename = time.strftime('%Y-%m-%d') + ".json"
                try:
                    publisher.publish(topic_name, sensor_json.encode("utf-8"), placeholder='')
                    save_event_to_file(filename, sensor_json)
                except Exception as e:
                    print(e)
            time.sleep(1)

if __name__ == '__main__':
    main()
            


