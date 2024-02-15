def get_meal(user_input):
    time_split = user_input.split(":")
    # print(time_split)
    hour = time_split[0]
    minute = time_split[1]

    time_float = int(hour) + int(minute) / 60
    # print(f"{time_float:.2f}")

    if 7.0 <= time_float <= 8.0:
        return "Breakfast Time"
    elif 12.0 <= time_float <= 13.0:
        return "Lunch Time"
    elif 18.0 <= time_float <= 19.0:
        return "Dinner Time"
    else:
        return "No specific meal time"


user_input = input("Enter the time (HH:MM): ")
meal = get_meal(user_input)
print(meal)
