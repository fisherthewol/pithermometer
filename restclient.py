import os
import requests
import json
# import models
from tempRead import getSensors


baseurl = os.getenv("api_url")


def main():
    while True:
        currentsensors = getSensors()
        for sensor in currentsensors:
            d = {"serial": sensor, "name": os.secrets.token_urlsafe, "connected": True}
            r = requests.post(baseurl + "/sensors", data=json.dumps(d))
            if r.status_code == 409:
                r1 = requests.put(baseurl + "/sensors", data=json.dumps(d))
                if r.status_code != 200:
                    raise SystemExit("SOmething is wrong.")


if __name__ == "__main__":
    pass
