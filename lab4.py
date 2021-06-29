from Program4 import Menu
from lab2 import NBA_players


import numpy as np 
def fibonacciFinder (max):
    i = 0
    j = 1
    k = 0
    while i < max
    print k



Area = triangleArea(2,4)

n = 5
m = 5 
areaList = []
for b in range(0,n)
    for h in range(o,m)
     areaList.append(triangleArea(b,h))

Menu = {"Burgers": 12.99, "Fries": 3.99, "Shakes": 1.50}
def foodSum(Dict, item1, item2):
    sum = Dict[item1] + Dict[item2]
    print("the total price of your order of" + item1 + "and" + item2 + "is $" + str(sum))
    sum *= 1.0925
    print("with tax that will be $" + str(sum))

def foodSum2 (Dict, *args):
    sum = 0 
    text = 'the total price of your order of '
    for keys in args:
        if keys in Dict:
        sum += Dict[keys]
        text += keys = " "
    text += "is $" + str(sum)
    print(text)

foodSum2(Menu, "Burgers", "Fries", "Fries", "SHakes", "Burrito", "Shakes")
