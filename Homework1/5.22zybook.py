"""

Abhmanyu Kidarithil Meethal
PSID:2105385

"""
print("""Davy's auto shop services
Oil change -- $35
Tire rotation -- $19
Car wash -- $7
Car wax -- $12""")
lst = [("Oil change", 35), ("Tire rotation", 19), ("Car wash", 7), ("Car wax", 12), ("-", "No service")]
print()
print("Select first service:")
s1 = input()
print("Select second service:")
s2 = input()
print()
k = 0
x = 0
for i, j in lst:
    if i == s1:
        k = j
    if i == s2:
        x = j
print("Davy's auto shop invoice\n")
if k != "No service" and x != "No service":
    print(f"Service 1: {s1}, ${k}")
    print(f"Service 2: {s2}, ${x}\n")
    print(f"Total: ${k+x}")
else:
    if k == "No service" and x != "No service":
        print(f"Service 1: {k}")
        print(f"Service 2: {s2}, ${x}\n")
        print(f"Total: ${x}")
    elif x == "No service" and k != "No service":
        print(f"Service 1: {s1}, ${k}")
        print(f"Service 2: {x}\n")
        print(f"Total: ${k}")
    else:
        print(f"Service 1: {k}")
        print(f"Service 2: {x}\n")
        print(f"Total: $0")
