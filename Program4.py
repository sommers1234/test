import random as rand

Menu = {"Burgers": 12.99, "Fries": 3.99, "Shakes": 1.50}
def  foodSum(Dict,item1,item2):
    sum = Dict[item1] + Dict[item2]
    print("the total price of your order of" + item1 + "and" + item2 + "is $" + str(sum))
    sum*= 1.0925
    print("with tax that will be $" + str(sum))

foodSum(Menu, "Burgers", "Shakes")

#foodSum(Menu, "Burgers", "Shakes")

listPlayers = [1,2,3,4,5,6,7]
length = len(listPlayers)
for i in range(length):
    length = len(listPlayers)
    randomNumber = rand.randint(0,length)
    print(listPLayers.pop(randomNumber))
    print(listPlayers)

#append,extend,insert
#pop,remove,clear