import random


def findLargest(arr):
    high = arr[0]
    high_idx = 0
    for i in range(0, len(arr), 1):
        if arr[i] > high:
            high = arr[i]
            high_idx = i
    return high_idx


def findSmallest(arr):
    smallest = arr[0]
    smallest_idx = 0
    for i in range(0, len(arr), 1):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_idx = i
    return smallest_idx


def selectionSort_descending(arr):
    sorted_ascending = []
    for i in range(len(arr)):
        largest_idx = findLargest(arr)
        sorted_ascending.append(arr.pop(largest_idx))
    return sorted_ascending


def selectionSort_ascending(arr):
    sorted_descending = []
    for i in range(len(arr)):
        smallest_idx = findSmallest(arr)
        sorted_descending.append(arr[smallest_idx])
        arr.pop(smallest_idx)
    return sorted_descending


if __name__ == "__main__":
    # build array of random size and value
    arrSize = random.randint(0, 100)
    arr_random = []
    for i in range(0, arrSize, 1):
        arr_random.append(random.randint(0, 500))

    # show the array we created
    print(arr_random)

    # print(selectionSort_ascending(arr_random))
    print(selectionSort_descending(arr_random))
