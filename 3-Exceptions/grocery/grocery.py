def main():
    print("Please enter your grocery items (one item per line):")

    # Create an empty dictionary to store grocery items and their counts
    grocery_items = {}

    # Prompt the user to input items until they press control-d
    try:
        while True:
            item = input().strip().title()
            if item in grocery_items:
                grocery_items[item] += 1
            else:
                grocery_items[item] = 1  # Initialize count to 1 for new item
    except EOFError:  # End of input detected
        pass

    # Print the grocery list in uppercase, sorted alphabetically by item
    print("\nYour Grocery List:")
    for item in sorted(grocery_items.keys()):  # Sort items alphabetically
        count = grocery_items[item]
        print(f"{count} {item.upper()}")  # Print count and item in uppercase


if __name__ == "__main__":
    main()
