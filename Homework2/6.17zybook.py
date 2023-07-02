"""

Abhmanyu Kidarithil Meethal
PSID:2105385

"""

def strong_password(password):
    stronger_password = ""
    for char in password:
        if char == "i":
            stronger_password += "!"
        elif char == "a":
            stronger_password += "@"
        elif char == "m":
            stronger_password += "M"
        elif char == "B":
            stronger_password += "8"
        elif char == "o":
            stronger_password += "."
        else:
            stronger_password += char

    stronger_password += "q*s"
    return stronger_password

password = input()

new_password = strong_password(password)

print(new_password)
