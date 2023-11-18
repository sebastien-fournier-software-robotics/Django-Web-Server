# part2/views.py

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

import pandasdmx as sdmx
import pandas as pd

import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta


class ExchangeDataViewSet(viewsets.ViewSet):
    @action(detail=False, methods=["get"])
    def get_exchange_data(self, request):
        # Get the Bitcoin price in EUR from the Blockchain API, delayed from 15min
        bitcoin_data = requests.get("https://blockchain.info/ticker")
        bitcoin_data.raise_for_status()

        bitcoin_eur = bitcoin_data.json().get("EUR").get("15m")

        # Get the average exchange rate from last month for the EUR-GBP pair, from the ECB data
        # That is expressed by the M.GBP.EUR.SP00.A
        last_month = (datetime.now() - relativedelta(months=1)).strftime("%Y-%m")
        ecb = sdmx.Request("ECB")
        data_response = pd.DataFrame(
            sdmx.to_pandas(
                ecb.data(
                    resource_id="EXR",
                    key="M.GBP.EUR.SP00.A",
                    params={"startPeriod": last_month},
                )
            )
        )

        # Note: We expect a DataFrame with only 1 value given all columns indexes
        # For example :
        # FREQ CURRENCY CURRENCY_DENOM EXR_TYPE EXR_SUFFIX TIME_PERIOD
        #   M    GBP      EUR            SP00     A          2023-10      0.867984
        eur_to_gbp = data_response.iloc[0][0]

        # Convert Bitcoin price to GBP using the ECB rate
        bitcoin_gbp = bitcoin_eur * eur_to_gbp

        exchange_data = {
            "bitcoin_eur": bitcoin_eur,
            "eur_to_gbp": eur_to_gbp,
            "bitcoin_gbp": bitcoin_gbp,
        }

        return Response(exchange_data)
