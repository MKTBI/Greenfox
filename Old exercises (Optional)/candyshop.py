shop_items = ["Cupcake", 2, "Brownie", False]

# Accidentally we added "2" and "false" to the list
# Your task is to change from "2" to "Croissant" and change from "false" to "Ice cream"
# No, don't just remove the items :)
# Create a function called repair_sweets() which takes the list as a parameter
# Expected output: "Cupcake", "Croissant", "Brownie", "Ice cream"

def repair_sweets(item:list) -> list:
    for i in item:
        if i == 2:
            shop_items[1] = "Croissant"
        if i == False:
            shop_items[-1] = "Ice cream"
    return item
            
#not proud of this answer to be honest :)

print(repair_sweets(shop_items))