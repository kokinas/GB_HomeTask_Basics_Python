with open('for_task_5.6.txt', 'r') as schedule:
    output_dict = {}
    for line in schedule:
        sum_hours = 0
        digit_flag = 0
        text_for_numb = ''

        schedule_text = line.split(':')
        subject = schedule_text[0]

        for pos_line in schedule_text[1]:
            if pos_line.isdigit():
                digit_flag = 1
                text_for_numb = text_for_numb + pos_line
            else:
                if digit_flag:
                    sum_hours += int(text_for_numb)
                    digit_flag = 0
                    text_for_numb = ''
        output_dict.update({subject: sum_hours})
print(output_dict)
