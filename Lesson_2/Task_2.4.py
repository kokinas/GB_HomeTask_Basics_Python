#Home task Basics python
###Lesson #2
#Task #2.4 split and handle message

in_str = input('type some message: ')
str_handled = in_str.split()
for i, word in enumerate(str_handled, 1):
	print(i, word[:10])