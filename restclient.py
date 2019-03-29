import os
import requests
import json
import models
from tempRead import getSensors


baseurl = os.getenv("api_url")


def dispatchSensor(sensor):
    d = {"serial": sensor.serial,
         "name": sensor.name,
         "connected": sensor.connected}
    r = requests.post(baseurl + "/sensors", data=json.dumps(d))
    if r.status_code == 409:
        r1 = requests.get(baseurl + "/sensors")
        j = r1.json()
        for i in j:
            if i["serial"] == sensor.serial:
                x = i["id"]
        r2 = requests.put(baseurl + "/sensors/" + x, data=json.dumps(d))
        if r2.status_code != 200:
            raise SystemExit("Something is wrong.")
    return "Success"


def dispatchReadings(sensor):
    q = models.Reading.select().where(models.Reading.sensor == sensor).order_by(models.Reading.timestamp.desc())
    d = {"sensor": q[0].serial, "timestamp": q[0].timestamp, "temperature": q[0].temperature}
    r = requests.post(baseurl + "/readings", data=json.dumps(d))
    if r.status_code != 200:
        raise SystemExit("Something is wrong.")


def main():
    while True:
        connectedsensors = []
        for sensor in getSensors():
            x = models.Sensor.get_or_create(serial=sensor,
                                            defaults={"name": os.secrets.token_urlsafe,
                                                      "connected": True})
            connectedsensors.append(x)
        for sensor in models.Sensor.select():
            if sensor not in connectedsensors:
                sensor.connected = False
        for sensor in models.Sensor.select().where(models.Sensor.connected == True):
            dispatchSensor(sensor)
            dispatchReadings(sensor)


if __name__ == "__main__":
    pass
