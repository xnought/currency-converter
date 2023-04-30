# currency-converter

Supports three endpoints `/convert`, `/convert-all`, and `/supported-currencies`. All detailed below.

## Setup

You must have pip and python 3 installed.

Then install the dependencies with

```bash
pip3 install -r requirements.txt
```

Then run the REST server with

```bash
python3 converter.py
```

which hosts the server on `http://localhost:8000`.

**optional**

if you want to run it on a different port instead of 8000, you can specify the port with the `--port` flag.

```bash
python3 converter.py --port 8080 #or whatever port
```

## `http://localhost:8000/supported-currencies`

GET request to `/supported-currencies` returns a list of supported currencies.

**From command line**

```bash
curl http://localhost:8000/supported-currencies
# >>> ["CAD","USD","EUR","JPY","CNY","GBP","AUD","CHF"]
```

## `http://localhost:8000/convert/{from_currency}/{amount}/{to_currency}`

GET request that converts a supported currency name of a given amount to a different supported currency. If this call fails, it will return a status 404 error.

For example, I want to convert 100 US Dollars (USD) to canadian (CAD).

```bash
curl http://localhost:8000/convert/USD/100/CAD
# >>> {"amount":133.6217102267553,"currency":"CAD"}
```

For example, I want to convert 348.55 canadian (CAD) to euros (EUR)

```bash
curl http://localhost:8000/convert/CAD/348.55/EUR
# >>> {"amount":237.54515095754107,"currency":"EUR"}
```

## `http://localhost:8000/convert-all/{currency}/{amount}`

GET request to convert the amount of currency to all other supported currencies. Returns a list of conversions.

```bash
curl http://localhost:8000/convert-all/CAD/1000
# >>> [{"amount":748.381380767396,"currency":"USD"},{"amount":681.5238874122538,"currency":"EUR"},{"amount":100163.56573297894,"currency":"JPY"},{"amount":5140.939139916854,"currency":"CNY"},{"amount":602.283105022831,"currency":"GBP"},{"amount":1114.7004702514823,"currency":"AUD"},{"amount":668.7112383289034,"currency":"CHF"}]
```
