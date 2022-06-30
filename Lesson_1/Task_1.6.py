# Home task Basics python
###Lesson #1

# Task #1.6 profitability
print('Task #1.6 profitability')

income = int(input('type your income: '))
expenses = int(input('type your expenses: '))
revenue = income - expenses
if revenue > 0:
    print(f"your profitability is {revenue / income}")
staff = int(input('type amount of staff: '))
inc_to_staff = income / staff
print(f"each employee income {inc_to_staff}")
