from replit import clear
from art import logo

print(logo)
bids = {}
bidding_ended = False

def find_winner_bid(bid_records):
  win_bid = 0
  win_person = ""
  for bidder in bid_records:
    if int(bid_records[bidder]) > win_bid:
      win_bid = int(bid_records[bidder])
      win_person = bidder
  print(f"The bid by {win_person} has won with ${win_bid}")
  
while not bidding_ended:
  name = input("What is the name: ")
  price = input("What is the bid: $")
  bids[name] = price
  resumer = input("Any other bidders (yes/no): ")
  if resumer == "no":
    bidding_ended = True
    find_winner_bid(bids)
  elif resumer == "yes":
    clear()
  else:
      "Invalid option. Try again."

#can use the last line to see everyone as assurance
print(bids)