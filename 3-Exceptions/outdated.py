def get_month_number(month_name):
    # Dictionary to assign month names to their numbers
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,
    }

    # Convert month name to title case and return the corresponding number
    return months.get(month_name.title())


def main():
    print("Please enter a date in MM/DD/YYYY format: ")
    while True:
        try:
            date_input = input("Date: ").strip()

            # Split the input by '/', ',', ' ', and '-'
            parts = [
                part.strip()
                for part in date_input.replace("/", ",")
                .replace("-", ",")
                .replace(" ", ",")
                .split(",")
            ]
            # print(f"PARTS! {parts}\n")
            # Extract day, month, and year from the input
            if "" in parts:
                parts.remove("")

            if len(parts) == 3:
                if (
                    parts[0].isdigit() and int(parts[0]) > 12
                ):  # If the first part is a digit, assume it's the month
                    main()
                elif int(parts[1]) > 31:
                    main()
                elif (
                    parts[0].isdigit() and int(parts[0]) <= 12
                ):  # If the first part is a digit, assume it's the month
                    month = int(parts[0])
                    day = int(parts[1])
                    year = int(parts[2])
                else:
                    month = get_month_number(parts[0])  # Convert month name to number
                    day = int(parts[1])
                    year = int(parts[2])

                # Print the date in month-day-year format
                if month < 10 or day < 10:
                    print(f"Date in year-month-day format: {year}-{month:02}-{day:02}")
                    exit()
                else:
                    print(f"Date in year-month-day format: {year}-{month}-{day}")
                    exit()
            else:
                print(
                    "Invalid date format. Please enter the date in the specified format."
                )
                exit()

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
