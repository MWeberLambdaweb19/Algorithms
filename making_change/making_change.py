#!/usr/bin/python

import sys


def making_change(amount, denominations):
  # We need a base case for the smallest amount and the smallest denomination

  # if amount == 0 and len(denominations) == 0:
  #   return 0
  if amount == 0: 
    return 1
  elif amount < 0:
    return 0 
  if len(denominations) <= 0 and amount > 0:
    return 0
  else: 
                            # 250        # 50                                                              # next after end of list, 25
    value = (making_change(amount - denominations[-1], denominations) + making_change(amount, denominations[:-1]))
    # the next go around, recursion, ^ will be 25
    return value




  

  # return making_change(amount -1, denominations) + making_change(amount -2, denominations) + making_change(amount-3, denominations) + making_change(amount-4, denominations) + making_change(amount-5, denominations)
  # return making_change(n-1) + making_change(n-2) 


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")








  # LEGACY CODE
  # smallest_denomination = 1
  # for i in range(0, len(denominations) -1):
  #   if denominations[smallest_denomination] < denominations[i]:
  #     smallest_denomination = denominations[i]
  #     print('smallest!', smallest_denomination)
  # largest_denomination = 50
  # if amount <= denomonations[0]:
    
  # elif amount >= denominations[-1]:

  # FIB CACHE

  def fib_buttom(n):
    fib_cache = [0, 1]
    for i in range(2, n + 1):
      fib_cache.append(fib_cache[i-1] + fib_cache[i-2])
    return fib_cache