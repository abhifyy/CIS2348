
"""

Abhmanyu Kidarithil Meethal
PSID:2105385

"""

print("Birthday Calculator")
age = 0
print("Current day")
print("Month: ", end="")
c_month = int(input())
print("Day: ", end="")
c_date = int(input())
print("Year:  ", end="")
c_year = int(input())
print("Birthday")
print("Month: ", end="")
b_month = int(input())
print("Day: ", end="")
b_date = int(input())
print("Year:  ", end="")
b_year = int(input())

if c_month == b_month and c_date == b_date:
    print("Happy Birthday!")
    age = c_year - b_year
if c_month > b_month:
    age = c_year - b_year
if c_month < b_month:
    age = c_year-b_year - 1
if c_month == b_month:
    if c_date < b_date:
        age = c_year - b_year - 1
    elif c_date > b_date:
        age = c_year - b_year


print(f"You are {age} years old.")
