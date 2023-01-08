# Create a function called 'create_new_verbs()' which takes a list of verbs and a string as parameters
# The string should be a prefix
# The function appends every verb to the prefix and returns the list of the new verbs

verbs = ["megy", "ver", "kapcsol", "rak", "néz"]
preverb = "be"

def create_new_verbs(preverb: str, verbs: list) -> list:
    return [preverb + verb for verb in verbs]


print(create_new_verbs(preverb, verbs))
# The output should be: "bemegy", "bever", "bekapcsol", "berak", "benéz"