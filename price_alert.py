from bs4 import BeautifulSoup
import requests


headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
URL = "https://www.amazon.in/Staging-Product-Not-Retail-Sale/dp/B08N3RQZ51/ref=sr_1_4?dchild=1&keywords=kindle&qid=1633335656&sr=8-4"
resp = requests.get(URL,headers=headers)
raw_text = u"\u20B9"
soup = BeautifulSoup(resp.content, "html5lib")
price = soup.find(id="priceblock_ourprice").get_text()
price = price.split(raw_text)[1]

pf=float(price.replace(',',''))
print(pf)
buy_price = 13000
if pf<=buy_price:
    telegram_chatID = "-580485284"
    telegram_token = "2020042444:AAHGgMFYx57ALlFZFMcjl5H7k0RbEfpLuQ0"
    telegram_baseurl = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    message = "Kindle Price dropped to {}!!".format(pf)

    telegram_params = {
        "chat_id": telegram_chatID,
        "text": message,
    }
    telegram_response = requests.get(url=telegram_baseurl, params=telegram_params)
    print(telegram_response)