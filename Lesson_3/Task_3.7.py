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


# Task #3.7 all words UpperCase
def int_func2(string):
    """
    change the first symbol of every word in sentence to uppercase

    (string) -> string

    int_func("hello, how are you my friend?")
    Hello, how are you my friend?
    """
    result = []
    for word in string.split():
        result.append(int_func(word))
    return " ".join(result)


print(int_func2("hello, how are you my friend?"))
