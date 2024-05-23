import requests
from celery import shared_task

from apps.common.models import ExchangeRate


@shared_task(name="get_currency")
def get_currency():
    url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"

    try:
        response = requests.get(url)
        data = response.json()

        currencies = []
        for item in data:
            if item["Ccy"] in ["USD", "EUR", "RUB"]:
                currency = {"Ccy": item["Ccy"], "Rate": item["Rate"], "Diff": item["Diff"]}
                currencies.append(currency)
        ExchangeRate.objects.create(
            usd=currencies[0]["Rate"],
            eur=currencies[1]["Rate"],
            rub=currencies[2]["Rate"],
            usd_diff=currencies[0]["Diff"],
            eur_diff=currencies[1]["Diff"],
            rub_diff=currencies[2]["Diff"],
        )
        return currencies

    except Exception as e:
        return e
