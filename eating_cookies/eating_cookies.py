#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  ways_to_eat = 0
  #Base case == 1
  if n == 1:
    return 1

  elif n < 1:
    return 0

  elif n in cache:
    print(cache[n])
    return cache[n]

  #I think the recursive soluton is eating_cookies(n) == (eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3))
  else:
    ways_to_eat = (eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache))

  return ways_to_eat
    


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')