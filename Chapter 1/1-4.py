# Exercise 1-4

# Converts Race Time to Seconds
def timeInSeconds(hours, minutes, seconds):
    hourConverter = 60 ** 2
    minuteConverter = 60
    return ((hours * hourConverter) + (minutes * minuteConverter) + seconds)


# Converts Input Kilometers to Miles
def kiloToMile(kilometers):
    kiloPerMile = 1.61
    return (kilometers / kiloPerMile)


# Calculates Miles Per Hour based on input miles and seconds
def milesPerHourCalculator(distanceMiles, timeSeconds):
    return round(((3600 / timeSeconds) * distanceMiles), 2)


# Main Function
def main():
    raceDistanceKilo = 10
    raceTimeHour = 0
    raceTimeMinute = 43
    raceTimeSecond = 30
    print(f'{milesPerHourCalculator(kiloToMile(raceDistanceKilo), timeInSeconds(raceTimeHour, raceTimeMinute, raceTimeSecond))} mph')


main()
