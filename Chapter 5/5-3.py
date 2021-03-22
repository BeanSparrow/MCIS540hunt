# Exercise 5-3

# Checks the Values against Fermat's Theorem
def check_fermat(a, b, c, n):
    fermatFirst = ((a**n)+(b**n))
    fermatSecond = (c**n)
    # print(fermatFirst)
    # print(fermatSecond)
    if fermatFirst == fermatSecond:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn\'t work.')


# Main function
def main():
    # Gets all Fermat Values
    fermatA, fermatB, fermatC, fermatN = map(
        int, input('Enter A B C and N\n').split())
    # Runs Theorem Check
    check_fermat(fermatA, fermatB, fermatC, fermatN)


main()
