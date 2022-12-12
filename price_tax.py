#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: Nov.24th, 2022
# This program asks the user for a price of an item
# and calculates the tax and displays the final price

import math


def provincial_tax(original_price):

    # Doing the math to find how much money the provincial government gets
    # from the tax you pay
    pst = original_price * 1.08
    pst = pst - original_price
    pst = round(pst, 2)

    return pst


def federal_tax(original_price):

    # Doing the math to find how much money the federal government gets
    # from the tax you pay
    the_federal_tax = original_price * 1.05
    the_federal_tax = the_federal_tax - original_price
    the_federal_tax = round(the_federal_tax, 2)

    return the_federal_tax


def total_tax_paid(original_price):

    # doing the math to find the tax and round it to 2 decimal places

    price_tax = original_price * 1.13
    price_tax = round(price_tax, 2)

    return price_tax


def main():
    play_again = input("Would you like to play? (yes/no) ")
    while play_again not in ["N", "NO", "n", "no", "No"]:
        # Asking the user for the price of the item they want to buy
        original_price = input("Enter the price of your item: ")

        try:
            # making sure the user input is valid
            original_price = float(original_price)
            if original_price < 0:
                print("Please enter a valid price")
            else:
                # calling the function
                pst = provincial_tax(original_price)
                the_federal_tax = federal_tax(original_price)
                final_price = total_tax_paid(original_price)
                print("The final price of your item is {}".format(final_price))
                print(
                    "The federal government takes {} from the tax you pay".format(
                        the_federal_tax
                    )
                )
                print(
                    "The provincial government takes {} from the tax you pay".format(
                        pst
                    )
                )

        except ValueError:
            print("Please enter a price")

        # Asking the user if they want to play again
        play_again = input("Do you want to try another item? (yes/no) ")

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
