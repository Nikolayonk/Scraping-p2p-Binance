# Scraping-p2p-Binance
Парсинг раздела p2p Binance. Программа отправляет Requests POST на сервер Binance, затем получая ответ в виде json, преобразует в csv формат, для удобного анализа данных. В данном примере используется связка RUB к различным парам криптовалют:
* USDT
* BTC
* BUSD
* BNB
* ETH
* DAI
# Как использовать:
-Установите виртуальное окружение virtualenv, для дальнейшего удобства.
```
pip install virtualenv
```
Создайте виртуальное окружение env
```
virtualenv env
```
Запустите для windows
```
./env/bin/activate
```
Запустите для osx
```
source ./env/bin/activate
```
Установите все необходимые зависимости, при налиии.
```
pip install -r req.txt
```
# Запуск:
-В командной строке выполните команду python3 main.py
```
python3 main.py
```
# Результат:
![Результат csv](https://i.postimg.cc/c4tvNJLF/2023-04-17-12-09-12.png)

