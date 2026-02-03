pwd = "admin"

username = input("Enter username:")
password = input("Enter password:")

if password == pwd:
    print("Login successful")
else:
    print("Invalid credentials")

# pwd = "admin"
# try:
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     if password != pwd:
#         raise ValueError("Invalid credentials")

#     print("Login successful")

# except ValueError:
#     print("Invalid credentials")
