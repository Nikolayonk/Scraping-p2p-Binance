import requests
import json
import csv


def get_data():
    data_list = []

    l_usd = ["USDT","BTC","BUSD","BNB","ETH", "DAI"]
    buy_sell = ["BUY","SELL"]
    
    for bs in buy_sell:
        for lr in l_usd:
            website = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
            response = requests.post(website, json={
                "asset": lr,
                "countries": [],
                "fiat": "RUB",
                "page": 1,
                "payTypes": [],
                "proMerchantAds": False,
                "rows": 10,
                "tradeType": bs
            })

            data = response.json()
            l_data = data.get("data")[:1]

            for im in l_data:
                item_fiat = im.get('adv').get("fiatUnit")
                item_price = im.get('adv').get("price")
                item_asset = im.get('adv').get("asset")
                item_trade = im.get('adv').get("tradeMethods")
                item_surplusAmount = im.get('adv').get("surplusAmount")
                item_tradeType = im.get('adv').get("tradeType")
                item_trade = im.get('adv').get("tradeMethods")
               #Объявляем пустой массив, для формирования списка банков, конкретной пары торговли.
                pay_list = []
                for ps in item_trade:
                    item_ntrade = ps.get("tradeMethodName")
                        
                    pay_list.append(item_ntrade)
            data_list.append(
                [item_fiat,item_price,item_asset,item_surplusAmount,item_tradeType,str(pay_list)]
            )

            # Запись в csv
    with open(f'result.csv', 'w', encoding='utf-16') as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                'Фиат',
                'Цена',
                'Альткоин',
                'Доступно',
                'Вид сделки',
                'Банк',
            )
        )
        
        writer.writerows(
            data_list
        )

def main():
    get_data()

if __name__ == '__main__':
    main()

