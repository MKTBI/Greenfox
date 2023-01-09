
students = [
        {'name': 'Theodor', 'age': 3, 'candies': 2},
        {'name': 'Paul', 'age': 9, 'candies': 2},
        {'name': 'Mark', 'age': 12, 'candies': 5},
        {'name': 'Peter', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'George', 'age': 10, 'candies': 1}
]

# create a function called listOfNames() that takes a list of students and returns:
# - The name of students who have more than 4 candies

# create a function called sumOfAge() that takes a list of students and returns:
# - The sum of the age of people who have less than 5 candies


def listOfNames(students):
    names = [student['name'] for student in students if student['candies'] > 4]
    return names

def sumOfAge(students):
    ages = [student['age'] for student in students if student['candies'] < 5]
    return sum(ages)


print(listOfNames(students))  # ['Mark', 'Olaf']
print(sumOfAge(students))  # 29
