# Exercise 3-4

# Runs Function Call Twice
def do_twice(f):
    f()
    f()


# Prints Spam
def print_spam():
    print('spam')


# Main Function
def main():
    do_twice(print_spam)


main()
