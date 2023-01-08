# Write a method that joins the two lists by matching one girl with one boy into a new list
# If someone has no pair, he/she should be added to the list on his/her own
# Expected output: ["Eve-Joe", "Ashley-Fred", "Claire-Tom", "Kat-Todd", "Jane-Neef", "Jeff"]

girls = ["Eve", "Ashley", "Claire", "Kat", "Jane"]
boys = ["Joe", "Fred", "Tom", "Todd", "Neef", "Jeff"]


def match(girls: list, boys: list) -> list:
    pairs = [f"{girl}-{boy}" for girl, boy in zip(girls, boys)]
    pairs += boys[len(girls):] + girls[len(boys):]
    return pairs


print(match(girls, boys))
