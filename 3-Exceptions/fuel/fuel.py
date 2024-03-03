# prompt user for a fraction


def calc_fuel_percent(X, Y):
    percentage = (X / Y) * 100
    return round(percentage)


def main():
    while True:
        try:
            fraction = input("enter fraction (X/Y): ")
            if "/" not in fraction:
                raise ValueError

            X, Y = map(int, fraction.split("/"))

            if Y == 0:
                raise ZeroDivisionError

            elif X > Y:
                raise ValueError

            percentage = calc_fuel_percent(X, Y)

            if percentage <= 1:
                print("E")

            elif percentage >= 99:
                print("F")

            else:
                print(f"{percentage}%, full")

            break

        except ValueError:
            print("ValueError, try again.")

        except ZeroDivisionError:
            print("ZeroDivisionError, try again.")


main()
