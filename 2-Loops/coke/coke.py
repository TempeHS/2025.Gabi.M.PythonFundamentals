def main():
    accepted_coins = [5, 10, 25]

    coke_price = 50

    total_inserted = 0

    while total_inserted < coke_price:
        coin_inserted = False
        while not coin_inserted:
            try:
                coin = int(input("Insert coin one at a time: "))

                # check coin validity
                if coin in accepted_coins:
                    total_inserted += coin
                    coin_inserted = True
                    print("Amount due:", coke_price - total_inserted)

                else:
                    print("Invalid coin, amount due:", coke_price)

            except ValueError:
                print("Invalid input. Please enter an integer.")

    # change owed
    change_due = total_inserted - coke_price

    # output change due
    print("Change owed:", change_due, "cents. ")


if __name__ == "__main__":
    main()
