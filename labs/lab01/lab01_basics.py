from colorama import init
from colorama import Fore, Back, Style

init()
print(Fore.BLACK)
print(Back.GREEN)

what = input("What to do?(+,-): ")

print(Back.CYAN)

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print(Back.YELLOW)

if what == "+":
    c = a + b
    print("Result: " + str(c))
elif what == "-":
    c = a - b
    print("Result: " + str(c))
else:
    print("Invalid operation!")
