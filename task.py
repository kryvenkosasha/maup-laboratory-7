import urllib.request
import json

# Функція для отримання та виведення інформації
def get_and_display_info(url):
    try:
        response = urllib.request.urlopen(url)
        body = response.read()
    except urllib.error.HTTPError as e:
        print('HTTP Error:', e.code)
        return
    except urllib.error.URLError as e:
        print('URL Error:', e.reason)
        return

    # Парсинг JSON
    fromJson = json.loads(body.decode('utf-8'))

    # Виведення інформації
    for data in fromJson:
        print("Дата -", data['date'])
        print("Банк -", data['bankName'])
        print("Адреса сайту -", data['sourceUrl'])
        print("Валюта -", data['codeAlpha'])
        print("Покупка -", data['rateBuy'])
        print("Продажа -", data['rateSale'])
        print('')

# Запити для отримання даних
url_currency = 'http://resources.finance.ua/ua/public/currency-cash.json'
url_metals = 'http://resources.finance.ua/ua/public/metal-cash.json'

# Виклики функції для курсів валют та металів
print("Курси валют:")
get_and_display_info(url_currency)

print("Банківські метали:")
get_and_display_info(url_metals)
