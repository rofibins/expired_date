import datetime as dt

def expired_date(start_date, exp_days):

    custom_holidays = [dt.date(2021, 11, 15), dt.date(2021, 11, 16)]
    days_elapsed = 0

    while days_elapsed < exp_days:
        test_date = start_date + dt.timedelta(days=1)
        start_date = test_date
        if test_date.weekday() > 4 or test_date in custom_holidays:
            continue
        else:
            days_elapsed += 1

    return start_date

if __name__ == "__main__":
    date_entry = input("Enter a delivery date (yyyy-MM-dd) : ")
    year, month, day = map(int, date_entry.split('-'))
    print("Expired date : ", end = ' ')
    print(expired_date(dt.date(year,month,day), 3))