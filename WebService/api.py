from flask import Flask, render_template, request, json
import os
import requests

if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    # use '0.0.0.0' to ensure your REST API is reachable from all your
    # network (and not only your computer).
    host = '0.0.0.0'
else:
    port = 50000
    host = '127.0.0.1'
    transactionCount = 0

app = Flask(__name__)
transactionCount = 0
#url = 'http://api.sandbox.amadeus.com/v1.2/trains/extensive-search?origin=871A001&destination=871A008&departure_date=2017-12-29&apikey=DLnGlh7WM0Jx7ybk9zUTirdsGGPyrgP5'

result = '''{
  "results": [
    {
      "origin": {
        "station_id": "8768600",
        "station_name": "PARIS GARE DE LYON"
      },
      "destination": {
        "station_id": "8775605",
        "station_name": "NICE VILLE"
      },
      "itineraries": [
        {
          "trains": [
            {
              "departs_at": "2017-12-25T07:19",
              "departure_station": {
                "station_id": "8768600",
                "station_name": "PARIS GARE DE LYON"
              },
              "arrives_at": "2017-12-25T13:06",
              "arrival_station": {
                "station_id": "8775605",
                "station_name": "NICE VILLE"
              },
              "marketing_company": "SNCF",
              "operating_company": "SNCF",
              "train_number": "6171",
              "train_type": "TGV Duplex",
              "prices": [
                {
                  "service_class": "SECOND_CLASS_SEAT",
                  "booking_code": "SNF-BP",
                  "accommodation": "SEAT",
                  "total_price": {
                    "amount": "132.00",
                    "currency": "EUR"
                  },
                  "rate": {
                    "rate_code": "PN00",
                    "rate_name": "TGV LOISIR",
                    "restrictions": "RefWithCondition"
                  }
                }
              ]
            }
          ]
        },
        {
          "trains": [
            {
              "departs_at": "2017-12-25T09:21",
              "departure_station": {
                "station_id": "8768600",
                "station_name": "PARIS GARE DE LYON"
              },
              "arrives_at": "2017-12-25T15:06",
              "arrival_station": {
                "station_id": "8775605",
                "station_name": "NICE VILLE"
              },
              "marketing_company": "SNCF",
              "operating_company": "SNCF",
              "train_number": "6173",
              "train_type": "TGV Duplex",
              "prices": [
                {
                  "service_class": "SECOND_CLASS_SEAT",
                  "booking_code": "SNF-BP",
                  "accommodation": "SEAT",
                  "total_price": {
                    "amount": "132.00",
                    "currency": "EUR"
                  },
                  "rate": {
                    "rate_code": "PN00",
                    "rate_name": "TGV LOISIR",
                    "restrictions": "RefWithCondition"
                  }
                }
              ]
            }
          ]
        },
        {
          "trains": [
            {
              "departs_at": "2017-12-25T10:19",
              "departure_station": {
                "station_id": "8768600",
                "station_name": "PARIS GARE DE LYON"
              },
              "arrives_at": "2017-12-25T16:10",
              "arrival_station": {
                "station_id": "8775605",
                "station_name": "NICE VILLE"
              },
              "marketing_company": "SNCF",
              "operating_company": "SNCF",
              "train_number": "6175",
              "train_type": "TGV Duplex",
              "prices": [
                {
                  "service_class": "SECOND_CLASS_SEAT",
                  "booking_code": "SNF-BP",
                  "accommodation": "SEAT",
                  "total_price": {
                    "amount": "132.00",
                    "currency": "EUR"
                  },
                  "rate": {
                    "rate_code": "PN00",
                    "rate_name": "TGV LOISIR",
                    "restrictions": "RefWithCondition"
                  }
                }
              ]
            }
          ]
        },
        {
          "trains": [
            {
              "departs_at": "2017-12-25T14:11",
              "departure_station": {
                "station_id": "8768600",
                "station_name": "PARIS GARE DE LYON"
              },
              "arrives_at": "2017-12-25T20:10",
              "arrival_station": {
                "station_id": "8775605",
                "station_name": "NICE VILLE"
              },
              "marketing_company": "SNCF",
              "operating_company": "SNCF",
              "train_number": "6077",
              "train_type": "TGV Duplex",
              "prices": [
                {
                  "service_class": "SECOND_CLASS_SEAT",
                  "booking_code": "SNF-BP",
                  "accommodation": "SEAT",
                  "total_price": {
                    "amount": "132.00",
                    "currency": "EUR"
                  },
                  "rate": {
                    "rate_code": "PN00",
                    "rate_name": "TGV LOISIR",
                    "restrictions": "RefWithCondition"
                  }
                }
              ]
            }
          ]
        },
        {
          "trains": [
            {
              "departs_at": "2017-12-25T14:11",
              "departure_station": {
                "station_id": "8768600",
                "station_name": "PARIS GARE DE LYON"
              },
              "arrives_at": "2017-12-25T20:10",
              "arrival_station": {
                "station_id": "8775605",
                "station_name": "NICE VILLE"
              },
              "marketing_company": "SNCF",
              "operating_company": "SNCF",
              "train_number": "6177",
              "train_type": "TGV Duplex",
              "prices": [
                {
                  "service_class": "SECOND_CLASS_SEAT",
                  "booking_code": "SNF-BP",
                  "accommodation": "SEAT",
                  "total_price": {
                    "amount": "132.00",
                    "currency": "EUR"
                  },
                  "rate": {
                    "rate_code": "PN00",
                    "rate_name": "TGV LOISIR",
                    "restrictions": "RefWithCondition"
                  }
                }
              ]
            }
          ]
        },
        {
          "trains": [
            {
              "departs_at": "2017-12-25T17:19",
              "departure_station": {
                "station_id": "8768600",
                "station_name": "PARIS GARE DE LYON"
              },
              "arrives_at": "2017-12-25T23:04",
              "arrival_station": {
                "station_id": "8775605",
                "station_name": "NICE VILLE"
              },
              "marketing_company": "SNCF",
              "operating_company": "SNCF",
              "train_number": "6181",
              "train_type": "TGV Duplex",
              "prices": [
                {
                  "service_class": "SECOND_CLASS_SEAT",
                  "booking_code": "SNF-BG",
                  "accommodation": "SEAT",
                  "total_price": {
                    "amount": "118.00",
                    "currency": "EUR"
                  },
                  "rate": {
                    "rate_code": "PR11",
                    "rate_name": "TGV LOISIR",
                    "restrictions": "RefWithCondition"
                  }
                }
              ]
            }
          ]
        },
        {
          "trains": [
            {
              "departs_at": "2017-12-25T18:19",
              "departure_station": {
                "station_id": "8768600",
                "station_name": "PARIS GARE DE LYON"
              },
              "arrives_at": "2017-12-26T00:03",
              "arrival_station": {
                "station_id": "8775605",
                "station_name": "NICE VILLE"
              },
              "marketing_company": "SNCF",
              "operating_company": "SNCF",
              "train_number": "6079",
              "train_type": "TGV Duplex",
              "prices": [
                {
                  "service_class": "SECOND_CLASS_SEAT",
                  "booking_code": "SNF-BG",
                  "accommodation": "SEAT",
                  "total_price": {
                    "amount": "111.00",
                    "currency": "EUR"
                  },
                  "rate": {
                    "rate_code": "PR11",
                    "rate_name": "TGV LOISIR",
                    "restrictions": "RefWithCondition"
                  }
                }
              ]
            }
          ]
        },
        {
          "trains": [
            {
              "departs_at": "2017-12-25T18:19",
              "departure_station": {
                "station_id": "8768600",
                "station_name": "PARIS GARE DE LYON"
              },
              "arrives_at": "2017-12-26T00:03",
              "arrival_station": {
                "station_id": "8775605",
                "station_name": "NICE VILLE"
              },
              "marketing_company": "SNCF",
              "operating_company": "SNCF",
              "train_number": "6183",
              "train_type": "TGV Duplex",
              "prices": [
                {
                  "service_class": "SECOND_CLASS_SEAT",
                  "booking_code": "SNF-BG",
                  "accommodation": "SEAT",
                  "total_price": {
                    "amount": "111.00",
                    "currency": "EUR"
                  },
                  "rate": {
                    "rate_code": "PR11",
                    "rate_name": "TGV LOISIR",
                    "restrictions": "RefWithCondition"
                  }
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}'''



@app.route("/")
def main():
    return render_template('searchPage.html')


@app.route('/transactions')
def showTransactions():
    global transactionCount
    #transactionCount += 1
    return json.dumps({'transactionCount': transactionCount})

@app.route('/reset')
def resetTransactions():
    global transactionCount
    transactionCount = 0
    return json.dumps({'transactionCount': transactionCount})

@app.route('/search')
def searchTrains():
    #global url, result, transactionCount
    global result, transactionCount
    transactionCount += 1
    return json.dumps(result)
    #response = requests.get(url)
    # if response.ok:
    #     jData = json.loads(response.content)
    #     return jData
    # else:
    #     return json.dumps(result)

@app.route('/searchResults')
def searchResults():
    #global url, result, transactionCount
    global transactionCount
    transactionCount += 1
    return render_template('searchResults.html')



if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)

