"""
Demonstration of else and elif.
"""

def greet(friend, money):
    """
    Greet people.  Say hi if they are your friend.  Give them
    $20 if they are your friend and you have enough money.  Steal
    $10 from them if they are not your friend.
    """
    if friend and (money > 20):
        print("Hi!")
        money = money - 20
    elif friend:
        print("Hello")
    else:
        print("Ha ha!")
        money = money + 10
    return money


money = 15

money = greet(True, money)
print("Money:", money)
print()

money = greet(False, money)
print("Money:", money)
print()

money = greet(True, money)
print("Money:", money)
print()



def am_i_hungry(hunger, cash):
    """
    Takes two input strings for hunger and amount of money and returns a status string
    depending on the values and boolean evaluation of those two inputs

    :param hunger:
    :param cash:
    :return:
    """
    if hunger and cash >= 10:
        print("Have a snack!")

    elif hunger and cash < 10:
        print("Get some money from the ATM!")
    else:
        print("I'm full.")

TUMMY = True
MOOLA=10
am_i_hungry(TUMMY, MOOLA)