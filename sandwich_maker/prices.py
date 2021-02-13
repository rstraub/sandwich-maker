itemPrices = {
    "wheat": 1.00,
    "white": 0.75,
    "sourdough": 1.00,
    "chicken": 1.00,
    "turkey": 1.25,
    "ham": 0.5,
    "tofu": 0.5,
    "cheddar": 0.25,
    "swiss": 0.5,
    "mozzarella": 0.25,
    "mayo": 0.1,
    "mustard": 0.1,
    "lettuce": 0.25,
    "tomato": 0.25,
}


def calculateSandwichPrice(selectedItems):
    return sum(map(getItemPrice, selectedItems))


def getItemPrice(item):
    return itemPrices.get(item, 0.0)
