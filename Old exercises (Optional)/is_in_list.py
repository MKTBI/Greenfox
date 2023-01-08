# Check if "list_of_numbers" contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# It should return "True" if it contains all elements, otherwise returns "False"

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]

def check_nums(numbers:list) -> str:
    if 4 and 8 and 12 and 16 in numbers:
        return True
    else: 
        return False


print(check_nums(list_of_numbers))