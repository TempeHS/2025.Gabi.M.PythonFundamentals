file_name = input("Enter a file name:")

# remove leading whitespace
user_file_name = file_name.strip()

if user_file_name.endswith(".jpg"):
    print("image/jpeg")
elif user_file_name.endswith(".jpeg"):
    print("image/jpeg")
elif user_file_name.endswith(".gif"):
    print("image/gif")
elif user_file_name.endswith(".png"):
    print("image/png")
elif user_file_name.endswith(".pdf"):
    print("application/pdf")
elif user_file_name.endswith(".txt"):
    print("txt/plain")
elif user_file_name.endswith(".zip"):
    print("applicatipn/zip")
else:
    print("application/octet-stream")
