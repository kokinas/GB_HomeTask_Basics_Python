# Task 4.4 without reapeted number
in_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
out_list = [i for i in in_list if in_list.count(i) == 1]
print(out_list)
