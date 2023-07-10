bidders = []

while True:

    name = input('What is your name?: ')
    bid = int(input('What is your bid?: $'))

    dict = {
        'name': name,
        'bid': bid
    }
    bidders.append(dict)

    if input('Are there any other bidders? Type "yes" or "no"') == 'no':
        break

winner = ''
highest_bid = 0
for bidder in bidders:
    if bidder['bid'] > highest_bid:
        winner = bidder['name']
        highest_bid = bidder['bid']

print(f'The winner is {winner} with a bid of ${highest_bid}')