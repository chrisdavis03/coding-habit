import random
import heapq as hq
import statistics as stats
from time import sleep
import os

#lock randomness for reproducble testing. 
random.seed(1)

data = []
max_heap = []
min_heap = []

def insert(val):
    if max_heap and val > max_heap[0]:   # val belongs to large half
        hq.heappush(min_heap, val)
    else:
        hq.heappush_max(max_heap, val) 

def rebalance():
    # Rebalance
    if len(max_heap) > len(min_heap) + 1:
        hq.heappush(min_heap, hq.heappop_max(max_heap))
    elif len(min_heap) > len(max_heap):
        hq.heappush_max(max_heap, hq.heappop(min_heap))

def median():
    # Median Lookup
    if len(max_heap) > len(min_heap):
        return max_heap[0]
    else:
        return (max_heap[0] + min_heap[0]) / 2

for i in range(100):
    val = random.randint(0, 1000)
    insert(val)
    rebalance()
    print (f"{max_heap} - {min_heap}")
    print (f"Two Heap Median:\t{median()}")
    print (f"Check Median:\t\t{stats.median(max_heap + min_heap)}")
    sleep(.5)
    os.system('cls' if os.name == 'nt' else 'clear')



