"""
A function that takes a list of numbers as an argument and returns a 
list with the min and max number from the list
"""


def find_max_min(num_list):
    if len(set(num_list)) == 1:
        return [len(num_list)]
    else:
        sorted_num_list = sorted(num_list)
        min_num = sorted_num_list[0]
        max_num = sorted_num_list[-1]
        return [min_num, max_num]
