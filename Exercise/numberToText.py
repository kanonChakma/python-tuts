#split method
longString = "What are you doing here budyy"
word = longString.split(" ")
print(word)

#-------------
nums = {

    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "Four",
    "5": "Five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

result = ""
phones = input("Phone ")
for phone in phones:
    result += nums.get(phone, "!")+" "

print(result)


