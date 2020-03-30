import requests
r=requests.get("https://financialmodelingprep.com/api/v3/company/rating/AAPL")
print(r.text)
print(r.status_code)

# url="wwwsomething.com"
#
# data={
#     "p1":4,"p2":8,"p3":9
# }
# r2=requests.post(url=url,data=data)
r=requests.get("")
