# Realization of a data pipeline for machine data acquisition in production
Includes python and arduino files used to visualize sensor data. The collected data gets publised via the MQTT protocol. The server runs bridge.py which subscribes to the MQTT instance. The data gets written to a local InfluxDB database. A Grafana instance is used to visualize the data over time by regulary pulling from the InfluxDB database. The setup of the InfluxDB and Grafana instance is not part of this repo. It is important to give a static ip to the raspberry pi.

## Setup
Used Hardware and Software
### Hardware
- ESP32
- Raspberry Pi
- BME680
- (cables)
### Software / Libraries
- Grafana
- InfluxDB
- Jupiter Notebook
- Mosquitto (MQTT)

## Sequenzdiagramm
![image](/doc/images/UML_Sensor.png)
