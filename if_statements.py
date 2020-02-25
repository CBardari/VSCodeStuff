"""
in - checks if a sub-collection is in a collection
    example: "so" in "something"
"""
password = "12283724"
guess = input("Enter your password")
while password != guess:
    print("Access Denied, Please try again")
    guess = input("Please try again")
print("Acces granted")
