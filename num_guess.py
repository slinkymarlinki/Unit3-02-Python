#!usr/bin/env python3
# Created By: Marli Peters
# Date: Oct. 12, 2023
# This program asks the user to guess a
# number then tells user if the guess was correct.
import constants


def main():
    # get user guess
    guess = int(input("Guess number: "))
    print("")

    # check if guess is correct
    if guess == constants.answer:
        print("Your guess was correct!")

    else:
        print("Your answer was incorrect!")


if __name__ == "__main__":
    main()
