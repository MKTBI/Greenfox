
def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit)**num_digits
    return sum == num

num = int(input("Please enter a number to check: "))
if is_armstrong_number(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
