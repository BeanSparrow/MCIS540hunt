# Chapter 2 Exercise 3.1
import math


# Calculates Volume of passed Radius
def volumeSphere(radius):
    ratio = 4/3
    print(round(ratio * math.pi * (radius**3), 1))


# Executes and Prints Volume Calculation
def main():
    radius = 5
    volumeSphere(radius)


main()
