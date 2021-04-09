# Exercise 3-3

# Takes a String (s) and Right Justifies to Column 70
def right_justify(s):
    rightJustifiedString = s.rjust(70)
    return rightJustifiedString


# Requests Userinput for String Variable (s)
def stringInput():
    print('Enter a String')
    s = input()
    return s


# Main Function
def main():
    # Executes String Input and Right Justify
    print(right_justify(stringInput()))


main()
