#  Create a function that takes a string and a list of string as a parameter 
#  and returns the index of the string (in the list) which contains the first string
#  You only need to find the first occurrence and return the index of that
#  Return `-1` if none of the items in the list contain the first string

def find_index(string, list_of_strings):
    for i, item in enumerate(list_of_strings):
        if string in item:
            return i
    return -1

#  Example
print(find_index("ching", ["this", "is", "what", "I'm", "searching", "in"]))
#  should print: `4`
print(find_index("not", ["this", "is", "what", "I'm", "searching", "in"]))
#  should print: `-1`