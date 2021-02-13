#! python3

import pyinputplus as pyip

selectedItems = []

print("Welcome! Please tell me what sandwich you would like")
# get bread type (wheat, white, sourdough)
availableBreadTypes = ("wheat", "white", "sourdough")
selectedBreadType = pyip.inputMenu(
    availableBreadTypes, prompt="What type of bread would you like?: \n"
)
selectedItems.append(selectedBreadType)

availableProteinTypes = ("chicken", "turkey", "ham", "tofu")
selectedProteinType = pyip.inputMenu(
    availableProteinTypes, prompt="What type of protein would you like?: \n"
)
selectedItems.append(selectedProteinType)

withCheese = pyip.inputYesNo(prompt="Would you like cheese with that? \n") == "yes"

availableCheeses = ("cheddar", "Swiss", "mozzarella")
selectedCheese = None
if withCheese:
    selectedCheese = pyip.inputMenu(
        availableCheeses, prompt="What type of cheese would you like?: \n"
    )
    selectedItems.append(selectedCheese)

availableToppings = ("mayo", "mustard", "lettuce", "tomato")
selectedToppings = []
for topping in availableToppings:
    withTopping = (
        pyip.inputYesNo(prompt=f"Would you like {topping} with that?: \n") == "yes"
    )
    if withTopping:
        selectedToppings.append(topping)
        selectedItems.append(topping)

amountOfSandwiches = pyip.inputNum(
    prompt="How many sandwiches would you like? \n", min=1
)

totalPrice = 1.00
formattedItems = ", ".join(selectedItems)
result = f"""
Great! {amountOfSandwiches} sandwich(es) with {formattedItems} coming right up.
That will cost you ${totalPrice}.
"""
print(result)

# get protein type (chicken, turkey, ham, tofu)

# want cheese?
# if so which cheese? (cheddar, swiss, mozarella)
# Want other toppings? (mayo, mustard, lettuce, tomato)
# How many do you want?

# Show the total price