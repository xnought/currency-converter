from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
from pydantic import BaseModel
from currency_converter import CurrencyConverter
from fire import Fire

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"])
c = CurrencyConverter()


class ConvertResponse(BaseModel):
    amount: float
    currency: str


SUPPORTED_CURRENCIES = [
    "CAD",  # Canadian Dollar
    "USD",  # US Dollar
    "EUR",  # Euro
    "JPY",  # Japanese Yen
    "CNY",  # Chinese Yuan Renminbi
    "GBP",  # British Pound
    "AUD",  # Australian Dollar
    "CHF",  # Swiss Franc
]

SUPPORTED_CURRENCIES_DESCRIPTION = [
    "Canadian Dollar",
    "US Dollar",
    "Euro",
    "Japanese Yen",
    "Chinese Yuan Renminbi",
    "British Pound",
    "Australian Dollar",
    "Swiss Franc",
]


class SupportedResponse(BaseModel):
    currency: str
    description: str


@app.get("/currencies")
def supported_currencies() -> list[SupportedResponse]:
    return [
        SupportedResponse(currency=currency, description=description)
        for currency, description in zip(
            SUPPORTED_CURRENCIES, SUPPORTED_CURRENCIES_DESCRIPTION
        )
    ]


@app.get("/convert/{from_currency:str}/{amount:float}/{to_currency:str}")
def convert(from_currency: str, amount: float, to_currency: str) -> ConvertResponse:
    # if currency not supported error out with status 404
    if (
        from_currency not in SUPPORTED_CURRENCIES
        or to_currency not in SUPPORTED_CURRENCIES
    ):
        raise HTTPException(status_code=404, detail="Currency not found")

    # convert the from_currency amount to the to_currency amount
    # if this fails, also error out with status 404
    try:
        conversion = c.convert(amount, from_currency, to_currency)
    except ValueError:
        raise HTTPException(status_code=404, detail="Converter failed")

    return ConvertResponse(amount=conversion, currency=to_currency)


@app.get("/convert-all/{from_currency:str}/{amount:float}")
def convert_all(from_currency: str, amount: float) -> list[ConvertResponse]:
    return [
        convert(from_currency, amount, to_currency)
        for to_currency in SUPPORTED_CURRENCIES
        if to_currency != from_currency
    ]


def server_runner(host: str = "localhost", port: int = 8000):
    run(app, host=host, port=port)


if __name__ == "__main__":
    """
    python3 converter.py
    will run the server on http://localhost:8000

    --- if you want to change port
    python3 converter.py --port 8080
    will run the server on http://localhost:8080

    you get the point
    """
    Fire(server_runner)
