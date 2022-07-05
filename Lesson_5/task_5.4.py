num_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
with open('for_task_5.4_ENG.txt', 'r') as buf_input:
    for line in buf_input:
        eng_numb = line.split(' — ')[0]
        new_line = line.replace(eng_numb, num_dict.get(eng_numb))
        with open('for_task_5.4_RUS.txt', 'a') as buf_output:
            buf_output.write(new_line)
