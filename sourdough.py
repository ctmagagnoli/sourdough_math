"""
NAME:
    Sourdough Code
    
PURPOSE:
    Create/edit a CSV file of recipies, include a way to add recipies to said 
    file, and provide options to scale recipes up/down for convienience
    
REFERENCE:
    Christina Magagnoli

CALLING SEQUENCE:
    python3 "sourdough.py"

MODIFICATION HISTORY:
    Created on 2023-12-09
    Last modified on 2023-12-09
"""
import pandas as pd
import numpy as np
from fractions import Fraction
#*******************************************************************************
def add_recipe(recipeName, recipe_filename):
    df = pd.read_csv(recipe_filename) #open the file with the recipes as a DataFrame
    yn = recipeName in df.recipe_name.values #Checks to see if the recipe already exists in the file
    if yn == False: #If the recipe is not there, we're going to put it in
        is_done = False
        while is_done != True: #Here we insert the loop to add ingredients
            ing = input('Ingredient: ')     
            str_ing_amount = input('How much of it? ') #Cannot handle fractions
            ing_amount = float(sum(Fraction(s) for s in str_ing_amount.split()))
            un = input('What units? ')
            #these three input lines take in the needed data for our row
            newline = {'recipe_name' : recipeName, 'ingredient' : ing, 'amount' : ing_amount, 'unit' : un} #format the row
            df = df.append(newline, ignore_index=True) #add the line
            check = input('Add another ingredient? Y/N ') #are we done?
            if str.lower(check).startswith("n"):
                is_done = True
        df.to_csv(recipe_filename)
    else: #this statement asks for what should happen if the user tries to input a recipe with a name that already exists in the file
        tf = input('There is already a recipe with this name. Would you like to see the ingredients? Y/N ')
        if str.lower(tf).startswith("y"): #NEED TO REWORK THIS WHOLE SECTION
            print(df[df.recipe_name.isin([recipeName])])
    #print(df)

add_recipe('buttery_sourdough_biscuits', 'recipes.csv')

