"""
Day 9
Blind Auction Challenge

[Sol]
    1. Ask the user for their name
    2. Ask the user how much they want to bid
    3. Store this into a dictionary where the name is the key
       with the value being a list of name and bid
    4. Ask if there are any more bidders
        a. Check the highest bid if no one else bids
        b. Clear the screen and loop back to 1

"""

from art import logo


def print_logo():
    print(logo)


def compare_bids(bid_log):
    winning_bid = 0
    current_winner = ''
    for key in bid_log:
        if float(bid_log[key][1]) > float(winning_bid):
            winning_bid = bid_log[key][1]
            current_winner = bid_log[key][0]
    winning_bidder = [current_winner, winning_bid]
    return winning_bidder


if __name__ == "__main__":
    print_logo()
    bidding_log = {}
    more_bidders = True

    while more_bidders:
        # TODO-1: Ask the user for input
        name = input("what is your name? ")
        price = input("How much will you bid? $")

        # TODO-2: Save data into dictionary {name: price}
        bidding_log[name] = [name, price]

        # TODO-3: Whether if new bids need to be added
        valid_answer = False    # Verify yes or no as an answer for more bidders
        while not valid_answer:
            additional_bids = input("Are there anymore bidders? (y/N) ")
            if additional_bids.lower() == 'y' or additional_bids.lower() == "yes":
                valid_answer = True
                more_bidders = True
                print("\n" * 50)
            # TODO-4: Compare bids in dictionary
            elif additional_bids.lower() == 'n' or additional_bids.lower() == "no":
                valid_answer = True
                more_bidders = False
                winner = compare_bids(bidding_log)
                print(f"The winner is {winner[0]} with a bid of ${winner[1]}")
            else:
                print("Please refrain from sudden outbursts.")
