#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # We need to compare two dictionaries, recipe and ingredients
  # We need to make sure that every key in recipe also exists in ingredients
  if recipe.keys() != ingredients.keys():
    return 0
  else:
    batches = 0
    multiples = 0
    prevmult = None
    # We need to make sure that every value in each key in recipe is less than
      # or equal to the key value pair in ingredients
    for i in recipe:
      if recipe[i] == ingredients[i]:
        batches += 1
      elif recipe[i] >= ingredients[i]:
        batches -= 0
      else: 
      # If the value of (ingredient_key) is (n>1 * value recipe_key), we need to track that 
        # in a variable
      # If each value of (ingredient_key) is (n>1 * value recipe_key), we need to return
        # how many batches of dictionary recipe with dictonary ingredients
        batches += 1
        batch_mult = ingredients[i] // recipe[i]
        if prevmult == None:
          prevmult = batch_mult
          multiples = batch_mult
        else: 
          if prevmult == batch_mult:
            multiples = batch_mult
          elif prevmult <= batch_mult:
            multiples = prevmult
          else:
            multiples = 0
    if batches == len(ingredients) and multiples == 0:
        return 1
    elif multiples != 0 and batches == len(ingredients):
        return multiples

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  # recipe = { 'milk': 100, 'butter': 50, 'flour': 5, }
  # ingredients = { 'milk': 300, 'butter': 150, 'flour': 15 }
  recipe = { 'milk': 2, 'sugar': 3, 'flour': 4, 'eggs': 5 }
  ingredients = { 'flour': 400, 'sugar': 300, 'eggs': 500, 'milk': 200, }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))