# Task #3.3 sum two maximum

def sum_max(numb1, numb2, numb3):
    """
    return sum of two maximum number

    (number, number, number) -> number

    >>> sum_max(3, 8, 4)
    12
    """
    list1 = [numb1, numb2, numb3]
    list1.remove(min(list1))
    return sum(list1)


print(sum_max(3, 8, 3))
