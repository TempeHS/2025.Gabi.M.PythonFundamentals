x = input("What's the answer to the great question of life? ")

# match x.lower():
#     case "42" | "forty two" | "forty-two":
#         print("Yes")
#     case _:
#         print("No")

answer = x.lower()
if answer == "42" or answer == "forty two" or answer == "forty-two":
    print("yes")
else:
    print("no")
