#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  # We need to set a base case
  if n <= 0:
    return 1
  if n == 1:
    return 1
  else:
    return eating_cookies(n-1) + eating_cookies(n-2)
  # We need to find out how many ways Cookie Monster can eat n of cookies
  # We need to possibly set a variable to track this amount
  # We need to rerun the function for each cookie
  # We need to run the function allowing for CM to eat 0, 1, 2, or 3 cookies. 



if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')