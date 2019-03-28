import os
import requests
import models
from tempRead import getSensors


baseurl = os.getenv("api_url")


def main():
    while True:
        sensors = getSensors()
        for sensor in sensors:
            requests.post(baseurl + "/sensors")


if __name__ == "__main__":
    pass
