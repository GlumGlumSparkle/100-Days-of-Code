from Secret_Auction_logo import *
import os
print(logo)

bidding_finished = False
auction = {}
while not bidding_finished:

    name = input("Please input your name:\n")
    bid_price = input("Please input bid price in dollars:\n")
    auction.update({name:bid_price})
    reply = input("Are there other users who want to bid?\n").lower()

    if reply == "yes":
        os.system("cls")

    if reply == "no":
        max_key = max(auction, key=auction.get)
        print(f"The winner is - {max_key} with bid - {auction[max_key]}$")
        bidding_finished = True
