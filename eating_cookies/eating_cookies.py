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
  
  #I don't understand why the test case has zero cookies with a way to eat them, but I'm accounting for that here.
  elif n == 0:
    return 1
  
  #if there aren't cookies, you can't eat them.
  elif n < 0:
    return 0

  #check if it's in the cache
  elif cache and (cache[n] > 0):
    return cache[n]

  #I think the recursive soluton is eating_cookies(n) == (eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3))
  else:
    if not cache:
      cache = {i: 0 for i in range(0, n+1)}
    result = (eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache))
    cache[n] = result
  
  return cache[n]
    


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')