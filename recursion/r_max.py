def find_max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = find_max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


# todo - revisit this


if __name__ == "__main__":
    arr = [32, 67, 3, 7, 12, 5674]
    print(find_max(arr))
