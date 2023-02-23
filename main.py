from replit import clear
from art import logo

import re

biddings = {}

print(logo)

program_continue = True
while program_continue :

    clear()

    bidder = {}
    
    bidder_name = input("What is your name?: ")
    bid_value = input("What's your bid?: ")
    bid_value = int(re.sub('\D', '', bid_value))
    bidder["name"] = bidder_name
    bidder["bid_value"] = bid_value
    
    biddings["bidder"] = bidder

    decision = input("Is any other person bidding? 'yes' or 'no': ")

    if decision == 'no' :
        program_continue = False
    elif decision != 'yes' :
        print("Wrong value! Program will end.\n")
        program_continue = False

clear()

top_bid = 0
winner = 'nobody'

for bidder in biddings :
    if biddings[bidder]["bid_value"] > top_bid :
        top_bid = biddings[bidder]["bid_value"]
        winner = biddings[bidder]["name"]

print(f"The winner is {winner} with the highest bidding of ${top_bid}.\nCongratulations!")