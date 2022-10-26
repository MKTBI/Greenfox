num = int(input("write number here: "))
x = num

def calculate_factorial(x):
    factorial = 1
    if x < 0:
        print("we dont have for negative number")
    if x == 0:
        print("it's 1")
    else:
        for i in range(1, num + 1):
            factorial *= i
        print("The factorial of", num, "is", factorial)

calculate_factorial(num)