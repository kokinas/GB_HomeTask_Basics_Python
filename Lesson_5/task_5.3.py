with open('for_task_5.3.txt', 'r') as wages:
    sum_wage = 0
    numb_employee = 0
    for line in wages:
        numb_employee += 1
        employee = line.split()
        name = employee[0]
        wage = float(employee[1])
        if wage < 20000:
            print(name)
        sum_wage += wage

print('average wage is %.2f' % (sum_wage / numb_employee))
