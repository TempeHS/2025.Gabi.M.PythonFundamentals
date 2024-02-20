# prompt user for variable


def camel_to_snake_case(camel_case_string):
    snake_case = " "
    first_char_processed = False
    for char in camel_case_string:
        if char.isupper() and first_char_processed:
            snake_case += "_"
        snake_case += char.lower()
        if not first_char_processed:
            first_char_processed = True
    return snake_case


def main():
    camel_case_string = input("Enter a variable name in camel case: ")
    snake_case_string = camel_to_snake_case(camel_case_string)
    print("Snake case string:", snake_case_string)


main()
