def countdown(i):
    print(i)
    if i <= 0:
        return 0
    else:
        countdown(i - 1)


# countdown(5)

def greet2(name):
    print("How are you, ", name, "?")


def bye():
    print("Ok bye!")


def greet(name):
    print("Hello, ", name, "?")
    greet2(name)
    print("Getting ready to say bye")
    bye()


# greet("Ivan")

def fact(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * fact(x - 1)


# print(fact(5))

def binary_search(arr, target):
    if not arr:
        return -1
    if len(arr) == 1 and arr[0] == target:
        return arr[0]
    if len(arr) == 1 and arr[0] != target:
        return -1
    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2
    if arr[mid] > target:
        return binary_search(arr[:mid], target)
    else:
        return binary_search(arr[mid + 1:], target)


# print(binary_search([1, 3, 6, 9, 11, 14, 17, 23, 29], 1))


def find_max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = find_max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


# print(find_max([2, 4, 800, 8]))


def sum_array(arr):
    if not arr:
        return 0
    return arr[0] + sum_array(arr[1:])


print(sum_array([1, 2, 3, 4, 5]))
