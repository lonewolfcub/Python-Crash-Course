first_number = input("\nFirst number: ")
second_number = input("\nSecond number: ")
try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("You must input integers!")
else:
    print(answer)