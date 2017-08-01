import random

appetizer = ["potstickers", "crab-stuffed mushrooms", "bruschetta", "stuffed cherry peppers", "nachos"]
soup = ["hot and sour soup", "creamy chicken and wild rice soup", "chicken noodle soup", "minestrone", "baked potato soup", "french onion soup"]
salad = ["chicken caesar salad", "quinoa salad", "harvest salad", "couscous salad", "pasta salad", "potato salad"]
main_course = ["spaghetti", "chicken tikka masala", "lasagna", "spinach alfredo", "mac n' cheese", "tacos"]
dessert = ["cheesecake", "creme brulee", "tiramisu", "vanilla ice cream", "chocolate ice cream"]
drinks = ["sprite", "coke", "vintage wine", "beer", "sangria", "lemonade", "margarita"]

menu1 = random.choice(appetizer)
menu2 = random.choice(soup)
menu3 = random.choice(salad)
menu4 = random.choice(main_course)
menu5 = random.choice(dessert)
menu6 = random.choice(drinks)


print("")
print("Bon apple tea! Our appetizer, chosen by our gracious host ")
print("is " + menu1 + ", and will include " + menu6 + " as a fancy drink.")
print("Next, we'll start off with " + menu2 + ".")
print("The next course will include " + menu3 + ".")
print("The main course will be " + menu4 + ", if that's ok with you.")
print("Finally, for dessert, we'll be having " + menu5 + ".")
