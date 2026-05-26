def check_even_odd(num):
    if num % 2 == 0:    
        return "Even"
    else:
        return "Odd"

def check_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
        else:
            return True

def check_palindrome(s):
    s = s.lower()

    if s==s[::-1]:
        return True
    else:
        return False

def calculator():
    print("Welcome to the Mini Calculator!!")
    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the second number : "))
    operation = input("Enter the operation (+, -, *, /) : ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        print("Invalid operation!")
    return print(f"The result of {num1} {operation} {num2} is {result}.")

def multiplication_table(num):
    print(f"Multiplication Table for {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

while True:
    print("\n*****************************************************")
    print("*********** Welcome to the Logic Toolkit! ***********")
    print("*****************************************************")

    print("What operations would you like to perform? ")
    print("1. Even or Odd checker")
    print("2. Prime number checker")
    print("3. Palindrome checker")
    print("4. Calculator")
    print("5. Multiplication table generator")
    print("6. Exit ")

    choice = input("Enter the number corresponding to your choice: ")  
    if choice == '1':
        print("You chose the Even or Odd checker!")
        number = int(input("Enter a number to check if it's even or odd: "))
        result = check_even_odd(number)
        print(f"The number {number} is {result}.")
    elif choice == '2':
        print("You chose the Prime number checker!")
        number = int(input("Enter the number to check if it's Prime : "))
        result = check_prime(number)
        if result:
            print(f"The given number {number} is Prime.")
        else:
            print(f"The given number {number} is not Prime.")
    elif choice == '3':
        print("You chose the Palindrome checker!")
        string = input("Enter a string to check if it's a Palindrome :")
        result = check_palindrome(string)
        if result:
            print(f"The given string '{string}' is a Palindrome.")
        else:
            print(f"The given string '{string}' is not a Palindrome.")
    elif choice == '4': 
        print("You chose the Calculator!")
        calculator()
    elif choice == '5':   
        print("You chose the Multiplication table generator!")
        num = int(input("Enter a number to generate its multiplication table: "))
        multiplication_table(num)

    elif choice == '6':
        print("You chose to exit!")
        break
    else:
        print("Invalid choice. Please select a number from 1 to 6.")


        
