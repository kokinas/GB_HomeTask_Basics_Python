output_dict = {}
count = 0
sum_revenue = 0
with open('for_task_5.7.txt', 'r') as f_obj:
    for line in f_obj:
        buf = line.split()
        firm = buf[0]
        ownership = buf[1]
        income = int(buf[2])
        expanse = int(buf[3])
        revenue = income - expanse
        if revenue > 0:
            count += 1
            sum_revenue += revenue
        output_dict.update({firm: revenue})
print([output_dict, {'average_profit': sum_revenue / count}])
