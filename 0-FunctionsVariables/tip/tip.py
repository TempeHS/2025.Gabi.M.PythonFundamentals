def dollars_to_float(d):
    d = d.lstrip("$")
    return float(d)


def percent_to_float(p):
    p = p.rstrip("%")
    return float(p)


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip?"))
    # tip = dollars * percent
    tip = (percent * dollars) / 100
    print(f"Leave ${tip:.2f}")


main()
