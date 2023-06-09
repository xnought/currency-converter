# Currency Converter

A Python REST API server that converts national currencies upon request.

Currency Converter supports HTTP `GET` requests:

-   `/currencies`
-   `/convert`
-   `/convert-all`

<a href="https://www.figma.com/file/I4FUw5ZXxNuHlK3nDIWHpU/Currency-Converter-Architecture?type=whiteboard&node-id=0%3A1&t=9F5v6CcHE8LXZIJY-1">
<img src="https://user-images.githubusercontent.com/65095341/236584335-e383d383-5109-40fb-be41-cb0ae7442104.png" alt="UML diagram"
</a>

## Endpoints

### `/currencies`

`GET` request to `/currencies` returns a list of supported currencies and their descriptions in plain english.

The "currency" names are three letter codes and are used later in the `/convert` and `/convert-all` endpoints.

**Example Request**

```bash
curl http://localhost:8000/currencies
```

**Response**

```json
[
	{ "currency": "CAD", "description": "Canadian Dollar" },
	{ "currency": "USD", "description": "US Dollar" },
	{ "currency": "EUR", "description": "Euro" },
	{ "currency": "JPY", "description": "Japanese Yen" },
	{ "currency": "CNY", "description": "Chinese Yuan Renminbi" },
	{ "currency": "GBP", "description": "British Pound" },
	{ "currency": "AUD", "description": "Australian Dollar" },
	{ "currency": "CHF", "description": "Swiss Franc" }
]
```

### `/convert`

`GET` request to `/convert/{currency}/{amount}/{other_currency}` converts the `amount` of a `currency` to the `other_currency`.

**Example Request to convert 100 USD to CAD**

```bash
curl http://localhost:8000/convert/USD/100/CAD
```

**Response**

```json
{ "amount": 133.6217102267553, "currency": "CAD" }
```

### `/convert-all`

`GET` request to `/convert-all/{currency}/{amount}` converts the `amount` of a `currency` to all other supported currencies.

**Example Request to convert 1000 CAD to all other currencies**

```bash
curl http://localhost:8000/convert-all/CAD/1000
```

**Response**

```json
[
	{ "amount": 748.381380767396, "currency": "USD" },
	{ "amount": 681.5238874122538, "currency": "EUR" },
	{ "amount": 100163.56573297894, "currency": "JPY" },
	{ "amount": 5140.939139916854, "currency": "CNY" },
	{ "amount": 602.283105022831, "currency": "GBP" },
	{ "amount": 1114.7004702514823, "currency": "AUD" },
	{ "amount": 668.7112383289034, "currency": "CHF" }
]
```

## Running the server

You must have pip and python 3 installed.

Then install the dependencies with

```bash
pip3 install -r requirements.txt
```

Then run the REST Currency Converter server on `http://localhost:8000` with

```bash
python3 server.py --port 8000
```

## Example in the browser

Open [`index.html`](examples/index.html) and the console to see requests in action using the `fetch` API.

## Sequence Diagram

You can call any one of these whenever you want. There is no sequence requred.

<img src="https://user-images.githubusercontent.com/65095341/236586273-cd6d5a77-cc63-4b29-ae4d-4136da100ffe.png" width="50%" >
