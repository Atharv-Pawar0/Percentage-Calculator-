a = input("Enter your Marks: ")
b = input("Enter Total Marks: ")

if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)

    if b == 0:
        print("Total marks cannot be zero.")
    elif a > b:
        print("Obtained marks cannot be greater than total marks.")
    else:
        percentage = (a * 100) / b
        print(f"Your Percentage: {percentage:.2f}%")
else:
    print("Please enter valid positive numbers only.")