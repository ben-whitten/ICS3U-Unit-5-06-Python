#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: November 2019
# This is a program which finds the area of the triangle.


# This allows me to do things with the text.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def rounding(number):
    # This rounds it
    number[0] = (number[0]*(10**number[1])+0.5)
    number[0] = int(number[0])
    number[0] = float(number[0])
    number[0] = (number[0]/(10**number[1]))


def main():
    # This is what gets the variables

    number = []

    while True:
        number_as_string = input(color.YELLOW + 'Input a number: ' + color.END)
        decimal_as_string = input(color.YELLOW + "Input the number of decimal"
                                  + " places to round to: " + color.END)

        try:
            chosen_number = float(number_as_string)
            decimal = int(decimal_as_string)

            number.append(chosen_number)
            number.append(decimal)

            rounding(number)

            print(number[0])
            break

        except Exception:
            print('')
            print(color.PURPLE + color.UNDERLINE + 'That is not a valid'
                  ' number...' + color.END)
            print("")
            print("")


if __name__ == "__main__":
    main()
