# Exercise 2-4 Part 3
import math


#Calculate Total Time running in Seconds
def timeAdditionSeconds(milesEasy, milesTempo):
  easyPaceMinutes = 8
  easyPaceSeconds = 15
  tempoPaceMinutes = 7
  tempoPaceSeconds = 12
  totalMinutes = ((milesEasy * easyPaceMinutes) + (milesTempo * tempoPaceMinutes))
  totalSeconds = ((totalMinutes * 60) + (milesEasy * easyPaceSeconds) + (milesTempo * tempoPaceSeconds))
  return totalSeconds


#Determine New Time after Run
def newTime(initialTimeHour, initialTimeMinute, addedTime):
  morningOrNight = 'am'
  newTimeHour = initialTimeHour
  newTimeMinute = math.floor(addedTime / 60 + initialTimeMinute)
  while newTimeMinute >= 60:
    newTimeMinute -= 60
    newTimeHour += 1
  if newTimeHour >= 12:
    morningOrNight = 'pm'
  print(f'{newTimeHour}:{newTimeMinute} {morningOrNight}')


def main():
  initialTimeHour = 6
  initialTimeMinute = 52
  milesEasy = 2
  milesTempo = 3
  newTime(initialTimeHour, initialTimeMinute, timeAdditionSeconds(milesEasy, milesTempo)) 

main()