import sys
import requests

def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        bitcoin_price_usd = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        sys.exit(1)
    except KeyError:
        print("Unexpected response format from API")
        sys.exit(1)

    total_cost_usd = bitcoins * bitcoin_price_usd
    formatted_cost = "{:,.4f}".format(total_cost_usd)
    print(f"${formatted_cost} USD")

if __name__ == "__main__":
    main()
