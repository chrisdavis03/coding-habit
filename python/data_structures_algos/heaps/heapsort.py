import heapq as hq

def heapsort(n:list[int]):
    #initialize heaps
    minheap = n.copy() 
    maxheap = n.copy()

    #heapify / create heap order
    hq.heapify(minheap)
    hq.heapify_max(maxheap)

    #store results
    ascending = []
    descending = []

    for i in range(len(nums)):
        ascending.append(hq.heappop(minheap))
        descending.append(hq.heappop_max(maxheap))

    return {
        "asc": ascending, 
        "desc": descending
    }

if __name__ == '__main__':
    nums = [11, 13, 27, 13, 14, 32, 40, 21, 41, 26, 78]

    print (heapsort(n=nums))