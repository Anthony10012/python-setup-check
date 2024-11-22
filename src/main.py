
operand1 = None
operator = None
operand2 = None
result = None

def main():
    ask_user_input()
    global result
    result = calculate(operand1,operator, operand2)
    display_result(operand1, operator ,operand2 , result)
    # Perform the operation based on the operator

def ask_user_input():
    # Get first operand from the user
    global operand1
    operand1 = float(input("Enter the first operand: "))

    # Get the operator from the user
    global operator
    operator = input("Enter an operator (+, -, *, /): ")

    # Get second operand from the user
    global operand2
    operand2 = float(input("Enter the second operand: "))

def calculate(ope1, oper, ope2):
    res = None
    match oper:

        case '+':
            res = ope1 + ope2

        case'-':
            res = ope1 - ope2

        case '*':
            res = ope1 * ope2

        case '/':
            if ope2 == 0:
                print("Error: Division by zero is undefined.")
                return
            res = ope1 / ope2
        case _:
            print("Invalid operator.")
            return
    return res

def display_result(ope1, ope, ope2, res):
    print(str(ope1)+ " " + ope + " " + str(ope2) + " = " + str(res))

# Call the main function to run the program
main()

