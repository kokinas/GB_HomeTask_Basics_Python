#Home task Basics python
###Lesson #2
#Task #2.3.1 month season

month = int(input("type numb of month: "))
months = [None, 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
seasons = [None, 'winter', 'winter', 'spring',
		   'spring', 'spring', 'summer', 'summer',
		   'summer', 'autumn', 'autumn', 'autumn',
		    'winter']
print(months[month])
print(seasons[month])



#Task #2.3.2 month season
month =input("type numb of month: ")
seasons = {
	 '1' : 'winter',
	 '2' : 'winter',
	 '3' : 'spring',
	 '4' : 'spring',
	 '5' : 'spring',
	 '6' : 'summer',
	 '7' : 'summer',
	 '8' : 'summer',
	 '9' : 'autumn',
	'10' : 'autumn',
	'11' : 'autumn',
	'12' : 'winter'
}
print(seasons[month])