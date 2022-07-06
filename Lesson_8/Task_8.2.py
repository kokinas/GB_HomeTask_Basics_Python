class DelZero(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    x = int(input('type some divider: '))
    try:
        if x != 0:
            x = 10 / x
        else:
            raise DelZero("don't divide by Zero")
    except DelZero as err:
        print(err)
