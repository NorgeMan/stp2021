book = dict()  # or use book = {}

# book["apple"] = 0.67
# book["milk"] = 1.49
# book["avocado"] = 1.49
# print(book)

book = {"apple": 0.49, "milk": 1.49, "avocado": 1.49}
# print(book)

# print(book["apple"]) # print value of key

voted = {}


def check_voter(name):
    if voted.get(name):
        print("Kick them out!")
    else:
        voted[name] = True
        print("Let them vote!")


check_voter("Tom")
check_voter("Mike")
check_voter("Mike")
