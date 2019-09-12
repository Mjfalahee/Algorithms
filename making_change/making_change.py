#!/usr/bin/python

import sys

#defining a cache for use

def making_change(amount, denominations, cache=None):

  #base case
  if amount == 0:
    return 1

  elif amount < 0 or denominations == []:
    return 1

  elif cache and (cache[amount] > 0):
    return cache[amount]

  else:
    if not cache:
      cache = {i: 0 for i in range(0, amount+1)}
      cache[0] = 1
    for coin in denominations:
      print('coin', coin)
      for higher_amount in range(coin, amount+1):
        print('higher_amount', higher_amount)
        difference = higher_amount - coin
        cache[amount] = cache[difference] + cache[amount]

  
  return cache[amount]

making_change(5, [1,5,10])
print(making_change(11, [1,5,10]))

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")