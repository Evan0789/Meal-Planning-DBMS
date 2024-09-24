import _sqlite3
from random import shuffle, choice

sql_file_path = 'menu.sql'

conn = _sqlite3.connect('menu.db')
cursor = conn.cursor()

with open(sql_file_path, 'r') as sql_file:
    sql_script = sql_file.read()

cursor.executescript(sql_script)
########################################################################################################################


'''Functions'''


def new_ingredient():
    item_name = input("Enter ingredient name: ").lower()
    item_source = input("Enter ingredient source: ").lower()
    cursor.execute("INSERT INTO INGREDIENTS (name, source) VALUES (?, ?)",
                   (item_name, item_source))


def new_meal():
    food_name = input("Enter food name: ").lower()
    food_side = input("Enter side(s) (separate with commas or leave empty for no sides): ").lower()
    if not food_side == '':
        cursor.execute("SELECT name FROM FOOD")
        meals = ''
        for i in cursor.fetchall():
            meals = meals + i[0]
        for i in food_side.split(','):
            j = i.strip()
            if not j in meals:
                op = input(f"{j} not found in table. Make a new side? (y/n): ")
                if op == 'y':
                    new_side(j)
                else:
                    print(f"{j} will not be added to the meal.")
                    food_side = food_side.replace(j, '')
    food_type = input("Enter food type (ie. breakfast, lunch, dinner. Separate with commas or leave empty): ").lower()
    food_ingredients = input("Enter ingredients (separate with commas or leave empty for no ingredients): ").lower()
    food_ingredients = food_ingredients.replace(', ', ',')
    cursor.execute("INSERT INTO FOOD (name, sides, meal_type) VALUES (?, ?, ?)",
                   (food_name, food_side, food_type))
    cursor.execute("INSERT INTO RECIPE (name, ingredients) VALUES (?, ?)",
                   (food_name, food_ingredients))


def new_side(side):
    food_ingredients = input("Enter ingredients (separate with commas or leave empty for no ingredients): ").lower()
    food_ingredients = food_ingredients.replace(', ', ',')
    cursor.execute("INSERT INTO FOOD (name) VALUES (?)",
                   (side,))
    cursor.execute("INSERT INTO RECIPE (name, ingredients) VALUES (?, ?)",
                   (side, food_ingredients))


def show_ingredients():
    cursor.execute("SELECT * FROM INGREDIENTS")
    for row in cursor.fetchall():
        print(row, sep='\n')


def show_meals():
    cursor.execute("SELECT * FROM FOOD")
    for row in cursor.fetchall():
        print(row, sep='\n')


def delete_ingredient():
    meal = input("Which ingredient would you like to delete?: ").lower()
    cursor.execute("DELETE FROM INGREDIENTS WHERE name = ?", (meal,))


def delete_meal():
    meal = input("Which meal would you like to delete?: ").lower()
    cursor.execute("DELETE FROM FOOD WHERE name = ?", (meal,))


def edit_ingredient():
    ingredient = input("Which ingredient would you like to edit?: ").lower()
    op = input("What would you like to edit?\n1: Name\n2: Source\nEnter your option: ")
    if op == '1':
        ingredient_name = input("Enter new name: ").lower()
        cursor.execute("UPDATE INGREDIENTS SET name = ? WHERE name = ?",
                       (ingredient_name, ingredient))
    elif op == '2':
        ingredient_source = input("Enter new source: ").lower()
        cursor.execute("UPDATE INGREDIENTS SET source = ? WHERE name = ?",
                       (ingredient_source, ingredient))


def edit_meal():
    meal = input('Which meal would you like to edit?: ').lower()
    op = input('What would you like to edit?\n1: Name\n2: Add Side\n3: Remove Side\n4: Meal Type\n5: Add Ingredient\n'
               '6: Remove Ingredient\n'
               'Enter your option: ')
    if op == '1':
        meal_name = input('Enter new name: ').lower()
        cursor.execute("UPDATE FOOD SET name = ? WHERE name = ?",
                       (meal_name, meal))
    elif op == '2':
        food_side = input('Enter new side: ').lower()
        cursor.execute("SELECT name FROM FOOD")
        meals = ''
        for i in cursor.fetchall():
            meals = meals + i[0]
        for i in food_side.split(','):
            j = i.strip()
            if not j in meals:
                op = input(f"{j} not found in table. Make a new side? (y/n): ")
                if op == 'y':
                    new_side(j)
                else:
                    print(f"{j} will not be added to the meal.")
                    food_side = food_side.replace(j, '')
        cursor.execute("SELECT sides FROM FOOD WHERE name = ?", (meal,))
        sides = ''.join(cursor.fetchone())
        sides = sides + f",{food_side}"
        cursor.execute("UPDATE FOOD SET sides = ? WHERE name = ?",(sides, meal))
    elif op == '3':
        food_side = input('Enter side to delete: ').lower()
        cursor.execute("SELECT sides FROM FOOD WHERE name = ?", (meal,))
        sides = ''.join(cursor.fetchone())
        sides = sides.replace(food_side, '')
        sides = sides.replace(',,',',')
        cursor.execute("UPDATE FOOD SET SIDES = ? WHERE name = ?",(sides, meal))
    elif op == '4':
        meal_type = input('Change Meal Type: ').lower()
        cursor.execute("UPDATE FOOD SET meal_type = ? WHERE name = ?",
                       (meal_type, meal))
    elif op == '5':
        meal_ingredient = input('Enter new ingredient: ').lower()
        cursor.execute("SELECT ingredients FROM RECIPE WHERE name = ?", meal)
        recipe = ''.join(cursor.fetchone())
        recipe = recipe + ',' + meal_ingredient
        cursor.execute("UPDATE RECIPE SET ingredients = ? WHERE name = ?", (recipe, meal))
    elif op == '6':
        meal_ingredient = input('Enter ingredient to remove: ').lower()
        cursor.execute("SELECT ingredients FROM RECIPE WHERE name = ?", meal)
        recipe = ''.join(cursor.fetchone())
        recipe = recipe.replace(meal_ingredient, '')
        recipe = recipe.replace(',,', ',')
        cursor.execute("UPDATE RECIPE SET ingredients = ? WHERE name = ?",(recipe, meal))


def get_recipe(meal):
    if meal == '':
        return ['']
    cursor.execute("SELECT ingredients FROM RECIPE WHERE name = ?", (meal,))
    recipe_row = cursor.fetchone()
    if recipe_row is not None:
        recipe = recipe_row[0]
        recipe_array = recipe.split(',')
        for i in range(len(recipe_array)):
            recipe_array[i] = recipe_array[i].strip()
        return recipe_array
    else:
        return []


def create_menu(days):
    breakfasts = []
    lunches = []
    dinners = []
    breakfast_sides = []
    lunch_sides = []
    dinner_sides = []

    '''get random lists of breakfasts, lunches, and dinners'''
    cursor.execute("SELECT name FROM FOOD WHERE meal_type = ?",('breakfast',))
    for i in cursor.fetchall():
        breakfasts.append(i[0])
        if len(breakfasts) == 7: break
    cursor.execute("SELECT name FROM FOOD WHERE meal_type = ?", ('lunch',))
    for i in cursor.fetchall():
        lunches.append(i[0])
        if len(lunches) == 7: break
    cursor.execute("SELECT name FROM FOOD WHERE meal_type = ?", ('dinner',))
    for i in cursor.fetchall():
        dinners.append(i[0])
        if len(dinners) == 7: break
    shuffle(breakfasts)
    shuffle(lunches)
    shuffle(dinners)

    '''get lists of sides for meals'''
    for i in breakfasts:
        cursor.execute("SELECT sides FROM FOOD WHERE name = ?", (i,))
        sides = cursor.fetchone()[0]
        if sides == '':
            breakfast_sides.append('')
        else:
            sides_array = sides.split(',')
            breakfast_sides.append(choice(sides_array))
    for i in lunches:
        cursor.execute("SELECT sides FROM FOOD WHERE name = ?", (i,))
        sides = cursor.fetchone()[0]
        if sides == '':
            lunch_sides.append('')
        else:
            sides_array = sides.split(',')
            lunch_sides.append(choice(sides_array))
    for i in dinners:
        cursor.execute("SELECT sides FROM FOOD WHERE name = ?", (i,))
        sides = cursor.fetchone()[0]
        if sides == '':
            dinner_sides.append('')
        else:
            sides_array = sides.split(',')
            dinner_sides.append(choice(sides_array))

    '''output menu'''
    while days < 1 or days > 7:
        days = int(input("How many days would you like for the menu to have? (enter number 1-7): "))
    print("")
    print(f"Here's a menu for the next {days} days:")
    print("=" * 156)
    for i in range(days):
        print("| Day {} | {:<25} {:<20} | {:<25} {:<20} | {:<25} {:<20} |".format(
            i+1, breakfasts[i], breakfast_sides[i], lunches[i], lunch_sides[i], dinners[i], dinner_sides[i]))
    print("=" * 156)

    '''make new menu or create shopping list'''
    print("What would you like to do?   1: Generate new menu    2: Create Shopping List    3: Exit")
    op = input("Enter your option: ")
    if op == '1': create_menu(days)
    elif op == '2': create_list(days, breakfasts, lunches, dinners, breakfast_sides, lunch_sides, dinner_sides)


def create_list(days, breakfasts, lunches, dinners, breakfast_sides, lunch_sides, dinner_sides):
    ingredients_array = []
    for i in range(days):
        ingredients_array.extend(get_recipe(breakfasts[i]))
        ingredients_array.extend(get_recipe(lunches[i]))
        ingredients_array.extend(get_recipe(dinners[i]))
        ingredients_array.extend(get_recipe(breakfast_sides[i]))
        ingredients_array.extend(get_recipe(lunch_sides[i]))
        ingredients_array.extend(get_recipe(dinner_sides[i]))
    ingredients_array = [string for string in ingredients_array if string != '']
    ingredients_array.sort()

    i = 0
    amount = 1
    print("===========================================\n"
          "|     Ingredients     | Amount |  Source  |\n"
          "===========================================")
    while i < len(ingredients_array) - 1:
        if ingredients_array[i] == ingredients_array[i + 1]:
            i += 1
            amount += 1
        else:
            cursor.execute("SELECT source FROM INGREDIENTS WHERE name = ?", (ingredients_array[i],))
            source = cursor.fetchone()[0]
            print("| {:<20}|   x{}   | {:<8} |".format(ingredients_array[i], amount, source))
            amount = 1
            i += 1
    cursor.execute("SELECT source FROM INGREDIENTS WHERE name = ?", (ingredients_array[i],))
    source = cursor.fetchone()[0]
    print("| {:<20}|   x{}   | {:<8} |".format(ingredients_array[i], amount, source))
    print("===========================================")


########################################################################################################################


'''Main Program'''
if __name__ == '__main__':
    exit_program = False
    print("Welcome!")
    while not exit_program:
        print("\n1: Manage Ingredient Table\n2: Manage Meal Table\n3: Create Menu\nq: quit program")
        option = input("Enter your option: ")

        if option == '1':
            back = False
            while not back:
                print("\n1: Add Ingredient\n2: Edit Ingredient\n3: Delete Ingredient\n4: Show All Ingredients\n"
                      "b: Go Back")
                option = input("enter your option: ")
                if option == '1': new_ingredient()
                elif option == '2': edit_ingredient()
                elif option == '3': delete_ingredient()
                elif option == '4': show_ingredients()
                elif option == 'b' or option == 'B' or option == 'q' or option == 'Q': back = True

        elif option == '2':
            back = False
            while not back:
                print("\n1: Add Meal\n2: Edit Meal\n3: Delete Meal\n4: Show All Meals\n5: Show Recipe\n"
                      "b: Go Back")
                option = input("enter your option: ")
                if option == '1': new_meal()
                elif option == '2': edit_meal()
                elif option == '3': delete_meal()
                elif option == '4': show_meals()
                elif option == '5':
                    for i in get_recipe(input('Enter meal: ').lower()): print(i)
                elif option == 'b' or option == 'B' or option == 'q' or option == 'Q': back = True

        elif option == '3': create_menu(-1)

        elif option == 'q' or option == 'Q': exit_program = True

########################################################################################################################

conn.commit()
conn.close()
