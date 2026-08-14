import art,os


print(art.logo)
def clear_screen():
    """Clears screen with cross_platform availability"""
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Mac/Linux/Unix
        os.system('clear')

active = True
bids = {}
while active:
    name = input("What is your name?\n")
    price = input("What are you bidding?\n$")
    bids[name] = int(price)
    clear_screen()
    newbid = input("Any other bids (y/n):\n").lower()
    if newbid == "n":
        active = False
highest_bid = 0
winner_name = ""
for bid in bids:
    if bids[bid] > highest_bid:
        highest_bid = bids[bid]
        winner_name = bid

print(f"Highest bid was by {winner_name} with the price of ${highest_bid}. Congrats!")
