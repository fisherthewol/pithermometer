import models
import os
import time


def getSensors():
    """Return all connected OneWire devices."""
    return [d for d in os.listdir("/sys/bus/w1/devices/") if "28" in d[0:2]]


def readRawTemp(sensor):
    """Get raw value for temperature (spec: °C*1000)."""
    try:
        with open("/sys/bus/w1/devices/{}/w1_slave".format(sensor), "r") as f:
            data = f.readlines()
        return data
    except FileNotFoundError:
        return None


def getTemp(sensor):
    """Check CRC and convert to °C."""
    data = readRawTemp(sensor)
    if data:
        x = 100
        while data[0].strip()[-3:] != "YES":
            x -= 1
            if x <= 0:
                return None
            time.sleep(0.1)
            data = readRawTemp(sensor)
        (discard, sep, reading) = data[1].partition(" t=")
        return float(reading) / 1000
    else:
        return None


def saveToDatabase(sens, temp):
    """Save reading to the database."""
    with models.db:
        x = models.Reading(sensor=sens, temperature=temp)
        x.save()


def main():
    while True:
        sensors = getSensors()
        for sensor in sensors:
            temp = getTemp(sensor)
            if temp:
                saveToDatabase(sensor, temp)
        time.sleep(30)


if __name__ == "__main__":
    main()
