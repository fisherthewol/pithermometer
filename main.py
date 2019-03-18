import multiprocessing
import tempRead
import display
import time


if __name__ == "__main__":
    jobs = []
    p = multiprocessing.Process(target=tempRead.main())
    jobs.append(p)
    p2 = multiprocessing.Process(target=display.main())
    jobs.append(p2)
    for job in jobs:
        job.start()
        time.sleep(4)
