#Home task Basics python
###Lesson #2
#Task #2.2 script type

len_list = int(input("type numb elements of list: "))
list_1 = []

for i in range(1, len_list + 1):
	list_1.append(input(f"type element #{i}: "))
print(list_1)

for i in range(1, len_list, 2):
	buf = list_1[i - 1]
	list_1[i - 1] = list_1[i]
	list_1[i] = buf
print(list_1)
