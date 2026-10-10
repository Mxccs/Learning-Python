Num1 = float(input("please enter your number: "))
Num2 = float(input("please enter your second number: "))

AskNum3 = str(input("do you want to calculate another number? (yes/no): ")).strip().lower()
if AskNum3 == "yes":
    Num3 = float(input("please enter your third number: "))

    Question = str(input("do you want to multiply or divide or minus or add? (multiply/divide/minus/add): ")).strip().lower()

    if Question == "multiply":
            result = Num1 * Num2 * Num3
            print("the result of multiplication is: " + str(result))
    elif Question == "divide":
            if Num2 != 0:
                result = Num1 / Num2 / Num3
                print("the result of division is: " + str(result))
            else:
                print("Error: Division by zero is not allowed.")
    elif Question == "minus":
        result = Num1 - Num2 - Num3
        print("the result of subtraction is: " + str(result))
    elif Question == "add":
        result = Num1 + Num2 + Num3
        print("the result of addition is: " + str(result))
    else:
        print("Invalid operation. Please choose from multiply, divide, minus, or add.")
elif AskNum3 == "no":
    Question = str(input("do you want to multiply or divide or minus or add? (multiply/divide/minus/add): ")).strip().lower()
    if Question == "multiply":
        result = Num1 * Num2
        print("the result of multiplication is: " + str(result))
    elif Question == "divide":
        if Num2 != 0:
            result = Num1 / Num2
            print("the result of division is: " + str(result))
        else:
            print("Error: Division by zero is not allowed.")
    elif Question == "minus":
        result = Num1 - Num2
        print("the result of subtraction is: " + str(result))
    elif Question == "add":
        result = Num1 + Num2
        print("the result of addition is: " + str(result))
    else:
        print("Invalid operation. Please choose from multiply, divide, minus, or add.")
else:
     print("please enter yes or no")


# ==================================================================
# (ORGANIZE WITH THE HELP OF AI)
# ==================================================================
# (This project was written by MXSYZ (me) from scratch)
# (AI assistance was used for debugging and learning purposes only)
# ==================================================================