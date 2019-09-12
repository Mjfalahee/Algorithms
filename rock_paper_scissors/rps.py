#!/usr/bin/python

import sys


def rock_paper_scissors(n):
  #Define all possible plays in a list
  plays = ['rock', 'paper', 'scissors']

  #Define a list to hold all of the possible plays
  result = []

  def rpshelper(n, rps):
    #base case or ceiling, if (len(rps) == 0) ==> result.append([]) ==> result = [[]]
    #if ceiling (rps has hit length n), append it to the result array
    if len(rps) == n:
      return result.append(rps)

    #iterate through possible plays, push rps + [i] together to make [rps, i]
    #and send back through recursion until rps is of length n
    for i in plays:
      rpshelper(n, rps + [i])
  
  #invoke helper to start recursion with a blank array
  rpshelper(n, [])
  return result


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

  # 0 - [[]]
  # 1 - [['rock'], ['paper'], ['scissors']]
  # 2 - [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]


  # 0 - [[]] 1
  # 1 - [[1], [2], [3]] 3
  # 2 - [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]] 9
  # 3 - [[]] 27
  # 4 - [[]] 81
  # 5 - [[]] 243

  # relationship is (n-1)*3