with open('for_task_5.1-5.2.txt', 'w') as logs:
	while True:
		new_line = input('Enter new line, enter empty line to quit: ')
		if new_line:
			logs.write(new_line + '\n')
		else:
			break
