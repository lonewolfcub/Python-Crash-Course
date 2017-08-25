filename = 'guest_book.txt'

prompt = "Please enter your name, honoured guest!"
prompt += "\n(Enter 'quit' to end the program): "

with open(filename, 'w') as file_object:
    active = True
    while active:
        guest_name = input(prompt)
        if guest_name == 'quit':
            active = False
        else:
            file_object.write(guest_name + "\n")