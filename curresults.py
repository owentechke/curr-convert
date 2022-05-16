
def convert_amount(amount, origcurrency, targetcurrency):
  my_api_key="paste_your_key_here"

  import requests
  import json

  url = "https://openexchangerates.org/api/latest.json?app_id="+ my_api_key
  response = requests.request("GET", url)

  # Convert JSON object to dictionary
  rate_data = json.loads(response.text)

  #origcurrencyrate = float(rate_data["rates"][origcurrency])
  origcurrencyrate = float(rate_data["rates"].get(origcurrency,1))
  targetcurrencyrate = float(rate_data["rates"].get(targetcurrency,0))
  convertedamount = amount / origcurrencyrate * targetcurrencyrate
  return convertedamount

amount = float(input("Amount: "))
origcurrency = input("Original Currency: ")
targetcurrency = input("Target Currency: ")

convertedamount = convert_amount(amount, origcurrency, targetcurrency)
myconvamount = "{0:,.2f}".format(convertedamount)
print(origcurrency, "{0:,.2f}".format(amount), "is", myconvamount, targetcurrency)
