while True:

    print("===Calculator===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Square root")
    print("7. Cube root")
    print("8. Power")
    print("9. Exit")

    try:

        operation = input("Select options from the above list (1-5): ")

        if(operation=='1'):
            print("You have selected Addition")

        elif(operation=='2'):
            print("You have selected Subtraction")

        elif(operation=='3'):
            print("You have selected Multiplication")

        elif(operation=='4'):
            print("You have selected Division")

        elif(operation=='5'):
            print("You have selected Modulus")

        elif(operation=='6'):
            print("You have selected Square root")

        elif(operation=='7'):
            print("You have selected Cube root")

        elif(operation=='8'):
            print("You have selected Power")

        elif(operation=='9'):
            print("You have selected Exit")
            break
        
        else:
            print("You have selected something else")
    
    except:
        print("Please enter valid number from 1-5,not text")
    

    try:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if(operation=='1'):
            sum = num1+num2
            print(f"Addition of {num1} and {num2} is {sum}")

        elif(operation=='2'):
            difference = num1-num2
            print(f"Subtraction of {num1} and {num2} is {difference}")

        elif(operation=='3'):
            product = num1*num2
            print(f"Multiplication of {num1} and {num2} is {product}")

        elif(operation=='4'):
            remmainder = num1/num2
            print(f"Division of {num1} and {num2} is {remmainder}")

        
        elif(operation=='5'):
            mod = num1%num2
            print(f"Modulus of {num1} and {num2} is {mod}")

        
        elif(operation=='6'):
                print(f"Square root of {num1} is {num1 ** 0.5}")

        elif(operation=='7'):
                print(f"Cube root of {num1} is {num1 ** (1/3)}")

        elif(operation=='8'):
                print(f"{num1} raised to the power of {num2} is {num1 ** num2}")
        
        elif(operation=='9'):
            print("You are exit from the program Goodbye!!")

        else:
            print("Something went wrong")

    except ValueError:
            print(" Please enter valid numeric values.")

    



