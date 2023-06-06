def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == "__main__":
    arr = [7, 2, 4, 8, 5, 7, 1, 345]
    print(quicksort(arr))
