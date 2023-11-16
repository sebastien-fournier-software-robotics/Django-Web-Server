# part2/views.py

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

import requests
import pandasdmx as sdmx


class ExchangeDataViewSet(viewsets.ViewSet):
    @action(detail=False, methods=["get"])
    def get_exchange_data(self, request):
        # Get Bitcoin price in EUR from the Blockchain API
        bitcoin_data = requests.get("https://blockchain.info/ticker")
        bitcoin_eur = bitcoin_data.json().get("EUR").get("15m")

        # Get EUR to GBP conversion rate from ECB API (monthly rate)

        ecb = sdmx.Request("ECB")
        data_response = ecb.data(
            resource_id="EXR", key="M.GBP.EUR.SP00.A", params={"startPeriod": "2023-09"}
        )
        data = data_response.data
        # set(s.key.FREQ for s in data.series)
        # monthly = (s for s in data.series if s.key.FREQ == "M")
        # ts2 = data_response.write(monthly)
        # ts2.tail()

        # rate = (
        #     data_response.write(sdmx_location="compact")
        #     .reset_index()
        #     .loc[0, "OBS_VALUE"]
        # )

        # data = sdmx.Request("ECB").data("EXR").structure("ECB").to_pandas()
        # data_response = data.loc["M.GBP.EUR.SP00.A", "OBS_VALUE"]

        # ecb = sdmx.Request("ECB")
        # parameters = {
        #     "startPeriod": "2023-10-01",
        #     "endPeriod": "2021-10-31",
        # }
        # data_response = ecb.data(
        #     resource_id="EXR",
        #     key={"CURRENCY": ["EUR", "GBP"]},
        #     params=parameters,
        # )
        # data = data_response.to_pandas()

        # ecb = (
        #     sdmx.Request("ECB")
        #     .data(
        #         resource_id="EXR",
        #         key="M.GBP.EUR.SP00.A",
        #         params={
        #             "startTime": "2023-10",
        #             "dimensionAtObservation": "TimeDimension",
        #         },
        #     )
        #     .write()
        # )
        print(data)

        # Convert Bitcoin price to GBP using the ECB rate
        bitcoin_gbp = bitcoin_eur * 1

        # Step 4: Prepare the response dictionary
        exchange_data = {
            "bitcoin_eur": bitcoin_eur,
            # "eur_to_gbp": eur_to_gbp,
            "bitcoin_gbp": bitcoin_gbp,
        }

        # Step 5: Return the response
        return Response(exchange_data)
