#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def eating_cookies(n, cache=None):
  # We need to set a base case
  if n < 0:
    return 0
  if n <= 1:
    return 1
  if cache and cache[n] > 0:
    return cache[n]
  else:
    if not cache:
      cache = {i:0 for i in range(n+1)}
      print(cache)
    value = (eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache))
    cache[n] = value
    return value
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