import os
import requests
import models
from tempRead import getSensors


baseurl = os.getenv("api_url")


def checkequal(l1, l2):
    return len(L1) == len(L2) and sorted(L1) == sorted(L2)



def main():
    knownsensors = []
    while True:
        sensors = getSensors()
        if checkequal(knownsensors, sensors):
            pass
        for sensor in knownsensors:
                d = {"serial": sensor, "name": os.secrets.token_urlsafe, "connected": true}
                r = requests.post(baseurl + "/sensors", data=d)


if __name__ == "__main__":
    pass
