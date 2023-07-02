"""

Abhmanyu Kidarithil Meethal
PSID:2105385

"""
s=input()
k = s.replace(" ", "")
if k.lower()==k.lower()[::-1]:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")

