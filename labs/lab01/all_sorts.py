# Here are popular sorts, other info and some other sorting algorithms you can find in google

# 1. Selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_ind = i
        for j in range(i + 1, len(arr)):
            if arr[min_ind] > arr[j]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    print("Selection sort. Sorted list:", arr)


selection_sort([5, 3, 2, 6, 9, 15, 12])


# 2. Insertion sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        elem = arr[i]
        j = i
        while j >= 1 and arr[j - 1] > elem:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = elem
    print("Insertion sort. Sorted list:", arr)


insertion_sort([5, 3, 2, 6, 9, 15, 12])


# 3. Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("Bubble sort. Sorted list:", arr)


bubble_sort([5, 3, 2, 6, 9, 15, 12])


# 4. Binary insertion sort (first we need to use binary search and then use insertion sort)
# iterative implementation
def binary_search(arr, item, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if item == arr[mid]:
            return mid + 1
        elif item > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return low


def binary_insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        j = i - 1
        selected = arr[i]
        location_of_selected = binary_search(arr, selected, 0, j)
        while j >= location_of_selected:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = selected
    print("Binary insertion sort. Sorted list:", arr)


binary_insertion_sort([5, 3, 2, 6, 9, 15, 12])


# 5. Merge sort
def merge_sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    if n > 1:
        mid = n // 2
        left_part = merge_sort(arr[:mid])
        right_part = merge_sort(arr[mid:])
        return merge(left_part, right_part)


def merge(left, right):
    i = j = 0
    output = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])
    return output


def run_merge_sort():
    unsorted_list = [5, 3, 2, 6, 9, 15, 12]
    sorted_list = merge_sort(unsorted_list)
    print("Merge sort. Sorted list:", sorted_list)


run_merge_sort()


# 6. Quick sort
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


print("Quick sort. Sorted list:", quick_sort([10, 5, 2, 3, 6, 7, 24, 18]))


# 7. Gnome sort
def gnome_sort(arr):
    n = len(arr)
    i = 0
    while i < n:
        if i == 0:
            i += 1
        if arr[i] >= arr[i - 1]:
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    print("Gnome sort. Sorted list:", arr)


gnome_sort([10, 5, 2, 3, 6, 7, 24, 18])


# 8. Cocktail Shaker sort
def cocktail_shaker_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1

    print("Cocktail shaker sort. Sorted list:", arr)


cocktail_shaker_sort([10, 5, 2, 3, 6, 7, 24, 18])


# 9. Comb sort (looks like bubble sort but we can compare elements which a on distance more than 1)
def comb_sort(arr):
    n = len(arr)
    swapped = True
    while n > 1 or swapped:
        n = max(1, int(n / 1.25))
        swapped = False
        for i in range(len(arr) - n):
            if arr[i] > arr[i + n]:
                arr[i], arr[i + n] = arr[i + n], arr[i]
                swapped = True
    print("Comb sort. Sorted list: ", arr)


comb_sort([10, 5, 2, 3, 6, 7, 24, 18])


# 10. Shell sort
def shell_sort(arr):
    # start with a big gap
    n = len(arr)
    gap = n // 2
    """
    do a gapped insertion sort for this gap size. el arr[0...gap-1] are already in gapped. 
    Order keep adding 1 more el until the entire arr is gap sorted"""
    while gap > 0:
        for i in range(gap, n):
            # add arr[i] to gap sorted,
            # save arr[i] in temo and make a hole pos i
            temp = arr[i]
            # shift earlier gap-sorted el up until the correct loc for arr[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                # put temp(arr[i] orig in its correct location
            arr[j] = temp
        gap //= 2
    print("Shell sort. Sorted list: ", arr)


shell_sort([10, 5, 2, 3, 6, 7, 24, 18])


# 11. Heap sort
# heapify subtree rooted at ind i, n - size of heap
def heapify(arr, n, i):
    # Find largest
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    # Swap if root isn't largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)
    # Build max heap
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        # Swap and heapify root el
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    print("Heap sort. Sorted list:", arr)


heap_sort([10, 5, 2, 3, 6, 7, 24, 18])
