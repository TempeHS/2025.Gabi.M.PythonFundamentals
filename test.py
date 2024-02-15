def convert(time):
    hours, minutes = int(time.split(":"))
    return hours + minutes / 60


def main():
    time = input("Enter the time: ")

    if time.startswith(7):
        print("Breakfast time!")
    elif time.startswith(8):
        print("Lunch time!")
    elif time.startswith(9):