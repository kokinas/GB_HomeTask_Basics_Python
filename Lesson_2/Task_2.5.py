#Home task Basics python
###Lesson #2

#Task #2.5 rating insert
rating_list = [7, 5, 5, 4, 3, 3, 3, 2]
print(rating_list)
input_numb = int(input('Type a numb to insert to rating list: '))
flag_min = False
for numb in rating_list:
	if numb < input_numb:
		index = rating_list.index(numb)
		rating_list.insert(index, input_numb)
		flag_min = True
		break
if not flag_min:
	rating_list.append(input_numb)
print(rating_list)
