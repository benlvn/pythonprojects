import sys

CALORIE_DATA = {
    "apple": 105,
    "banana": 105,
    "blueberry": 103,
    "kiwi": 93,
    "orange": 90,
    "pineapple": 103,
    "raspberry": 96,
    "watermellon": 110
}

def get_calories(food):
    if food in CALORIE_DATA:
        return CALORIE_DATA[food]
    else:
        return "Error food not found: {}".format(food)

if __name__ == "__main__":
    print(get_calories(sys.argv[1]))
