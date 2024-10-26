import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Regular expression pattern for matching the time format
    pattern = r'^(1[0-2]|[1-9]):?([0-5][0-9])? (AM|PM) to (1[0-2]|[1-9]):?([0-5][0-9])? (AM|PM)$'
    match = re.match(pattern, s)
    if not match:
        raise ValueError("Invalid time format")

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    # Default minutes to 00 if not provided
    start_minute = start_minute if start_minute else '00'
    end_minute = end_minute if end_minute else '00'

    # Validate minutes
    if int(start_minute) >= 60 or int(end_minute) >= 60:
        raise ValueError("Invalid minutes")

    # Convert to 24-hour format
    start_hour_24 = to_24_hour_format(start_hour, start_minute, start_period)
    end_hour_24 = to_24_hour_format(end_hour, end_minute, end_period)

    return f"{start_hour_24} to {end_hour_24}"

def to_24_hour_format(hour, minute, period):
    hour = int(hour)
    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0
    return f"{hour:02}:{minute}"

if __name__ == "__main__":
    main()
