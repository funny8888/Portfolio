# Requirements: List must be in alphabetical order
# 

# num = searching for num
# index = int(len(list))
# if num > list(index) --> search list(index+1) - list(end)
	# index += int(index/2)
# if num < list(index) --> search list(start) - list(index-1)
	# index -= int(index/2)
# if num == list(index) --> index == num

import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')

length = len(countries) -1

search_value = 'Czech Republic'
# search_value_letter = P
search_value_letter = search_value[0]
# for the final index to submit to the user
found_index = 0

# the first while loop
tf = True
index = (length)/2


while(tf):
	# used_index = countries[15]
	countries_index = countries[index]
	# gets the letter
	used_index = countries_index[0] 
	# check 2nd half
	# b is GREATER than a

	# search letter < current letter
	if (search_value_letter < used_index):
		index = int(index/2)
		if (index < 0):
			index = 0
	# search letter > current letter
	elif (search_value_letter > used_index):
		index += int(index/2)
		if (index > length):
			index = length -1
	# the first letter matches! does the second one match?
	else:
		# the word matches! index found
		num = True
		number = 1
		while(num):
			used_index = countries_index[number]
			if (countries[index] == search_value):
				found_index = index
				num = False
				tf=False
			elif (countries_index[number] > search_value[number]):
				index += 1
			else:
				index -= 1
print(found_index)
