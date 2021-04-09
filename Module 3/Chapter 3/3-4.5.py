# Exercise 3-4 Part 5

# Runs Function Call Twice
def do_twice(f, argument):
    f(argument)
    f(argument)


# Prints Spam
def print_twice(s):
    print(s)
    print(s)


# Runs Function do_twice, twice
def do_four(f, argument):
    do_twice(f, argument)
    do_twice(f, argument)


# Main Function
def main():
    do_four(print_twice, 'spam')


main()
