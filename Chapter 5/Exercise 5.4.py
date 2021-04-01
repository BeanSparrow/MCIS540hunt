# Exercise 5-4


# Request Stick Length for Three Sticks
def get_stick_lengths():
    loopFlag = True
    sticks_arr = []
    while loopFlag:
        try:
            stick1, stick2, stick3 = map(int, input(
                'Input the integer length of the three sticks.\n').split())
            loopFlag = False
        except:
            print('That is an invalid value, please try again.')
    sticks_arr.append(stick1)
    sticks_arr.append(stick2)
    sticks_arr.append(stick3)
    return sticks_arr


# Calculates Sum of Input Stick Values
def get_sums(sticks):
    sums_arr = []
    sums_arr.append(sticks[0]+sticks[1])
    sums_arr.append(sticks[1]+sticks[2])
    sums_arr.append(sticks[0]+sticks[2])
    return sums_arr


# Calculates if Triangle is Possible
def is_triangle(sums, sticks):
    possible = True
    for i in range(3):
        for j in range(3):
            if sticks[j-1] > sums[i-1]:
                possible = False
    if possible == True:
        print('Yes')
    else:
        print('No')


def main():
    sticks_arr = get_stick_lengths()
    sums_arr = get_sums(sticks_arr)
    is_triangle(sums_arr, sticks_arr)


main()
