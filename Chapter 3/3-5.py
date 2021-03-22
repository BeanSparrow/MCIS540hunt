# Exercise 3-5

# Symbol Identification
plusSymbol = '+'
minusSymbol = '-'
barSymbol = '|'


# Sequence per Coloumn
columnAdd = ((minusSymbol * 4) + plusSymbol)


# Inner Box Fillings
fillBox = '    ' + barSymbol


# Adds Column Header Based on number of Columns Specified
def addColumn(columns):
    print(plusSymbol + columnAdd * columns)
    i = 4
    while i > 1:
        print(barSymbol + fillBox * columns)
        i -= 1


# Generates the Grid based on rows and columns specified
def generateGrid(rows, columns):
    rowCount = rows
    while rowCount > 0:
        addColumn(columns)
        rowCount -= 1
    print(plusSymbol + columnAdd * columns)


# Main Function
def main():
    generateGrid(2, 3)


main()
