def calc_expression(x, y, z):
    if y == "+":
        return x + z
    elif y == "*":
        return x * z
    elif y == "-":
        return x - z
    elif y == "/" and x > 0:
        return x / z
    else:
        print("not a valid expression!!")


def main():
    expression = input("enter an arithmetic expression:")
    x, y, z = expression.split()
    x = float(x)
    z = float(z)

    result = calc_expression(x, y, z)
    print(f"answer: {result: .1f}")


main()
