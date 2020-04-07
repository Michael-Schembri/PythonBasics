# basic function
def helloFunction(name = "World"):
    print("Hello {0}".format(name))

helloFunction()
helloFunction("Michael")

# arbitrary args
def helloToAll(*texts):
    for text in texts:
        helloFunction(text)

helloToAll("jack", "jill", "bob", "bill")
# kwargs
def stockTake(bananas = 0, apples = 0, tomatoes = 0):
    if (bananas > 0):
        if (bananas == 1): print("One banana left.")
        else:
            print("You have %d bananas" % bananas)
    else:
        print("There are no bananas left.")
    if (apples > 0):
        print("One apple left.") if (apples == 1) else print("You have %d apples" % apples)
    else:
        print("There are no apples left.")
    if (tomatoes > 0):
        print("One tomato left.") if (tomatoes == 1) else print("You have %d tomatoes" % tomatoes)
    else:
        print("There are no tomatoes left.")
#stockTake(tomatoes = 8, bananas = 6)
# arbitrary kwargs
def stockTakeA(**Fruit):
    # init parameters in case the item is not found in dictionary
    parmTomatoes = 0
    if ("tomatoes" in Fruit):
        parmTomatoes = Fruit["tomatoes"]
    parmBananas = 0
    if ("bananas" in Fruit):
        parmBananas = Fruit["bananas"]
    parmApples = 0
    if ("apples" in Fruit):
        parmApples = Fruit["apples"]
    # without this construction, you could end up with a function being called with a non existent key in the dictionary resulting in an error
    # does not fall back to default values as it crashes during function call
    stockTake(bananas = parmBananas, tomatoes = parmTomatoes, apples = parmApples)

stockTakeA(bananas = 5, tomatoes = 2)

# recursion and returns
def factorial(n = 0):
    if (n == 0):
        return 1  
    else:
        return n * factorial(n-1)

print(factorial(3))
        

