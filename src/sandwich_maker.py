#! python3

import pyinputplus as pyip

print("Welcome! Please tell me what sandwich you would like")
# get bread type (wheat, white, sourdough)
availableBreadTypes = ("wheat", "white", "sourdough")
selectedBreadType = pyip.inputMenu(
    availableBreadTypes, prompt="What type of bread would you like?: \n"
)

availableProteinTypes = ("chicken", "turkey", "ham", "tofu")
selectedProteinType = pyip.inputMenu(
    availableProteinTypes, prompt="What type of protein would you like?: \n"
)

withCheese = pyip.inputYesNo(prompt="Would you like cheese with that? \n") == "yes"

availableCheeses = ("cheddar", "Swiss", "mozzarella")
selectedCheese = None
if withCheese:
    selectedCheese = pyip.inputMenu(
        availableCheeses, prompt="What type of cheese would you like?: \n"
    )

availableToppings = ("mayo", "mustard", "lettuce", "tomato")
selectedToppings = []  # TODO: saving the tougher one for last

print(
    selectedBreadType, selectedProteinType, withCheese, selectedCheese, selectedToppings
)

# get protein type (chicken, turkey, ham, tofu)

# want cheese?
# if so which cheese? (cheddar, swiss, mozarella)
# Want other toppings? (mayo, mustard, lettuce, tomato)
# How many do you want?

# Show the total price