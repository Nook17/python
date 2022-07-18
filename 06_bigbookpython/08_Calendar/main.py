#!/usr/bin/env python3

import datetime


DAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December')

while True:     # ask for the year
    print('Write the year')
    response = input('> ')
    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Enter the year as a number, for example: 2021')
    continue


while True:     # ask for the month
    print('Write the month')
    response = input('> ')

    if not response.isdecimal():
        print('Enter the month as a number, for example: 3')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Enter the number form 1 to 12')

def getCalendar(year, month):
    calText = ''

    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
    calText += ' ..Monday.....Tuesday...Wednesday..Thursday....Friday....Saturday....Sunday..\n'
    weekSeparator = ('+----------' * 7) + '+\n'
    blankRow = ('|          ' * 7) + '|\n'

    currentDate = datetime.date(year, month, 1)

    while currentDate.weekday() != 0:       # turn back time to the first Monday
        currentDate -= datetime.timedelta(days=1)
    # print(currentDate)

    while True:
        calText += weekSeparator
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)
        dayNumberRow += '|\n'

        calText += dayNumberRow
        for i in range(3):
            calText += blankRow

        if currentDate.month != month:
            break

    calText += weekSeparator
    return calText

calText = getCalendar(year, month)
print(calText)

calendarFileName = 'calendar_{}_{}.txt'.format(month, year)
with open(calendarFileName, 'w') as fileObj:
    fileObj.write(calText)
print('The file is saved under a name {}'.format(calendarFileName))
