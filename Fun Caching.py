import time
from functools import lru_cache

size = int(input("Enter the size of caching"))

@lru_cache(maxsize=size)
def some():
    time.sleep(3)

print("Start")
some()
print("Done Start")
some()
print("done Again start")