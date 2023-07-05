import requests

url = "PASTE YOUR URL WITHIN THESE QUOTATIONS"

print(requests.post(url, json= {"number": 7} ).text)