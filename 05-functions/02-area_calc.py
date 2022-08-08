#!/usr/bin/python3
import math
def get_shape():
    try:
        shape = str(input("Enter a shape: "))
        shape = shape.lower()
        match shape:
            case "square":
                square_area()
            case "rectangle":
                rectangle_area()
            case "circle":
                circle_area()
            case "triangle":
                triangle_area()
            case "rhombus":
                rhombus_area()
            case "trapezium":
                trapezium_area()
            case "parallelogram":
                parallelogram_area()
            case _:
                print("I can't find the area of the shape you are looking for. \n Try another one.")
    except ValueError:
        print("Please enter a string")

def sqaure_area():
    length = float(input("Enter the length of side of the square: "))
    print(f"Area of your square is {math.pow(length, 2):.2f}")

def rectangle_area():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print(f"Area of your rectangle is {length * width:.2f}")

def circle_area():
    radius = float(input("Enter the radius of your circle: "))
    print(f"Area of your cirlce is {math.pi * math.pow(radius, 2):.2f}")

def triangle_area():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    print(f"Area of your triangle is {(base / 2) * height:.2f}")

def rhombus_area(): 
    diag1 = float(input("Enter the length of the first diagonal: "))
    diag2 = float(input("Enter the length of the second diagonal: "))
    print(f"Area of your rhombus is {(diag1 * diag2) / 2 :.2f}")

def trapezium_area():
    side1 = float(input("Enter the length of the first parallel side: "))
    side2 = float(input("Enter the length of the second parallel side: "))
    height = float(input("Enter the height between parallel sides: "))
    print(f"Area of your trapezium is {(side1 + side2) / (height * 0.5) :.2f}")

def parallelogram_area():
    base = float(input("Enter the base of the parallelogram: "))
    height = float(input("Enter the perpendicular height of the parallelogram: "))
    print(f"Area of your parallelogram is {base * height :.2f}")

def main():
    get_shape()
    
