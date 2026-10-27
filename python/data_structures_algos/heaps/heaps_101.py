import heapq
import random

random.seed(111)
ints = []

#Create an unsorted list
for i in range(10):
    ints.append(random.randint(1, 50))

max_ints = ints.copy()

#Create a min-heap with heapify
#Converts a regular list into a min-heap in-place.
heapq.heapify(ints)
print (ints)

#Create a max-head with heapify_max
#Converts a regular list into a max-heap in-place
heapq.heapify_max(max_ints)
print (f"max heap: {max_ints}")


#ints[0] is the smallest/largest element
print (ints[0])
print (max_ints[0])

#push a new item onto the heap
heapq.heappush(ints, 78) 
print (ints)
heapq.heappush(ints,12)
print(ints)

#pop the head of the min-heap returning the smallest element. 
smallest = heapq.heappop(ints)
print (smallest, ints)

