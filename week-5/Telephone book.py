phoneBook = {
  "William A. Lathan": "405-709-1865",
  "John K. Miller": "402-247-8568",
  "Hortensia E. Foster": "606-481-6467",
  "Amanda D. Newland": "319-243-5613",
  "Brooke P. Askew": "307-687-2982"
}

# What is John K. Miller's phone number?
print("John K. Miller's phone number is", phoneBook["John K. Miller"])

# Whose phone number is 307-687-2982?
for name, number in phoneBook.items():
  if number == "307-687-2982":
    print(name, "has the phone number 307-687-2982")

# Do we know Chris E. Myers' phone number? (yes/no)
if "Chris E. Myers" in phoneBook:
  print("We know Chris E. Myers' phone number")
else:
  print("We do not know Chris E. Myers' phone number")
