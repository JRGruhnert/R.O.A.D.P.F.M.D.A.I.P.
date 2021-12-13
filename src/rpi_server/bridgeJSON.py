import re
from typing import NamedTuple

import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient

import json


ADDRESS = '192.168.0.152'

INFLUXDB_USER = 'influxdb_user'
INFLUXDB_PASSWORD = 'influxdb_password'
INFLUXDB_DATABASE = 'sensor_stations'

MQTT_USER = 'mqtt_user'
MQTT_PASSWORD = 'mqtt_password'
MQTT_TOPIC = 'home/+'
MQTT_CLIENT_ID = 'mqtt_client_id'

influxdb_client = InfluxDBClient(ADDRESS, 8086, INFLUXDB_USER, INFLUXDB_PASSWORD, None)

def on_connect(client, userdata, flags, rc):
    client.subscribe(MQTT_TOPIC)
    print('Connected')

def on_message(client, userdata, msg):
    data = msg.payload.decode('utf8').replace("'", '"')
    pyData = json.load(data)

    if pyData is not None:
        influxdb_client.write_points(pyData)

def _init_influxdb_database():
    databases = influxdb_client.get_list_database()
    if len(list(filter(lambda x: x['name'] == INFLUXDB_DATABASE, databases))) == 0:
        influxdb_client.create_database(INFLUXDB_DATABASE)
    influxdb_client.switch_database(INFLUXDB_DATABASE)

def main():
    _init_influxdb_database()

    mqtt_client = mqtt.Client(MQTT_CLIENT_ID)
    mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    mqtt_client.connect(ADDRESS, 1883)
    mqtt_client.loop_forever()


if __name__ == '__main__':
    print('bridge running...')
    main()