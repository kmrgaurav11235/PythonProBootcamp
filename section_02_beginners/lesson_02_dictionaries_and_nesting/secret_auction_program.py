from clear_screen import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
bidders_left = "yes"
all_bids = {}

def find_winner(bidding_record):
    winner = ""
    winning_bid = 0.0
    for name in bidding_record:
        if bidding_record[name] > winning_bid:
            winner = name
            winning_bid = bidding_record[name]

    print(f"The winner is {winner} with a bid of ${winning_bid}")

while bidders_left.lower() == "yes":
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))
    all_bids[name] = bid
    bidders_left = input("Are there any other bidders? Type 'yes or 'no'.")
    clear()
find_winner(all_bids)
