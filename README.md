# currency-converter

You must have pip and python installed.

Then install the dependencies with

```bash
pip3 install -r requirements.txt
```

Then run the REST server with

```bash
python3 main.py
```

which hosts the only two endpoint `/convert` and `/supported-currencies` on `http://localhost:8000`.

### `http://localhost:8000/supported-currencies`

GET request to `/supported-currencies` returns a list of supported currencies.

```bash
curl http://localhost:8000/supported-currencies
# >>> ["CAD","USD","EUR","JPY","CNY","GBP","AUD","CHF"]
```

### `http://localhost:8000/convert/{from}/{amount}/{to}`

GET request that converts a supported currency name of a given amount to a different supported currency.

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
