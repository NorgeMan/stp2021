def recursive_sum(my_list):
    if my_list == []:
        return 0
    return my_list[0] + sum(my_list[1:])


print(recursive_sum([1, 2, 3, 4, 5, 6]))
