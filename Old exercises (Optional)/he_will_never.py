# Things are a little bit messed up here
# Your job is to decode the not_so_cryptic_message by using the hashmap as a lookup table
# Assemble the fragments into the out variable


not_so_cryptic_message = [1, 12, 1, 2, 11, 1, 7, 11, 1, 49, 1, 3, 11, 1, 50, 11]

hashmap = {
    7: "run around and desert you",
    50: "tell a lie and hurt you ",
    49: "make you cry, ",
    2: "let you down",
    12: "give you up, ",
    1: "Never gonna ",
    11: "\n",
    3: "say goodbye "
}

out = "".join([hashmap[x] for x in not_so_cryptic_message])
print(out)

                