# Task #3.6 first word UpperCase
def int_func(string):
    """
    change the first symbol of sentence to uppercase

    (string) -> string

    int_func("hello, how are you my friend?")
    Hello, how are you my friend?
    """
    if string.istitle:
        return string.capitalize()
    else:
        return "input sentens has upper case"


print(int_func("hello, how are you my friend?"))
