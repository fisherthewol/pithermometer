import os
import time


def getSensors():
    """Return all connected onewire sensors."""
    return [dev for dev in os.listdir("/sys/bus/w1/devices/") if "28" in dev[0:2]]


def readRawTemp(sensor):
    """Get raw value for temperature (spec: DEG C *1000)"""
    with open("/sys/bus/w1/devices/{}/w1_slave".format(sensor), "r") as f:
        data = f.readlines()
    return data


def getTemp(sensor):
    """Check CRC and convert to DEG C."""
    data = readRawTemp(sensor)
    while data[0].strip()[-3:] != "YES":
        time.sleep(0.1)
        data = readRawTemp(sensor)
    (discard, sep, reading) = data[1].partition(" t=")
    return reading / 1000


def main():
    sensors = getSensors()
    while True:
        for sensor in sensors:
            print(str(getTemp(sensor)))
        time.sleep(1)


if __name__ == "__main__":
    main()
