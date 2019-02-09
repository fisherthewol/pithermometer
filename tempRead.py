import os
import time


def getSensors():
    """Return all connected OneWire devices."""
    return [d for d in os.listdir("/sys/bus/w1/devices/") if "28" in d[0:2]]


def readRawTemp(sensor):
    """Get raw value for temperature (spec: °C*1000)."""
    with open("/sys/bus/w1/devices/{}/w1_slave".format(sensor), "r") as f:
        data = f.readlines()
    return data


def getTemp(sensor):
    """Check CRC and convert to °C."""
    data = readRawTemp(sensor)
    while data[0].strip()[-3:] != "YES":
        time.sleep(0.1)
        data = readRawTemp(sensor)
    (discard, sep, reading) = data[1].partition(" t=")
    return float(reading) / 1000


def main():
    sensors = getSensors()
    while True:
        for index, sensor in enumerate(sensors):
            print(str(index), str(getTemp(sensor)))
        time.sleep(1)


if __name__ == "__main__":
    main()
