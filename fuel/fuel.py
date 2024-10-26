def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
    try:
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError("Denominator cannot be zero")

        if x > y:
            raise ValueError("Numerator cannot be greater than denominator")

        percentage = (x / y) * 100
        return str(round(percentage))  # Return as string instead of int
    except ValueError:
        raise ValueError("Invalid input: X and Y must be integers")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}"  


if __name__ == "__main__":
    main()
