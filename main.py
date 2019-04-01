import multiprocessing
import tempRead
import display
import restclient
import time


if __name__ == "__main__":
    jobs = []
    p1 = multiprocessing.Process(target=tempRead.main)
    jobs.append(p1)
    p2 = multiprocessing.Process(target=display.main)
    jobs.append(p2)
    p3 = multiprocessing.Process(target=restclient.main)
    jobs.append(p3)
    for job in jobs:
        job.start()
        time.sleep(4)
