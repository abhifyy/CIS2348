"""

Abhmanyu Kidarithil Meethal
PSID:2105385

"""
import math

height = int(input("Enter wall height (feet):\n"))
width = int(input("Enter wall width (feet):\n"))
wall_area = height * width
paint_needed = wall_area / 350
cans_needed = math.ceil(paint_needed)
paint_colors = {
    "red": 35,
    "blue": 25,
    "green": 23
}
print("Wall area: {} square feet".format(int(wall_area)))
print("Paint needed: %.2f gallons" % paint_needed)
print("Cans needed: {} can(s)".format(cans_needed))
color = input("\nChoose a color to paint the wall:\n")
paint_cost = cans_needed * paint_colors.get(color.lower(), 0)

print("Cost of purchasing {} paint: ${}".format(color.lower(), paint_cost))
