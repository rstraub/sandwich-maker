#! python3

import pyinputplus as pyip

print('Welcome! Please tell me what sandwich you would like')
# get bread type (wheat, white, sourdough)
breadTypes = ('wheat', 'white', 'sourdough')
breadType = pyip.inputMenu(breadTypes, prompt='What type of bread would you like?: \n')

print(breadType)

# get protein type (chicken, turkey, ham, tofu)

# want cheese?
# if so which cheese? (cheddar, swiss, mozarella)
# Want other toppings? (mayo, mustard, lettuce, tomato)
# How many do you want?

# Show the total price