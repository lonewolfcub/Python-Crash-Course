filename = 'reasons_i_love_programming.txt'

prompt = "Please enter a reason you love programming!"
prompt += "\n(Enter 'quit' to end the program): "

with open(filename, 'a') as file_object:
    active = True
    while active:
        reason = input(prompt)
        if reason == 'quit':
            active = False
        else:
            file_object.write(reason + "\n")