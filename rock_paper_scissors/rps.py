#!/usr/bin/python

import sys

#define a list with all of the plays.
plays = ['rock', 'paper', 'scissors']
def rock_paper_scissors(n):

  # recursion
  # List of results. All of length n. All with different values. 
  # cache?
  # Concatenate two lists with the + operator

  inner_lists = []
  #all of the inner_lists are of length n
  result_list = [inner_lists]
  return result_list


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')