"""
Implementing RPSLS for Practice Project
"""

import random

def name_to_number(name):
    """
    Take string name as input (rock-Spock-paper-lizard-scissors)
    and returns integer (0-1-2-3-4)
    """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print("I do not recognize the input name you used. Please try again.")

def number_to_name(number):
    """
    Take string name as input (rock-Spock-paper-lizard-scissors)
    and returns integer (0-1-2-3-4)
    """
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print("I do not recognize the input number you used. Please try again.")

def rpsls(player_choice):
    """
    Given string player_choice, play a game of RPSLS
    and print the results to the console
    :param player_choice:
    :return:
    """
    print()
    print("Player chose: " + player_choice)
    player_number = name_to_number(player_choice)
    print("Player number is: " + str(player_number))
    computer_number = random.randrange(start=0, stop=4)
    computer_choice=number_to_name(computer_number)
    print("Computer chose: " + computer_choice)
    print()

    difference = (computer_number - player_number) % 5

    if difference == 0:
        print("Player and computer tie!")
    elif (difference == 1) or (difference == 2):
        print("Computer wins!")
    else:
        print("Player wins!")


rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


# print(name_to_number("rock"))  # output - 0
# print(name_to_number("Spock"))  # output - 1
# print(name_to_number("paper"))  # output - 2
# print(name_to_number("lizard"))  # output - 3
# print(name_to_number("scissors"))  # output - 4
# # print(name_to_number("spock"))  # output - none
#
# print(number_to_name(0))  # output - 0
# print(number_to_name(1))  # output - 1
# print(number_to_name(2))  # output - 2
# print(number_to_name(3))  # output - 3
# print(number_to_name(4))  # output - 4
# # print(number_to_name("0"))  # output - none