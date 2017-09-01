filename = 'guest.txt'

with open(filename, 'w') as file_object:
    guest_name = input("Please enter your name, honoured guest!: ")
    file_object.write(guest_name)