import string

def most_common_word(file_name: str) -> str:
    
    word_count = {}
    try:
        with open(file_name, "r") as f:
            for line in f:
                for word in line.translate(str.maketrans('', '', string.punctuation)).lower().split():
                    word_count[word] = word_count.get(word, 0) + 1
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return ""
    
    most_common = max(word_count, key=word_count.get)
    return most_common


print(most_common_word("Trial Exam.txt"))