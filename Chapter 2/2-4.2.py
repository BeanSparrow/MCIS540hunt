# Exercise 2-4 Part 2


# Function to determin Shipping Cost
def shipCost(quantityBooks):
    return ((quantityBooks - 1) * 75) + 300


# Function to determin Price of each book with discount
def pricePerBook(priceCents, discount):
    return round(priceCents * (discount / 100),)


# Function to determine the total cost
def totalCostDollars(shipCost, pricePerBook, quantityBooks):
    return (((pricePerBook * quantityBooks) + shipCost)/100)


# Main Function
def main():
    priceCents = 2495
    discountPercentage = 40
    quantityBooks = 60
    print(f'${totalCostDollars(shipCost(quantityBooks), pricePerBook(priceCents, discountPercentage), quantityBooks)}')


main()
