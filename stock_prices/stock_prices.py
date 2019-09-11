#!/usr/bin/python

import argparse

def find_max_profit(prices):
  for i in range(0, len(prices) - 1):
    current_index = i
    #Set up current minimum price, and profit to be the initial value, and zero.
    if i == 0:
      current_min_price_so_far = prices[current_index]
      max_profit_so_far = prices[current_index + 1] - prices[current_index]

    else:
      if prices[i] < current_min_price_so_far:
        current_min_price_so_far = prices[i]
    
    # print('i', i)
    # print('Current Min', current_min_price_so_far)
    # print('Max Profit', max_profit_so_far)
    #loop through the remaining values. This way we always buy first, and sell after.
    for k in range(0, current_index):
      if (prices[current_index] - prices[k]) > max_profit_so_far:
        max_profit_so_far = (prices[current_index] - prices[k])

  return max_profit_so_far
  


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))