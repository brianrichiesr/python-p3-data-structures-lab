from statistics import mean

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    emoji =  "🌶"
    for food in spicy_foods:
        fstr = ""
        num = int(food["heat_level"])
        for i in range(0, num):
            fstr += emoji
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {fstr}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    spiciest = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest)

def get_average_heat_level(spicy_foods):
    levels = [food["heat_level"] for food in spicy_foods]
    return mean(levels)

def create_spicy_food(spicy_foods, spicy_food):
    return [*spicy_foods, spicy_food]
