
selected_operation = input("What kind of operation do you want to do? (Add / Subtract / Multiply / Divide): ").upper()

first_number = input("Please input a number: ")
second_number = input("Please input another number to do the operation: ")

if selected_operation == "ADD":
    answer = int(first_number) + int(second_number)
    print("The answer to the operation is {}".format(answer))
elif selected_operation ==  "SUBTRACT":
    answer = int(first_number) - int(second_number)
    print("The answer to the operation is {}".format(answer))
elif selected_operation == "MULTIPLY":
    answer = int(first_number) * int(second_number)
    print("The answer to the operation is {}".format(answer))
else:
    answer = int(first_number) / int(second_number)
    print("The answer to the operation is {}".format(answer))
