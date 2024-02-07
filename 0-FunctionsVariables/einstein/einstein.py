def energy(mass):
    speed_of_light = 300000000
    E = mass * speed_of_light**2

    return E


def main():
    mass = int(input("Enter mass number in kilograms:"))
    joules = int(energy(mass))
    print(joules)


main()
