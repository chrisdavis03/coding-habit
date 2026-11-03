#---Top K Elements---# 
# Use a min-heap of size k to track the k largest/smallest elements.  
# The heap keeps candidates and discards elements that fall out of the top k. 

#---Signals---#
# - Find top k, k largest, k smallest, k most frequent
# - "k closest points"
# - Sorting all elements is too expensive

#-- Time: O(n log k), Space: O(k)


import heapq as hq

def top_k_pattern(arr: list[int], k: int) -> list[int]:
    #min heap of size k
    m = []

    for i in range(len(arr)):
        hq.heappush(m, arr[i])
        if len(m) > k:
            hq.heappop(m)

    return m


if __name__ == '__main__':
    print('farts')
    input = [4, 5, 98, 3, 99, 5, 100, 8, 2, 7 ]
    
    print (top_k_pattern(arr=input, k=4))
