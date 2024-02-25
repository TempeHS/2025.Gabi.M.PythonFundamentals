def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not start_with_letters(s):
        return False
    if not end_with_numbers(s):
        return False
    if contain_invalid_char(s):
        return False
    return True


def start_with_letters(s):
    return s[:2].isalpha()


def end_with_numbers(s):
    if s[-1].isdigit() and s[-1] != "0":
        return True
    return False


def contain_invalid_char(s):
    for i in range(len(s)):
        if not s[i].isalnum():
            return True
        if s[i].isdigit() and i < len(s) - 1:
            return True
    return False


main()
