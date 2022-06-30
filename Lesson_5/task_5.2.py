with open('for_task_5.1-5.2.txt', 'r') as logs:
    num_words = 0
    lines = logs.readlines()
    for line in lines:
        num_words += len(line.split())
    print(f'number of line is {len(lines)}, number of words {num_words}')
