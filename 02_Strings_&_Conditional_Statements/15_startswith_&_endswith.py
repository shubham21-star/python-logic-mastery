str = "I am a coder."

print(str.startswith("I"))
print(str.endswith("."))

# WAP check email
email = input("Enter email: ")

if email.endswith("@gmail.com"):
    print("Valid Gmail")
else:
    print("Invalid Gmail")