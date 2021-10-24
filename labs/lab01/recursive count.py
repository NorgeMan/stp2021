def recursive_count(my_list):
    if not my_list:
        return 0
    return 1 + recursive_count(my_list[1:])


print(recursive_count([1, 2, 3, 4, 5, 6, 7]))
