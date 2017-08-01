# dictionary
i = {
	"eggs": 3,
	"water (cups)": "1/3",
	"hot red pepper sauce (cups)": 1,
	"self-rising flour (cups)": 2,
	"pepper (teaspoon)": 1,
	"chicken": 1,
	"oil": 1,
	"salt (cup)": 1,
	"black pepper": "1/4",
	"garlic powder (cups)": "1/4"
}

#list
d = ["In a medium size bowl, beat the eggs with the water. ", 
	"Add enough hot sauce so the egg mixture is bright orange. ",
	"In another bowl, combine the flour and pepper. ",
	"Season the chicken with the house seasoning. ",
	"Dip the seasoned chicken in the egg, ",
	"and then coat well in the flour mixture.",
	"Heat the oil to 350 degrees F in a deep pot. ",
	"Do not fill the pot more than 1/2 full with oil.",
	"Fry the chicken in the oil until brown and crisp. ",
	"Dark meat takes longer then white meat. ",
	"It should take dark meat about 13 to 14 minutes, ",
	"white meat around 8 to 10 minutes."]

print("\nSouthern Fried Chicken:\n")

for num in i:
	print(str(i[num]) + " " + num)

print("\n")

for num in range(0, len(d)):
	print(d[num])
