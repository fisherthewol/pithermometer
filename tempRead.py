import os
import time
from typing import List


def getSensors() -> List[str]:
    return [dev for dev in os.list("/sys/bus/w1/devices/") if "28" in dev[0:2]]


def readRawTemp(sensor: str) -> List[str]:
    """Get raw value for temperature (spec: DEG C *1000)"""
    with open(f"/sys/bus/w1/devices/{sensor}/w1_slave", "r") as f:
        data = f.readlines()
    return data


def getTemp(sensor: str) -> float:
    """Check CRC and convert to DEG C."""
    data = readRawTemp(sensor)
    while data[0].strip()[-3:] != "YES":
        time.sleep(0.1)
        data = readRawTemp(sensor)
    (discard, sep, reading) = data.partition(" t=")
    return reading / 1000.0
