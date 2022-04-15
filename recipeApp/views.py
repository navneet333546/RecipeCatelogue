from cmath import exp
from math import degrees
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipes

# Create your views here.


def say_hello(request):
    return render(request,'index.html')

recipe1 = Recipes()
recipe1.id = 0
recipe1.title = 'Chicken Bar BBQ Pizza Recipe'
recipe1.img = 'recipe_images/dish-4.png'
recipe1.desc = 'BBQ Chicken, Whether Cooked On The Grill Or Baked In The Oven, Is One Of Those Dinners Nobody At The Table Will Complain About. Unless It’s Dry And Overcooked. But That Is NOT This Recipe. It’s A Basic Anyone Can Easily Master, So That They Too Can Claim Their BBQ …'
recipe1.cookTime = 45
recipe1.ingredients = '350 gm chicken 1/2 teaspoon ginger paste 1/2 teaspoon red chilli powder 1/4 teaspoon cumin powder salt as required 1/2 cup hung curd 1/2 teaspoon garlic paste 1/4 teaspoon coriander powder 1/4 teaspoon powdered black pepper 1 teaspoon garam masala powder'
recipe1.author = 'Admin'
recipe1.date = '2022-04-04'

recipe2 = Recipes()
recipe2.id = 1
recipe2.title = 'Chocolate Chip Cookies Recipe'
recipe2.img = 'recipe_images/dish-5.png'
recipe2.desc = 'These Cookies Are Great...You Get A Double Dose Of Chocolate! My Kids Love Them. Directions Instructions Checklist Step 1 Preheat Oven To 350 Degrees F (175 Degrees C). Step 2 In Large Bowl, Beat Butter, Sugar, Eggs, And Vanilla Until Light And Fluffy. Combine The Flour, Cocoa, Baking Soda, And …'
recipe2.cookTime = 60
recipe2.ingredients = '1 cup butter, softened 1 ½ cups white sugar 2 eggs 2 teaspoons vanilla extract 2 cups all-purpose flour ⅔ cup cocoa powder ¾ teaspoon baking soda ¼ teaspoon salt 2 cups semisweet chocolate chips ½ cup chopped walnuts (Optional)'
recipe2.author = 'Admin'
recipe2.date = '2022-04-04'

recipe3 = Recipes()
recipe3.id = 2
recipe3.title = 'Oat Meal Recipe'
recipe3.img = 'recipe_images/menu-8.jpg'
recipe3.desc = 'This List Of Healthy Oatmeal Recipes Brings You All The Oatmeal Flavor Combos You Could Ever Imagine. With Its High Fiber Content, Oatmeal Is Sure To Keep You Full All Morning To Conquer The Day Ahead! Why Do I Love Oats So Much? Well, They’re… High In Fiber And Antioxidants …'
recipe3.cookTime = 10
recipe3.ingredients = 'You’ll need old fashioned oats or rolled oats, milk, water and a dash of salt.'
recipe3.author = 'Admin'
recipe3.date = '2022-04-04'

recipe4 = Recipes()
recipe4.id = 3
recipe4.title = 'Zinger Burger Recipe'
recipe4.img = 'recipe_images/dish-1.png'
recipe4.desc = 'This KFC Zinger Burger Recipe Allows You To Create The Delicious And Tangy Zingers At Home Whenever Your Want. We Also Have A Recipe For The Special KFC Zinger Sauce Which You Can Find Here. You Can Find Our Recipe For The KFC Zinger Sauce Here. 1) Prepare Your Chicken …'
recipe4.cookTime = 35
recipe4.ingredients = '• Chicken fillet 4 to 5 • Iceberg lettuce 4 to 5 leaves • Eggs 4 • Plain flour 1/2 cup • Cornflour 1/2 cup • Mustard powder 1 tsp • Baking powder 1 tsp • Cheese slices 4 to 5 • Hot sauce as required • Mayonnaise as required • Hot milk 1 cup • Flour 1 tbsp • Chicken cube 1 • Sugar 1 tsp • White pepper 1 tsp • Salt to taste • Buns 4 to 6 • Oil as required'
recipe4.author = 'Admin'
recipe4.date = '2022-04-04'

recipesList = [recipe1,recipe2,recipe3,recipe4]

def show_recipes(request):
    try:
        return render(request,'recipes.html',{"recipesList":recipesList})
    except:
        print('Something Went Wrong')

def error_404_view(request,exception):
    return render(request,'404.html')

def show_recipeDetails(request):
    try:
        recipeindex = 0
        for index in recipesList:
            if(index.id == int(request.GET['recipeID']) ):
                recipeindex = int(request.GET['recipeID']) 
        recipeData = recipesList[recipeindex]
        return render(request,'recipeDetails.html',{'recipeData':recipeData})    
    except:
        print('Something Went Wrong')

def show_dataModel(request):
    try:
        return render(request,'dataModel.html')    
    except:
        print('Something Went Wrong')        