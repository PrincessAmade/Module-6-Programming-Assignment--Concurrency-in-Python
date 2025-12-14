import multiprocessing
import os
import time
import random
from datetime import datetime

def whoami(message):
    print("Process %s says: %s" % (os.getpid(), message))

def worker(proc_id):
    # sleep a random time between 0 and 1 second
    delay = random.uniform(0, 1)
    time.sleep(delay)

    # get the current time as string
    now = datetime.now().strftime("%H:%M:%S.%f")

    # print the result (no f-strings)
    print("Process %s finished after %.4f seconds at %s" % (os.getpid(), delay, now))


# you must save as main.py for multiprocessing on Windows
if __name__ == "__main__":
    whoami("This is the main process of the program")

    # create 3 processes
    for i in range(3):
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()
