phone = input("phone number> ")
newnumb = ''

dictnumb = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",
}

for translatednum in phone:
    if translatednum in dictnumb:
        newnumb += dictnumb.get(translatednum) + " "
    else:
        print("Error: Please enter only digits (0-9).")
        break

print(newnumb)
