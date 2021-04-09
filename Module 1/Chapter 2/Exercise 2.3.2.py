# Chapter 2 Exercise 3.2
import math


# Determines the Shipping Cost Based on Number of Books
def shipCost(quantityBooks):
    return ((quantityBooks - 1) * 75) + 300


# Determines the Price per Book after Discount
def pricePerBook(priceCents, discount):
    return round(priceCents * (discount / 100),)


# Determines the Total Cost of the books plus shipping
def totalCostDollars(shipCost, pricePerBook, quantityBooks):
    totalCost = (((pricePerBook * quantityBooks) + shipCost)/100)
    print(f'${totalCost}')


# Main Function contains Variable Declarations
def main():
    priceCents = 2495
    discountPercentage = 40
    quantityBooks = 60
    totalCostDollars(shipCost(quantityBooks), pricePerBook(
        priceCents, discountPercentage), quantityBooks)


main()
