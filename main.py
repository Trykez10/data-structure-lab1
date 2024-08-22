firstNum = int(input("Enter First Number: "))
secondNum = int(input("Enter First Number: "))

if firstNum < secondNum:
    print(f"{firstNum} is less than {secondNum}")
elif firstNum > secondNum:
    print(f"{firstNum} is greater than {secondNum}")
elif firstNum == secondNum:
    print(f"{firstNum} is equals to {secondNum}")
else:
    print("Can't determined")

name_One = input("Enter classmate name 1: ")
name_Two = input("Enter classmate name 2: ")
name_Three = input("Enter classmate name 3: ")
print(f"Your classmates are: {name_One}, {name_Two}, & {name_Three}")