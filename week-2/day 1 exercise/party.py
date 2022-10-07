G = int(input("number of the girls:"))
B = int(input("number of the boys:"))
if G == B:
    B += G > 20
    print("The party is excellent")
elif G > B:
    B += G
    print("Quite a cool party!")
else:
    G = 0
    print("Sausage party")
G += B < 20
print("Average party...")