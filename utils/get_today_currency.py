# from data import connector
import requests
def get_currency_today(from_="USD", to_="TRY", amount=100):
    url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/convert"

    querystring = {"from":f"{from_}","to":f"{to_}","amount":f"{amount}"}

    headers = {
        "x-rapidapi-key": "a0073c1790mshfd644a326ced12ep1e7f05jsnccae13a241ed",
        "x-rapidapi-host": "currency-conversion-and-exchange-rates.p.rapidapi.com"
    }

    r = requests.get(url, headers=headers, params=querystring)
    res = r.json()
    if res['success']:
        return {
            "from": from_,
            "to": to_,
            "amount": amount,
            "result": res['result'],
            "date": res['date']
        }
    else:
        return