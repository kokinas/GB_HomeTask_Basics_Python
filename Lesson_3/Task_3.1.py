# Home task Basics python
###Lesson #3 FUNCTION

# Task #3.1 divide function
def divide(divident, divisor):
    """
    first number divid by second

    (number, number) -> number

    >>> divide(99, 11)
    9
    """
    try:
        return divident / divisor
    except:
        return "cannot be divided by zero"

print(divide(10, 2))
print(divide(10, 0))
print("that's all")
