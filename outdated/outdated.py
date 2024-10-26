def main():
    import sys
    import datetime

    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date_str = input("Date: ").strip()

        # Try parsing the date in MM/DD/YYYY format
        try:
            month, day, year = map(int, date_str.split('/'))
            date = datetime.date(year, month, day)
            print(date.isoformat())
            break
        except ValueError:
            pass

        # Try parsing the date in Month DD, YYYY format
        try:
            month_str, day_year = date_str.split(' ', 1)
            day_str, year_str = day_year.split(', ')
            month = months.index(month_str) + 1
            day = int(day_str)
            year = int(year_str)
            date = datetime.date(year, month, day)
            print(date.isoformat())
            break
        except (ValueError, IndexError):
            pass

if __name__ == "__main__":
    main()
