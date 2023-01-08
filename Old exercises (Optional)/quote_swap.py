# Accidentally I messed up this quote from Richard Feynman
# Two words are out of place
# Your task is to fix it by swapping the right words with code
# To do this: create a method called "swap_quote()"

words = ["What", "I", "do", "create,", "I", "cannot", "not", "understand."]

def swap_quote(words: list) -> str:
    
    words[2], words[5] = words[5], words[2]
    return " ".join(words)

print(swap_quote(words))
# Expected output: "What I cannot create I do not understand."