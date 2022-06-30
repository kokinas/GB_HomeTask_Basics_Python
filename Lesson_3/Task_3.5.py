# Task #3.5 sum typed number
def sum():
    """
    return sum typed number, symbol q is quit cycle

    (None) -> number

    >>>sum('7 8 5')
    20
    """
    result = 0
    while (1):
        input_str = input('Type list of number: ')
        for i in input_str.split():
            if i != 'q':
                result = result + int(i)
            else:
                return result
        print(f'sum number: {result}')


print(f'Total sum:{sum()}')
