import requests
import os

API_KEY = 'fca_live_6RfbtFLrVplZfxCnNKFLP3mcTiC5hVwBqrKdVwTu'
BASE_URL = 'https://api.freecurrencyapi.com/v1/latest?apikey={}'.format(API_KEY)

TARGET_CURRENCIES = ["EUR", "USD", "BRL", "CAD", "AUD", "CNY"]

def get_amount():
    amount = None;
    
    while amount is None:
        try: 
            amount = float(input("Insira o valor: "))
        except:
            print("Valor inválido. Tente novamente.")

    return amount

def get_base_currency():
    base_currency = None;
    
    while base_currency not in TARGET_CURRENCIES:
        base_currency = input("Insira a moeda base: ")

        if base_currency.upper() in TARGET_CURRENCIES:
            return base_currency.upper()
        else:
            print("Moeda inválida. Tente novamente.")

def convert_currency(base_currency):
    formatted_target_currencies = ",".join(TARGET_CURRENCIES)

    url = '{}&base_currency={}&currencies={}'.format(BASE_URL, base_currency, formatted_target_currencies)

    try:
        response = requests.get(url)
        json = response.json()
        data = json["data"]
        del data[base_currency]
        return data;
    except Exception as e:
        print(e)
        return None;

def print_result(data, amount):
    for ticket, value in data.items():
        print("{}: {}".format(ticket, round(value * amount, 2)))

while True:
    AMOUNT = get_amount()
    BASE_CURRENCY = get_base_currency()
    
    os.system('cls')
    print("Convertendo {} {}:\n".format(AMOUNT, BASE_CURRENCY))

    data = convert_currency(BASE_CURRENCY)
    if not data:
        continue
    
    print_result(data, AMOUNT)
    
    if (input("\nDeseja realizar uma nova conversão? (s/n): ") != "s"):
        break
    else:
        os.system('cls')