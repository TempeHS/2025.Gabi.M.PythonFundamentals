def convert(input_str):
    # Replace :) with 🙂
    output_str = input_str.replace(":)", "🙂")

    # Replace :( with 🙁
    output_str = output_str.replace(":(", "🙁")

    return output_str


def main():
    input_str = input("Enter your text here: ")
    print(convert(input_str))


main()
