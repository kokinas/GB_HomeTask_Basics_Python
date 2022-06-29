#Task #2.6 structer data of goods

data_base = [
(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
(2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
(3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]

#Add new good
max = int(input('type number adding goods: '))
for i in range(1, max + 1):
	name = input(f'Type name of good #{i}: ')
	price = int(input(f'Type price of good #{i}: '))
	numb = int(input(f'Type numb of good #{i}: '))
	unit = input(f'Type unit of good #{i}: ') 
	count = len(data_base)
	data_base.append((len(data_base) + 1, {'название': name, "цена" : price, 'количество' : numb, 'eд' : unit} ))
	print('adding good complete')

#for i in data_base:				
#	print(i)

output_base = {}
keys = data_base[1][1].keys()		# receive all keys
for key in keys:
	buf = []
	for val in data_base:
		buf.append(val[1].get(key))
	output_base.update({key : buf})
print('{')
for i, j in output_base.items():
	print (f'{i} : {j}')
print('}')
