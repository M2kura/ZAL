"""
Homer's fridge
Course: B0B36ZAL
"""

#nasledujici kod nijak nemodifikujte!
class Food:
    def __init__(self, name, expiration):
        self.name = name
        self.expiration = expiration
#predesly kod nijak nemodifikujte!

def openFridge(fridge):
    print("Following items are in Homer's fridge:")
    for food in fridge:
        print("{0} (expires in: {1} days)".format(
            str(food.name), str(food.expiration))
        )

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# fridge = [Food("beer", 4), Food("steak", 1), Food("hamburger", 1), Food("donut", 3)]
# openFridge(fridge)


"""
Task #1
"""

def maxExpirationDay(fridge: list[Food]):
    maxExpo = 0
    if len(fridge) == 0:
        return -1
    else: 
        for food in fridge:
            if food.expiration > maxExpo:
                maxExpo = food.expiration
        return maxExpo
    

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(maxExpirationDay(fridge))
# The command should print 4


"""
Task #2
"""

def histogramOfExpirations(fridge):
    histogram = []
    for i in range (0, maxExpirationDay(fridge)+1):
        count = 0
        for food in fridge:
            if food.expiration == i:
                count += 1
        histogram.append(count)
    return histogram


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(histogramOfExpirations(fridge))
# The command should print [0, 2, 0, 1, 1]


"""
Task #3
"""
def cumulativeSum(histogram):
    cumSum = [histogram[0]]
    for i in range(1, len(histogram)):
        cumSum.append(cumSum[i-1] + histogram[i])
    return cumSum


# test vypisu - pri odevzdani smazte, nebo zakomentujte
# print(cumulativeSum([0, 2, 0, 1, 1]))
# The command should print [0, 2, 2, 3, 4]


"""
Task #4
"""
def sortFoodInFridge(fridge):
    sortedFridge = []
    for i in range (0, len(fridge)):
        sortedFridge.append(0)
    cumSum = cumulativeSum(histogramOfExpirations(fridge))
    for food in fridge:
        exp = food.expiration
        cumSum[exp] = cumSum[exp] - 1
        poslnd = cumSum[exp]
        sortedFridge[poslnd] = food
    return sortedFridge

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(sortFoodInFridge(fridge))
# The command should print
# Following items are in Homer's fridge:
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)


"""
Task #5
"""

def reverseFridge(fridge):
    revFridge = []
    for food in fridge:
        revFridge.insert(0, food)
    return revFridge

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(reverseFridge(fridge))
# The command should print
# Following items are in Homer's fridge:
# donut (expires in: 3 days)
# hamburger (expires in: 1 days)
# steak (expires in: 1 days)
# beer (expires in: 4 days)

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(sortFoodInFridge(reverseFridge(fridge)))
# The command should print
# Following items are in Homer's fridge:
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# beer (expires in: 4 days)


"""
Task #6
"""
def eatFood(name, fridge):
    gone = None
    for food in fridge:
        if food.name == name:
            if gone is not None:
                if gone.expiration > food.expiration:
                    gone = food
                continue
            else:
                gone = food
    fridge.remove(gone)
    return fridge

# test vypisu - pri odevzdani smazte, nebo zakomentujte
# openFridge(
#     eatFood("donut",
#         [Food("beer", 4), Food("steak", 1), Food("hamburger", 1),
#         Food("donut", 3), Food("donut", 1), Food("donut", 6)]
#     ))
# The command should print
# Following items are in Homer's fridge:
# beer (expires in: 4 days)
# steak (expires in: 1 days)
# hamburger (expires in: 1 days)
# donut (expires in: 3 days)
# donut (expires in: 6 days)
