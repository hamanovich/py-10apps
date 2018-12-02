import datetime


def print_header():
    print('BIRTHDAY APP')
    print('============')


def get_birthday_from_user():
    print('Tell us when you were born: ')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    return datetime.datetime(year, month, day)


def compute_days_between_dates(original_date, now):
    date1 = now
    date2 = datetime.datetime(now.year, original_date.month, original_date.day)
    dt = date1 - date2
    return int(dt.total_seconds() / 60 / 60 / 24)


def print_birthday_information(days):
    if days < 0:
        print('Your birthday is in {} days!'.format(-days))
    elif days > 0:
        print('You had your birthday already this year! {} days ago'.format(days))
    else:
        print('Happy Birthday!')


def main():
    print_header()
    birthday = get_birthday_from_user()
    now = datetime.datetime.now()
    number_of_days = compute_days_between_dates(birthday, now)
    print_birthday_information(number_of_days)


main()
