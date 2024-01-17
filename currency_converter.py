import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f'https://open.er-api.com/v6/latest/{base_currency}'
    params = {'apikey': api_key}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        rates = response.json()['rates']
        exchange_rate = rates.get(target_currency)
        if exchange_rate is not None:
            return exchange_rate
        else:
            print(f"Currency code '{target_currency}' not found.")
    else:
        print(f"Failed to fetch exchange rates. Status code: {response.status_code}")
    
    return None

def convert_currency(api_key, amount, from_currency, to_currency):
    exchange_rate = get_exchange_rate(api_key, from_currency, to_currency)

    if exchange_rate is not None:
        converted_amount = amount * exchange_rate
        return converted_amount
    else:
        return None
api_key = 'YOUR_API_KEY'
amount = float(input("Enter amount to convert: "))
from_currency = input("Enter source currency code: ").upper()
to_currency = input("Enter target currency code: ").upper()

result = convert_currency(api_key, amount, from_currency, to_currency)

if result is not None:
    print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}.")
