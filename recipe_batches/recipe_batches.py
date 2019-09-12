#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  rec_keys = list(recipe.keys())
  ingredient_keys = list(ingredients.keys())

  #if the recipes keys are longer than the ingredient keys, it's an auto fail
  if len(rec_keys) > len(ingredient_keys):
    return 0

  #now to check the actual ingredients
  amount_of_batches = []
  lowest_amount = 0

  for i in recipe:
    #next auto-fail is if a recipe requires more than the ingredients at hand.
    if (recipe[i] > ingredients[i]):
      return 0
    else:
      #if there are enough ingredients, check how much more there are and store the value in a list.
      amount_of_batches.append(ingredients[i] // recipe[i])
  
  for k in range(0, len(amount_of_batches)):
    #set lowest to the first value
    if k == 0:
      lowest_amount = amount_of_batches[k]
    
    #check the rest to see if there is a lower value
    else: 
      if amount_of_batches[k] < lowest_amount:
        lowest_amount = amount_of_batches[k]

  #send it
  return lowest_amount
    



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))