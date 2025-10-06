name = input("What is your name? ")
last_name = input("What is your last name? ")

name = name[0].upper() + name[1:]
last_name = last_name[0].upper() + last_name[1:]

print("Hello, " + name + " " + last_name + "! This is a GitHub repository.")