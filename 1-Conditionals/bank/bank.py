greeting = input("Hello, enter a greeting: ")

# Remove leading whitespaces and make it case-insensitive
user_greeting = greeting.strip().lower()

if user_greeting.startswith("hello"):
    print("$0")
elif user_greeting.startswith("h"):
    print("$20")
else:
    print("$100")
