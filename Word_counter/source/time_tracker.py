import time
import datetime


def get_time():
    t = datetime.datetime.now()
    t = str(t)
    t = t.split(" ")
    time = []
    for x in t:
        print(x)
        x = x.split(":")
        time.append(x)
    return(time)


get_time()