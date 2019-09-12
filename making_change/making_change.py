#!/usr/bin/python

import sys

#defining a cache for use

def making_change(amount, denominations, cache=None):

  #base case
  if amount == 0:
    return 1

  #second base case? I think these should be called error cases
  elif amount < 0 or denominations == []:
    return 1


  else:
    if not cache:
      cache = {i: 0 for i in range(0, amount+1)}
      cache[0] = 1

    #iterate through the coins in denominations
    for coin in denominations:

      #iterate through every amount between the coin's value and the amount
      for higher_amount in range(coin, amount+1):

        #the difference between the amount and the coin is one way to solve for that amount. Add it to the cache.
        difference = higher_amount - coin
        cache[higher_amount] += cache[difference]

        #once you iterate through all of the coins, you'll have a running tally of each amount between (inclusive) 0 and the target value
        #with the number of ways to make change

  return cache[amount]

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")