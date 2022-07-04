# Task #3.2 print user data
def print_user_data(name, surname, birthday, town, email, tele_num):
    """
    make sentense with users data

    (string, string, string, string, string, string, string) -> string

    >>> print_user_data('Ivan', 'Ivanov', '01.01.1990', 'Moscow', 'ivanovII@gmail.com', '+79999879898')

    "Ivan Ivanov 01.01.1990 Moscow ivanovII@gmail.com +79999879898"

    """
    return ('{} {} {} {} {} {}'.format(name, surname, birthday, town, email, tele_num))


print(print_user_data('Ivan', 'Ivanov', '01.01.1990', 'Moscow', 'ivanovII@gmail.com', '+79999879898'))
