fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        fruit = "Fruit"
    print(fruit + " pie")


make_pie(4)
