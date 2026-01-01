import math

Shape = input("Pick a shape to calculate an area for (Square, Rectangle, Circle, Triangle): ")
SurfaceArea = input("Pick a 3D shape calculate area for (cubes, spheres, cylinders)")

if SurfaceArea == "None":
    print("No Surface Area")

if Shape.lower() == "rectangle":
    rect_length = float(input("Enter the length of the rectangle: "))
    rect_width = float(input("Enter the width of the rectangle: "))
    rect_area = rect_length * rect_width
    print(f"The area is {rect_area}cm^2")

elif Shape.lower() == "circle":
    radius = float(input("Enter the radius of the circle: "))
    circ_area = math.pi * radius * radius
    print(f"The area is {circ_area}cm^2")

elif Shape.lower() == "square":
    sq_length = float(input("Enter the length of the square: "))
    sq_area = sq_length * sq_length
    print(f"The area is {sq_area}cm^2")

elif Shape.lower() == "triangle":
    tri_base = float(input("Enter the base of the triangle: "))
    tri_height = float(input("Enter the height of the triangle: "))
    tri_area = 1/2 * tri_base * tri_height
    print(f"The area of the triangle is {tri_area} cm^2")

else:
    print("Shape is not valid")

user_input = input("Do you want quit?)")
if user_input.lower == "y":
    quit

