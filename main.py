from fastapi import FastAPI
from uvicorn import run
from pydantic import BaseModel
from fastapi.exceptions import HTTPException
from currency_converter import CurrencyConverter

app = FastAPI()
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


@app.get("/supported-currencies")
def supported_currencies():
    return SUPPORTED_CURRENCIES


@app.get("/convert/{from_currency:str}/{amount:float}/{to_currency:str}")
def convert(from_currency: str, amount: float, to_currency: str) -> ConvertResponse:
    if (
        from_currency not in SUPPORTED_CURRENCIES
        or to_currency not in SUPPORTED_CURRENCIES
    ):
        raise HTTPException(status_code=404, detail="Currency not found")

    try:
        conversion = c.convert(amount, from_currency, to_currency)
    except ValueError:
        raise HTTPException(status_code=404, detail="Converter failed")

    return ConvertResponse(amount=conversion, currency=to_currency)


if __name__ == "__main__":
    run(app, host="localhost", port=8000)
