import datetime, random


def getBirthdays(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        first_dat = datetime.date(1980, 1, 1)
        dat_delta = datetime.timedelta(random.randint(0, 364))
        dat_sum = first_dat + dat_delta
        birthdays.append(dat_sum)
    # print(birthdays)
    return birthdays

# print("".join(str(getBirthdays(10))))

print(getBirthdays(10))
