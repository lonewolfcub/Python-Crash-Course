age = 12

if age < 4:
    print("Your admission cost is $0\n")
elif age < 18:
    print("Your admission cost is $5\n")
else:
    print("Your admission cost is $10\n")

# This can be written more pythonically as:
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".\n")

# It is possible to use more than one elif:
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".\n")

# It is possible to replace the else block with an elif, this also stops your
# program from executing the else block in response to invalid or malicious
# input

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif:
    price = 5

print("Your admission cost is $" + str(price) + ".\n")
