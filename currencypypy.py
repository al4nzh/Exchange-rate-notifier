from bs4 import BeautifulSoup
import requests
from plyer import notification
import time

def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    currency = soup.find("span", class_="ccOutputRslt").get_text()
    return currency

if __name__ == "__main__":
    in_currency = 'USD'
    out_currency = 'KZT'
    
    while True:
        currency_rate = get_currency(in_currency, out_currency)
        
        # Send a notification with the currency exchange rate
        notification_title = "Currency Exchange Rate USD to KZT"
        notification_message = f"1 {in_currency} = {currency_rate} {out_currency}"
        
        notification.notify(
            title=notification_title,
            message=notification_message,
            app_name="Currency Checker",
        )
        
        # Wait for one minute (60 seconds) before sending the next notification
        time.sleep(60)
