def recursive_max(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


print(recursive_max([2, 6, 78, 24, 35]))
