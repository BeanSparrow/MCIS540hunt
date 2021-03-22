# Exercise 1-4

# Libraries
import math

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
    milesPerHour = round((3600 / timeSeconds) * distanceMiles, 2)
    print(f'{milesPerHour} mph')

# Calculates Average Time per Mile and prints result


def timePerMileCalculator(miles, timeInSeconds):
    totalSecondsPerMile = math.floor(timeInSeconds / miles)
    minutesPerMile = math.floor(totalSecondsPerMile / 60)
    secondsPerMile = totalSecondsPerMile - (minutesPerMile * 60)
    print(
        f'Average {minutesPerMile} minutes and {secondsPerMile} seconds per mile')

# Main Function Contains Variable Declaration


def main():
    raceDistanceKilo = 10
    raceTimeHour = 0
    raceTimeMinute = 43
    raceTimeSecond = 30
    milesPerHourCalculator(kiloToMile(raceDistanceKilo), timeInSeconds(
        raceTimeHour, raceTimeMinute, raceTimeSecond))
    timePerMileCalculator(kiloToMile(raceDistanceKilo), timeInSeconds(
        raceTimeHour, raceTimeMinute, raceTimeSecond))


main()
