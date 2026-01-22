num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice : "))

if choice == 1:
    print("The sum of", num1, "and", num2, "is", num1 + num2)
elif choice == 2:
    print("The difference between", num1, "and", num2, "is", num1 - num2)
elif choice == 3:
    print("The product of", num1, "and", num2, "is", num1 * num2)
elif choice == 4:
    print("The division of", num1, "by", num2, "is", num1 / num2)
else:
    print("Invalid choice")