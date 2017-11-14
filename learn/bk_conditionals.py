"""
Demonstration Logic and Conditionals
"""

def greet(friend, bling):
    """
    Greet people.  Say hi if they are your friend.  Give them
    $20 if they are your friend and you have enough money.  Steal
    $10 from them if they are not your friend.
    """
    if friend and (bling > 20):
        print("Hi!")
        bling = bling - 20
    elif friend:
        print("Hello")
    else:
        print("Ha ha!")
        bling = bling + 10
    return bling


money = 20

money = greet(True, money)
print("Money:", money)
print()

money = greet(False, money)
print("Money:", money)
print()

money = greet(True, money)
print("Money:", money)
print()

print("My hunger function result is: ")

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
MOOLA = 10
am_i_hungry(TUMMY, MOOLA)


def boolean_exp(val_a, val_b):
    print("Value: " + str(not(val_a or not val_b)))

print()
print("Evaluate boolean logic expression for 'not(A or not B)'")
boolean_exp(True, True)
boolean_exp(True, False)
boolean_exp(False, True)
boolean_exp(False, False)

print()
print("Which expressions evaluate to true")
print(not(True == False))
print(True == False)
print(not True)
print(True != False)

print()
print("Logically Equivalent example")
print(2 >= 1)
print((2 > 1) or (2 == 1))


def nand(bool1, bool2):
    """
    Take two Boolean values bool1 and bool2
    and return the specified Boolean values
    """

    if bool1:
        if bool2:
            return False
        else:
            return True
    else:
        return True

BOOL1 = True
BOOL2 = True

print()
print("The Control Boolean Expression, nand(bool1, bool2) result: " + str(nand(BOOL1, BOOL2)))
print("Choice #1 not(bool1 and bool2): " + str(not(BOOL1 and BOOL2)))
print("Choice #2 (bool1 or bool2): " + str(BOOL1 or BOOL2))
print("Choice #3: not(bool1 or bool2)" + str(not(BOOL1 or BOOL2)))
print("Choice #4: (bool1 and bool2)" + str(BOOL1 and BOOL2))


#Collatz Conjecture
def f(num):
#    print("Number is: " + str(num))
    xval = num % 2
#    print(xval)
    if xval == 0:
        result = num//2
#        print("If result: " + str(result))
        return result

    else:
        result = 3 * num + 1
#        print("Else result: " + str(result))
        return result

print()
print("Entering Collatz Exercise...")
# f(f(f(f(f(f(f(674)))))))
print("Collatz Result is: " + str(f(f(f(f(f(f(f(f(f(f(f(f(f(f(1071))))))))))))))))
print()

