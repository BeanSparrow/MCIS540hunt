# Exercise 2-4 Part 1
import math


# Calculates Volume of passed Radius
def volumeSphere(radius):
    ratio = 4/3
    return (ratio * math.pi * (radius**3))


# Main Function
def main():
    # Radius Value
    radius = 5
    print(round(volumeSphere(radius), 1))


main()
