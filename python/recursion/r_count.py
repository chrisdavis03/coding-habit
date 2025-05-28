def count(arr):
    if len(arr) == 0:
        return 0
    else:
        arr.pop(0)
        return 1 + count(arr)


if __name__ == "__main__":
    arr = [2, 5, 3, 6, 3]
    arr = [2, 5, 3, 6, 3, 345, 6, 3, 6, 7, 2, 7, 2, 345, 12, 567]
    print(count(arr))
