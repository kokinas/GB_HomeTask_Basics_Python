# Task #3.4.1 exponentiation
def exp1(x, y):
    """
    #return x exponent negative y

    (number, number) -> number

    exp(4, -4)
    256
    """

    if y < 0:
        y = (-1) * y
    else:
        return "'y' must be positive number"
    return (x ** y)


print(exp1(4, -4))


# Task #3.4.2 exponentiation
def exp2(x, y):
    """
    #return x exponent negative y

    (number, number) -> number

    exp(4, -4)
    256
    """

    result = x
    if y < 0:
        y = (-1) * y
    else:
        return "'y' must be positive number"
    for i in range(y - 1):
        result = result * x
    return result


print(exp2(4, -4))
