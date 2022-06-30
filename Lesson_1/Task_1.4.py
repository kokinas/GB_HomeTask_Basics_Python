#Home task Basics python
###Lesson #1
# Task #1.4 max digit

print('Task #1.4 max digit')
numb = int(input('type a number I will show max digit: '))
max_numb = 0
while numb:
	if max_numb < (numb % 10):
		max_numb = numb % 10
	numb = numb // 10
print(f'max digit is {max_numb}')
