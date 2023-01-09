# Create a function that prints the ingredient list of dictionaries to the console in the following format:
#
# +--------------------+---------------+----------+
# | Ingredient         | Needs cooling | In stock |
# +--------------------+---------------+----------+
# | vodka              | Yes           | 1        |
# | coffee_liqueur     | Yes           | -        |
# | fresh_cream        | Yes           | 1        |
# | captain_morgan_rum | Yes           | 2        |
# | mint_leaves        | No            | -        |
# +--------------------+---------------+----------+
#
# OPTIONAL:
# The frist columns should be automatically as wide as the longest key

ingredients = [
	{ "name": "vodka", "in_stock": 1, "needs_cooling": True },
	{ "name": "coffee_liqueur", "in_stock": 0, "needs_cooling": True },
	{ "name": "fresh_cream", "in_stock": 1, "needs_cooling": True },
	{ "name": "captain_morgan_rum", "in_stock": 2, "needs_cooling": True },
	{ "name": "mint_leaves", "in_stock": 0, "needs_cooling": False },
	{ "name": "sugar", "in_stock": 0, "needs_cooling": False },
	{ "name": "lime juice", "in_stock": 0, "needs_cooling": True },
	{ "name": "soda", "in_stock": 0, "needs_cooling": True }
]

def print_ingredient_list(ingredients):
    # Find the longest ingredient name
    max_name_len = max(len(ingredient['name']) for ingredient in ingredients)
    
    # Print the header row
    print("+" + "-"*(max_name_len+2) + "+---------------+----------+")
    print("| Ingredient" + " "*(max_name_len-9) + "| Needs cooling | In stock |")
    print("+" + "-"*(max_name_len+2) + "+---------------+----------+")
    
    # Print each ingredient
    for ingredient in ingredients:
        name = ingredient['name']
        cooling = "Yes" if ingredient['needs_cooling'] else "No"
        stock = ingredient['in_stock'] if ingredient['in_stock'] >= 0 else "-"
        print(f"| {name}{' '*(max_name_len-len(name))} | {cooling}           | {stock:8} |")
    
    # Print the footer row
    print("+" + "-"*(max_name_len+2) + "+---------------+----------+")

print_ingredient_list(ingredients)
