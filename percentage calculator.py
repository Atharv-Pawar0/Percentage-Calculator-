a_input = input("Enter your Marks: ")
b_input = input("Enter Total Marks: ")

if a_input.isdigit() and b_input.isdigit():
    a = int(a_input)
    b = int(b_input)

    if b == 0:
        print("Total marks cannot be zero.")
    elif a > b:
        print("Obtained marks cannot be greater than total marks.")
    else:
        percentage = (a * 100) / b
        print(f"Your Percentage: {percentage:.2f}%")
else:
    print("Please enter valid positive numbers only.")