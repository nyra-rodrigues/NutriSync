import MySQLdb as sq
import random
from tabulate import tabulate
import webbrowser

db = sq.connect('localhost', 'root', 'password')
cur = db.cursor()

sql = 'Create Database if not exists info'
cur.execute(sql)

sql1 = 'use info'
cur.execute(sql1)
print('*******************************')
print('Welcome!\n')
print('*******************************')

def dets():
    print('Lets get to know you!')
    list_dis = []
    print('Do you have any of the following:\n')
    print('*******************************')

    # Cholesterol
    Cholesterol = input('Do you suffer from Cholesterol?\n')
    if Cholesterol == 'no' or Cholesterol == 'No' or Cholesterol == 'NO':
        pass
    else:
        list_dis.append('Cholesterol,')

    # High Blood Pressure
    High_Blood_Pressure = input('Do you suffer from High Blood Pressure?\n')
    if High_Blood_Pressure == 'no' or High_Blood_Pressure == 'No' or High_Blood_Pressure == 'NO':
        pass
    else:
        list_dis.append('High Blood Pressure,')

    # Diabetes
    Diabetes = input('Do you suffer from Diabetes?\n')
    if Diabetes == 'no' or Diabetes == 'No' or Diabetes == 'NO':
        pass
    else:
        list_dis.append('Diabetes,')

    # Heart Disease
    Heart_Disease = input('Do you suffer from Heart Disease?\n')
    if Heart_Disease == 'no' or Heart_Disease == 'No' or Heart_Disease == 'NO':
        pass
    else:
        list_dis.append('Heart Disease,')

    # High Uric Acid
    High_Uric_Acid = input('Do you suffer from High Uric Acid?\n')
    if High_Uric_Acid == 'no' or High_Uric_Acid == 'No' or High_Uric_Acid == 'NO':
        pass
    else:
        list_dis.append('High Uric Acid,')

    # Obesity
    Obesity = input('Do you suffer from Obesity?\n')
    if Obesity == 'no' or Obesity == 'No' or Obesity == 'NO':
        pass
    else:
        list_dis.append('Obesity,')

    print('\nDiseases:', list_dis)
    dis = ''
    for i in list_dis:
        dis = dis + i

    sql2 = "Create Table if not exists details (Name char(10) PRIMARY KEY, Age INT, DOB varchar(10), Gender char(5), Nationality char(15), Diseases varchar(100))"
    cur.execute(sql2)

    print('*******************************')
    for i in range(1):
        name = input('Enter name:')
        age = int(input('Enter age:'))
        dob = input('Enter DOB DD/MM/YYYY')
        gender = input('Enter gender M-Male/ F-Female/ O-Other:')
        nationality = input('Enter Nationality')
        sql4 = "Insert ignore into details values('{}',{},'{}','{}','{}','{}')".format(name, age, dob, gender, nationality, dis)
        cur.execute(sql4)
        print('*******************************')
        db.commit()

def recipe():
    print('*******************************')
    print('The recipes have successfully uploaded to your computer!')
    print('*******************************')
    
    sql1 = 'use info'
    cur.execute(sql1)

    sql2 = 'Create Table if not exists recipes( SERIAL_NO INT PRIMARY KEY, RECIPE_NAME CHAR(50), INGREDIENTS VARCHAR(1000), RECIPE_LINK varchar(1000), COOKING_TIME VARCHAR (50), NUMBER_SERVINGS INT, NOT_SUITABLE_FOR CHAR(50))'
    cur.execute(sql2)

    # 1
    SERIAL_NO = 1
    RECIPE_NAME = 'Oatmeal With Peanut Butter and Banana '
    INGREDIENTS = 'Banana, Peanut Butter, Honey, Oats, Chocolate Chips'
    RECIPE_LINK = 'https://www.healthy-liv.com/4-ingredient-peanut-butter-banana-oatmeal-cookies/'
    COOKING_TIME = '20 minutes'
    NUMBER_SERVINGS = 3
    NOT_SUITABLE_FOR = 'Diabetes'
    sql3 = "Insert ignore into RECIPES values({},'{}','{}','{}','{}',{},'{}')".format(SERIAL_NO, RECIPE_NAME, INGREDIENTS, RECIPE_LINK, COOKING_TIME, NUMBER_SERVINGS, NOT_SUITABLE_FOR)
    cur.execute(sql3)
    db.commit()

    # 2
    SERIAL_NO = 2
    RECIPE_NAME = 'Avocado Toast and Egg'
    INGREDIENTS = 'Bread, Avocado, Eggs'
    RECIPE_LINK = 'https://avocadosfrommexico.com/recipe/breakfasts/avocado-egg-toast/'
    COOKING_TIME = '10 minutes'
    NUMBER_SERVINGS = 1
    NOT_SUITABLE_FOR = 'Diabetes'
    sql6 = "Insert ignore into RECIPES values({},'{}','{}','{}','{}',{},'{}')".format(SERIAL_NO, RECIPE_NAME, INGREDIENTS, RECIPE_LINK, COOKING_TIME, NUMBER_SERVINGS, NOT_SUITABLE_FOR)
    cur.execute(sql6)
    db.commit()

    # 3
    SERIAL_NO = 3
    RECIPE_NAME = 'Sun Butter, Banana & Chia Seed Toast'
    INGREDIENTS = 'Bread, Butter, Banana, Chia Seeds'
    RECIPE_LINK = 'https://theskinnyfork.com/blog/sunbutter-toast'
    COOKING_TIME = '20 minutes'
    NUMBER_SERVINGS = 1
    NOT_SUITABLE_FOR = ''
    sql7 = "Insert ignore into RECIPES values({},'{}','{}','{}','{}',{},'{}')".format(SERIAL_NO, RECIPE_NAME, INGREDIENTS, RECIPE_LINK, COOKING_TIME, NUMBER_SERVINGS, NOT_SUITABLE_FOR)
    cur.execute(sql7)
    db.commit()

    # 4
    SERIAL_NO = 4
    RECIPE_NAME = 'Berry Yogurt Smoothie'
    INGREDIENTS = 'Blueberries, Blackberries, Yogurt, Milk, Banana'
    RECIPE_LINK = 'https://chefsavvy.com/healthy-berry-yogurt-smoothie/'
    COOKING_TIME = '25 minutes'
    NUMBER_SERVINGS = 1
    NOT_SUITABLE_FOR = 'Cholesterol'
    sql8 = "Insert ignore into RECIPES values({},'{}','{}','{}','{}',{},'{}')".format(SERIAL_NO, RECIPE_NAME, INGREDIENTS, RECIPE_LINK, COOKING_TIME, NUMBER_SERVINGS, NOT_SUITABLE_FOR)
    cur.execute(sql8)
    db.commit()

    # 5
    SERIAL_NO = 5
    RECIPE_NAME = 'Honey Lime Quinoa Fruit Salad'
    INGREDIENTS = 'Quinoa, Strawberries, Blackberries, Blueberries, Mango, Honey, Lime'
    RECIPE_LINK = 'https://therecipecritic.com/honey-lime-quinoa-fruit-salad/'
    COOKING_TIME = '30 minutes'
    NUMBER_SERVINGS = 2
    NOT_SUITABLE_FOR = 'Diabetes'
    sql9 = "Insert ignore into RECIPES values({},'{}','{}','{}','{}',{},'{}')".format(SERIAL_NO, RECIPE_NAME, INGREDIENTS, RECIPE_LINK, COOKING_TIME, NUMBER_SERVINGS, NOT_SUITABLE_FOR)
    cur.execute(sql9)
    db.commit()

    # 6
    SERIAL_NO = 6
    RECIPE_NAME = 'Skinny Spiced Coconut Yogurt Quinoa Muffins'
    INGREDIENTS = 'Eggs, Banana, Yogurt, Maple Syrup, Sugar, Flour, Quinoa'
    RECIPE_LINK = 'https://www.simplyquinoa.com/skinny-spiced-coconut-yogurt-quinoa-muffins/'
    COOKING_TIME = '30 minutes'
    NUMBER_SERVINGS = 3
    NOT_SUITABLE_FOR = ''
    sql10 = "Insert ignore into RECIPES values({},'{}','{}','{}','{}',{},'{}')".format(SERIAL_NO, RECIPE_NAME, INGREDIENTS, RECIPE_LINK, COOKING_TIME, NUMBER_SERVINGS, NOT_SUITABLE_FOR)
    cur.execute(sql10)
    db.commit()

    # 7
    SERIAL_NO = 7
    RECIPE_NAME = 'Roasted Cauliflower Tacos'
    INGREDIENTS = 'Oil, Lime, Honey, Cauliflower, Tortillas'
    RECIPE_LINK = 'https://minimalistbaker.com/roasted-cauliflower-tacos-with-chipotle-romesco/'
    COOKING_TIME = '20 minutes'
    NUMBER_SERVINGS = 3
    NOT_SUITABLE_FOR = 'High Blood Pressure'
    sql11 = "Insert ignore into RECIPES values({},'{}','{}','{}','{}',{},'{}')".format(SERIAL_NO, RECIPE_NAME, INGREDIENTS, RECIPE_LINK, COOKING_TIME, NUMBER_SERVINGS, NOT_SUITABLE_FOR)
    cur.execute(sql11)
    db.commit()

    # 8
    SERIAL_NO = 8
    RECIPE_NAME = 'Shaved Carrot and Radish Salad'
    INGREDIENTS = 'Oranges, Lime, Honey, Oil, Carrots, Radishes'
    RECIPE_LINK = 'https://www.goodhousekeeping.com/food-recipes/healthy/a30729726/shaved-carrot-salad-recipe/'
    COOKING_TIME = '25 minutes'
    NUMBER_SERVINGS = 6
    NOT_SUITABLE_FOR = 'Obesity'
    sql12 = "Insert ignore into RECIPES values({},'{}','{}','{}','{}',{},'{}')".format(SERIAL_NO, RECIPE_NAME, INGREDIENTS, RECIPE_LINK, COOKING_TIME, NUMBER_SERVINGS, NOT_SUITABLE_FOR)
    cur.execute(sql12)
    db.commit()

    # 9
    SERIAL_NO = 9
    RECIPE_NAME = 'Steak Sandwich with Arugula'
    INGREDIENTS = 'Onions, Lime, Vinegar, Steak, Oil'
    RECIPE_LINK = 'https://www.goodhousekeeping.com/food-recipes/a37223559/steak-sandwich-recipe/'
    COOKING_TIME = '30 minutes'
    NUMBER_SERVINGS = 4
    NOT_SUITABLE_FOR = 'Cholesterol, Heart Disease'
    sql13 = "Insert ignore into RECIPES values({},'{}','{}','{}','{}',{},'{}')".format(SERIAL_NO, RECIPE_NAME, INGREDIENTS, RECIPE_LINK, COOKING_TIME, NUMBER_SERVINGS, NOT_SUITABLE_FOR)
    cur.execute(sql13)
    db.commit()

    # 10
    SERIAL_NO = 10
    RECIPE_NAME = 'Instant Pot Beef Curry'
    INGREDIENTS = 'Oil, Onions, Beef, Milk'
    RECIPE_LINK = 'https://www.goodhousekeeping.com/food-recipes/a38867914/instant-pot-beef-curry-recipe/'
    COOKING_TIME = '45 minutes'
    NUMBER_SERVINGS = 6
    NOT_SUITABLE_FOR = 'Obesity, High Blood Pressure'
    sql14 = "Insert ignore into RECIPES values({},'{}','{}','{}','{}',{},'{}')".format(SERIAL_NO, RECIPE_NAME, INGREDIENTS, RECIPE_LINK, COOKING_TIME, NUMBER_SERVINGS, NOT_SUITABLE_FOR)
    cur.execute(sql14)
    db.commit()

    # 11
    SERIAL_NO = 11
    RECIPE_NAME = 'Salmon Niçoise Salad'
    INGREDIENTS = 'Oil, Lime, Lettuce, Potatoes, Green Beans, Eggs, Salmon'
    RECIPE_LINK = 'https://www.goodhousekeeping.com/food-recipes/a36558853/salmon-nicoise-salad-recipe/'
    COOKING_TIME = '20 minutes'
    NUMBER_SERVINGS = 4
    NOT_SUITABLE_FOR = 'Cholesterol'
    sql15 = "Insert ignore into RECIPES values({},'{}','{}','{}','{}',{},'{}')".format(SERIAL_NO, RECIPE_NAME, INGREDIENTS, RECIPE_LINK, COOKING_TIME, NUMBER_SERVINGS, NOT_SUITABLE_FOR)
    cur.execute(sql15)
    db.commit()

    # 12
    SERIAL_NO = 12
    RECIPE_NAME = 'Veggie & Hummus Sandwich'
    INGREDIENTS = 'Bread, Hummus, Avocado, Lettuce, Cucumber, Carrots'
    RECIPE_LINK = 'https://www.eatingwell.com/recipe/259817/veggie-hummus-sandwich/'
    COOKING_TIME = '20 minutes'
    NUMBER_SERVINGS = 1
    NOT_SUITABLE_FOR = ''
    sql16 = "Insert ignore into RECIPES values({},'{}','{}','{}','{}',{},'{}')".format(SERIAL_NO, RECIPE_NAME, INGREDIENTS, RECIPE_LINK, COOKING_TIME, NUMBER_SERVINGS, NOT_SUITABLE_FOR)
    cur.execute(sql16)
    db.commit()

    # 13
    SERIAL_NO = 13
    RECIPE_NAME = 'Avocado sweet potato tacos'
    INGREDIENTS = 'Potatoes, Oil, Tortillas, Lime, Yogurt, Avocado, Garlic'
    RECIPE_LINK = 'https://www.loveandlemons.com/avocado-sweet-potato-tacos/'
    COOKING_TIME = '30 minutes'
    NUMBER_SERVINGS = 3
    NOT_SUITABLE_FOR = ''
    sql17 = "Insert ignore into RECIPES values({},'{}','{}','{}','{}',{},'{}')".format(SERIAL_NO, RECIPE_NAME, INGREDIENTS, RECIPE_LINK, COOKING_TIME, NUMBER_SERVINGS, NOT_SUITABLE_FOR)
    cur.execute(sql17)
    db.commit()

    # 14
    SERIAL_NO = 14
    RECIPE_NAME = 'Honey mustard chicken salad'
    INGREDIENTS = 'Oil, Honey, Vinegar, Onions, Chicken, Lettuce, Strawberries, Avocado, Corn'
    RECIPE_LINK = 'https://damndelicious.net/2019/04/01/honey-mustard-chicken-salad/'
    COOKING_TIME = '2 hours'
    NUMBER_SERVINGS = 4
    NOT_SUITABLE_FOR = 'Heart Disease, High Blood Pressure'
    sql18 = "Insert ignore into RECIPES values({},'{}','{}','{}','{}',{},'{}')".format(SERIAL_NO, RECIPE_NAME, INGREDIENTS, RECIPE_LINK, COOKING_TIME, NUMBER_SERVINGS, NOT_SUITABLE_FOR)
    cur.execute(sql18)
    db.commit()

    # 15
    SERIAL_NO = 15
    RECIPE_NAME = 'Chicken pot pie soup'
    INGREDIENTS = 'Butter, Onions, Carrots, Garlic, Potatoes, Flour, Milk, Chicken, Corn'
    RECIPE_LINK = 'https://www.twopeasandtheirpod.com/chicken-pot-pie-soup/'
    COOKING_TIME = '1 hour'
    NUMBER_SERVINGS = 4
    NOT_SUITABLE_FOR = 'High Blood Pressure'
    sql19 = "Insert ignore into RECIPES values({},'{}','{}','{}','{}',{},'{}')".format(SERIAL_NO, RECIPE_NAME, INGREDIENTS, RECIPE_LINK, COOKING_TIME, NUMBER_SERVINGS, NOT_SUITABLE_FOR)
    cur.execute(sql19)
    db.commit()

    # 16
    SERIAL_NO = 16
    RECIPE_NAME = 'Chili Lime Shrimp'
    INGREDIENTS = 'Shrimp, Lime, Oil, Garlic, Lime'
    RECIPE_LINK = 'https://www.delish.com/cooking/recipe-ideas/a22535146/best-chili-lime-shrimp-recipe/'
    COOKING_TIME = '50 minutes'
    NUMBER_SERVINGS = 4
    NOT_SUITABLE_FOR = ''
    sql20 = "Insert ignore into RECIPES values({},'{}','{}','{}','{}',{},'{}')".format(SERIAL_NO, RECIPE_NAME, INGREDIENTS, RECIPE_LINK, COOKING_TIME, NUMBER_SERVINGS, NOT_SUITABLE_FOR)
    cur.execute(sql20)
    db.commit()

    # 17
    SERIAL_NO = 17
    RECIPE_NAME = 'Mozzarella, Basil & Zucchini Frittata'
    INGREDIENTS = 'Oil, Onions, Zucchini, Eggs, Tomatoes'
    RECIPE_LINK = 'https://www.eatingwell.com/recipe/251004/mozzarella-basil-zucchini-frittata/'
    COOKING_TIME = '40 minutes'
    NUMBER_SERVINGS = 1
    NOT_SUITABLE_FOR = ''
    sql20 = "Insert ignore into RECIPES values({},'{}','{}','{}','{}',{},'{}')".format(SERIAL_NO, RECIPE_NAME, INGREDIENTS, RECIPE_LINK, COOKING_TIME, NUMBER_SERVINGS, NOT_SUITABLE_FOR)
    cur.execute(sql20)
    db.commit()

def custom():
    print('*******************************')
    name = input('Enter name: ')
    list_dis = []
    sql5 = 'Select diseases from details where name=%s'
    cur.execute(sql5, (name,))
    x = cur.fetchall()
    x = x[0][0]
    b = str(x)
    a = b.split(',')
    for i in a:
        list_dis.append(i)
    
    suitable = []
    sql6 = 'Select serial_no, not_suitable_for from recipes'
    cur.execute(sql6)
    x = cur.fetchall()
    for i in x:
        c = i[1]
        b = str(c)
        a = b.split(',')
        
        if a not in list_dis:
            suitable.append(i[0])

    sql1 = 'use info'
    cur.execute(sql1)

    c = -2
    sql2 = "Create Table if not exists " + name + " (Date int, Meal char(50), SERIAL_NO INT)"
    z = int(input('Enter current date: '))
    print('*******************************')
    cur.execute(sql2)

    lim = z + 5
    while z < lim:
        for i in range(15):
            a = random.choice(suitable)
            if i % 3 == 0:
                meal = 'Breakfast'
            if i % 3 == 1:
                meal = 'Lunch'
            if i % 3 == 2:
                meal = 'Dinner'
            sql4 = "Insert ignore into " + name + " values({},'{}',{})".format(z, meal, a)
            cur.execute(sql4)
            db.commit()

            if c % 3 == 0:
                z += 1
            c += 1

    print('Your customised diet plan:')
    sql3 = 'Select Date, Meal, recipes.SERIAL_NO, RECIPE_NAME, INGREDIENTS, RECIPE_LINK, COOKING_TIME, NUMBER_SERVINGS from ' + name + ', recipes where ' + name + '.SERIAL_NO = recipes.SERIAL_NO ORDER BY DATE'
    cur.execute(sql3)
    x = cur.fetchall()
    print(tabulate(x, headers=['Date', 'Meal', 'RecipeCode', 'RecipeName', 'Ingredients', 'Link', 'Cooking_time', 'Number_of_Servings'], tablefmt='psql', showindex=False))
    print('*******************************')

def GrocList():
    print('*******************************')
    name = input('Enter name: ')
    ingred = []
    sql4 = 'Select INGREDIENTS from ' + name + ', recipes where ' + name + '.SERIAL_NO = recipes.SERIAL_NO'
    cur.execute(sql4)
    x = cur.fetchall()

    for j in x:
        c = j[0]
        b = str(c)
        a = b.split(',')
        for i in a:
            if i not in ingred:
                ingred.append(i)
    
    print('Ingredients required:')
    for k in sorted(ingred):
        print(k)

    have = []
    nothave = []
    print('*******************************')
    print('\nTime to prepare your Grocery List!')
    print('*******************************')
    print('\nDo you have the following?\nEnter n for No or y for Yes\n')
    
    for j in ingred:
        print(j)
        ans = input('Enter y or n:\n')
        if ans == 'y':
            have.append(j)
        else:
            nothave.append(j)

    print('*******************************')
    print('Shopping list is:', sorted(nothave))

def display():
    print('*******************************')
    print('To go to recipe link:')
    ingred = []
    n = int(input('Enter the recipe code of the recipe you would like to find: '))
    sql5 = 'Select recipe_link from recipes where SERIAL_NO = %s'
    cur.execute(sql5, (n,))
    x = cur.fetchall()
    url = x[0][0]
    new = 2
    webbrowser.open(url, new=new)
    print('*******************************')

while True:
    print('*******************************')
    print('Enter 1 to add your details')
    print('Enter 2 to upload recipe details to your computer')
    print('Enter 3 to create your custom meal plan')
    print('Enter 4 to create your grocery list')
    print('Enter 5 to go to recipe link')
    print('*******************************')
    l = input('\n\nEnter your choice: ')
    
    if l == '1':
        dets()
        print('\nThank you for adding your details\n')
    elif l == '2':
        recipe()
    elif l == '3':
        custom()
    elif l == '4':
        GrocList()
    elif l == '5':
        name = input('Enter name: ')
        sql3 = 'Select Date, Meal, recipes.SERIAL_NO, RECIPE_NAME, INGREDIENTS, RECIPE_LINK, COOKING_TIME, NUMBER_SERVINGS from ' + name + ', recipes where ' + name + '.SERIAL_NO = recipes.SERIAL_NO ORDER BY DATE'
        cur.execute(sql3)
        x = cur.fetchall()
        print(tabulate(x, headers=['Date', 'Meal', 'RecipeCode', 'RecipeName', 'Ingredients', 'Link', 'Cooking_time', 'Number_of_Servings'], tablefmt='psql', showindex=False))
        
        while True:
            display() 
            ch = input('\nWould you like to look at another recipe?')
            if ch == 'No' or ch == 'no' or ch == 'NO':
                break
    else:
        print('Invalid Choice')

    ch1 = input('\n\nWould you like to go back to the menu?')
    if ch1 == 'No' or ch1 == 'no' or ch1 == 'NO':
        print('*******************************')
        break



