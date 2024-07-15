import random
import string
length = int(input("Enter the length of password: "))
alpha = string.ascii_lowercase + string.ascii_uppercase
num = "0123456789"
symbol = string.punctuation
all_char = num + alpha + symbol
while True:
    choice_alpha = input("do you want alphabets in your password? (Y/N): ")
    choice_num = input("do you want numbers in your password? (Y/N): ")
    choice_symbol = input("do you want symbol in your password? (Y/N): ")
    print("generated password: =",end="")
    for i in range(length):
        if choice_alpha == "Y" or choice_alpha == "y" and choice_symbol == "Y" or choice_symbol == "y" and choice_num == "Y" or choice_num == "y":
            print(random.choice(all_char),end="")
        elif choice_symbol == "Y" or choice_symbol == "y" and choice_alpha == "Y" or choice_alpha == "y":
            print(random.choice(symbol + alpha),end="")
        elif choice_num == "Y" or choice_num == "y" and choice_symbol == "Y" or choice_symbol == "y":
            print(random.choice(num + symbol),end="")
        elif choice_alpha == "Y" or choice_alpha == "y" and choice_num == "Y" or choice_num == "y":
            print(random.choice(num + alpha), end="")
        elif choice_alpha == "Y" or choice_alpha == "y":
            print(random.choice(alpha), end="")
        elif choice_num == "Y" or choice_num == "y":
            print(random.choice(num), end="")
        elif choice_symbol == "Y" or choice_symbol == "y":
            print(random.choice(symbol), end="")
    ans = input("\ndo u want to more password? (Y/N):")
    if ans == "N" or ans == "n":
        break
