with open('for_task_5.5.txt', 'w') as numb:
    numb.write('2 5 3 9 12')
with open('for_task_5.5.txt', 'r') as numb:
    numb_list = numb.read().split()
    sum_numb = 0
    for numb in numb_list:
        sum_numb += int(numb)
    print(sum_numb)
