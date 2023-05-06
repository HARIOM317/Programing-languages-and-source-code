import time
from functools import lru_cache

@ lru_cache(maxsize=3)
def Some_Work(n):
    # Some tasks taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work...")
    Starting_time1 = time.time()
    Some_Work(4)
    ending_time1 = time.time()
    print("Time taken in execution -->  ", ending_time1 - Starting_time1)

    print("Done! Calling again..")
    Starting_time2 = time.time()
    Some_Work(4)
    ending_time2 = time.time()
    print("Time taken in execution -->  ", ending_time2 - Starting_time2)

    print("Called again! ")
