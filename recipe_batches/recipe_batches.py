#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  #takes recipe first, then ingredients
  #I want to separate values from keys, so I can quickly evaluate if all of the recipe ingredients exist
  rec_keys = list(recipe.keys())
  ingredient_keys = list(ingredients.keys())

  #if the recipes keys are longer than the ingredient keys, it's an auto fail
  if len(rec_keys) > len(ingredient_keys):
    return 0


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))