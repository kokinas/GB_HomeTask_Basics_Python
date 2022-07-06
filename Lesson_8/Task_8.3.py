class OnlyNumb(Exception):
    def __init__(self, txt):
        self.txt = txt


result = []
while True:
    try:
        in_numb = input('type a numb for result list: ')
        if in_numb.isdigit():
            result.append(in_numb)
        elif in_numb == 'q':
            break
        else:
            raise OnlyNumb('Type only numb')
    except OnlyNumb as OnlN:
        print(OnlN)
print(result)
