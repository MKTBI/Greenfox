# Create a simple calculator application which reads parameters from the prompt
# and prints the result back to the prompt
# It should support one of the following operators: +, -, *, /, %
# and two operands
# The format of the input expressions must be: {operator} {operand} {operand}
# Input examples:
#    "+ 3 3" (the result will be 6)
#    "* 4 4" (the result will be 16)

# To make it work create a method named "calculate()" and use the Scanner class
# to get input from the user

# The process should work like this:
# - Start the program
# - Print: "Please type in the expression:"
#   (Wait for the user input)
# - After receiving the input print the result number to the prompt
# - Exit the program




def calculate():
    
    input_string = input("Please type in the expression and two numbers with speace")

    
    parts = input_string.split()
    operator = parts[0]
    num1 = int(parts[1])
    num2 = int(parts[2])

   
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    elif operator == "%":
        result = num1 % num2
    else:
        result = "Invalid operator"

    print(result)


calculate()
