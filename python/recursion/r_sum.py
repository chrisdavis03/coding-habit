def sum(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr.pop(0)
    else:
        return arr.pop(0) + sum(arr)


if __name__ == "__main__":
    arr = [2, 4, 6]
    print(sum(arr))
