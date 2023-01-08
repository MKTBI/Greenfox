# Write a function that checks if the list contains "7" 
# If it does, return "Hoorray" otherwise return "Noooooo"

numbers = [1, 2, 3, 4, 5, 6, 8]
numbers2 = [1,2,3,4,7,6,5]


def contains_seven(numbers: list) -> str:
    if 7 in numbers:
        return "Hoorray"
    else:
        return "Noooooo"



print(contains_seven(numbers))
# The output should be: "Noooooo"
# Do this again with a different solution using different list functions!

print(contains_seven(numbers2)) #Yessss