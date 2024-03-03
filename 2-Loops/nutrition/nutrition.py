# prompt user for fruit
def fruit_calories_dict(fruit_name):
    fruit_calories = {
        "Apple": "130",
        "Avocado": "50",
        "Banana": "110",
        "Cantaloupe": "50",
        "Grapefruit": "60",
        "Grapes": "90",
        "Honeydew Melon": "50",
        "Kiwifruit": "90",
        "Lemon": "15",
        "Lime": "20",
        "Nectarine": "60",
        "Orange": "80",
        "Peach": "60",
        "Pear": "100",
        "Pineapple": "50",
        "Plums": "70",
        "Strawberries": "50",
        "Sweet Cherries": "100",
        "Tangerine": "50",
        "Watermelon": "80",
    }

    # make capital to match dict key
    fruit_name = fruit_name.title()

    for fruit_name in fruit_calories:
        return fruit_calories[fruit_name]
    else:
        return None


def main():
    while True:
        calorie_checker = input("Enter fruit to check calories: ")
        fruit_calories = fruit_calories_dict(calorie_checker)
        if fruit_calories is not None:
            print("Calories:", fruit_calories)
        else:
            print("Enter a valid fruit")

        try_again = input("Check another fruit? (yes/no): ")
        if try_again.lower() != "yes":
            break


main()
