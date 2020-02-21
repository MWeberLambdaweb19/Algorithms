#!/usr/bin/python

import argparse

def find_max_profit(prices):
  current_min_price_so_far = 0
  current_max_price_so_far = len(prices) -1 

  for i in range(len(prices) -1):
    if prices[current_min_price_so_far] > prices[i]:
      current_min_price_so_far = i
  for i in range(current_min_price_so_far + 1, len(prices) -1):
    if prices[current_max_price_so_far] < prices[i]:
      current_max_price_so_far = i
  return prices[current_max_price_so_far] - prices[current_min_price_so_far]


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))



  # LEGACY CODE 
  # def find_max_profit(prices):
  # # We will need a variable that holds the minimum stock price AS WE ITERATE THROUGH THE LIST OF PRICES
  #   # This variable should be the index of that list
  # current_min_price_so_far = 0
  # # We will need a variable that holds the maximum stock price AS WE ITERATE THROUGH THE LIST OF PRICES
  #   # This variable should be the index of that list
  #   # We will need to start at the index of the minimum value as we search through that price
  # current_max_price_so_far = len(prices) - 1
  # # for i in range(current_min_price_so_far, len(prices) - 1):
  # #   if prices[i] <= prices[i+1]:
  # #     current_min_price_so_far = i
  # #   else:
  # #     current_min_price_so_far = i+1
  # # We want to find the difference between the maximum stock price and the minimum stock price
  # # for i in range(current_min_price_so_far + 1, len(prices) - 1):
  # #   if prices[current_max_price_so_far] < prices[i]:
  # #     current_max_price_so_far = i
  # #   elif prices[current_max_price_so_far] > prices[i]:
  # #     current_max_price_so_far = current_max_price_so_far
  # # return current_max_price_so_far - current_min_price_so_far
  # for i in range(len(prices) - 1):
  #   if pri

  # ANOTHER SOLUTION

  # def max(prices):
  #   min = prices[0]
  #   max = prices[1] - min

  #   for i in range (1, len(prices)):
  #     price = prices[i]
  #     max = max(price - min, max)
  #     min = min(price, min)

  #     return max

      # YOU WILL NEED TO CHANGE MAX AND MIN VARIABLES TO NOT COLLIDE WITH THE FUNCTIONS