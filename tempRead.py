import time


sensor = "/sys/bus/w1/devices/???/w1_slave"


def readRawTemp():
    """Get raw value for temperature (spec: DEG C *1000)"""
    with open(sensor, "r") as f:
        data = f.readlines()
    return data


def getTemp():
    """Check CRC and convert to DEG C."""
    data = readRawTemp()
    while data[0].strip()[-3:] != "YES":
        time.sleep(0.1)
        data = readRawTemp()
    (discard, sep, reading) = data.partition(" t=")
    return reading / 1000.0
