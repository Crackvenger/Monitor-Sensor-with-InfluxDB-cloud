from test import i2c, sensor, light
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "K1pT_r55WNYSh40huDEJO86_82H5EAGHoJDZlLMen42kFREgawbl8j-YSBoY-gMbLGM11uaWJYztsHKt5c3qkw=="
org = "NusaMeta IoT"
host = "https://us-east-1-1.aws.cloud2.influxdata.com"

client = influxdb_client.InfluxDBClient(url=host, token=token, org=org)

bucket = "temperature, humidity & light"

write_api = client.write_api(write_options=SYNCHRONOUS)

while True:
    h = sensor.relative_humidity
    t = sensor.temperature
    l = light.lux
    
    print(f"humidity: {h:.2f}, temperature: {t:.2f}, light: {l}")
    point = (
        Point("humidity")
        .tag("tagname1", "tagvalue1")
        .field("field1", h)
    )

    write_api.write(bucket=bucket, org="NusaMeta IoT", record=point)
    time.sleep(5) # separate points by 5 seconds