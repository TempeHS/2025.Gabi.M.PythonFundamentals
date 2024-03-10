# Function to display total cost
# Initialize total cost
total_cost = 0.0


def display_total_cost(total_cost):
    print(f"TOTAL: ${total_cost:.2f}")


def cumulative_cost(item_cost):
    global total_cost
    total_cost += item_cost
    # print(f"Inside cum-cost: Item-> {item_cost}, Total -> {total_cost}")
    return total_cost


# Function to process user input
def process_order(item):
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }

    # total_cost += menu[item]
    item = item.title()  # Convert input to title case
    if item in menu:
        display_total_cost(cumulative_cost(menu[item]))
    else:
        main()


# Main function
def main():
    print("Please enter your order (one item per line):")

    try:
        while True:
            item = input().strip()
            process_order(item)
    except EOFError:
        print("Thank you for your order!")


if __name__ == "__main__":
    main()
