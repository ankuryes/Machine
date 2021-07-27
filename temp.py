import requests
from time import sleep
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

urls = []
for i in range(9): urls.append(str(f"https://zagl{i+1}.ankurkumar8.repl.co"))
while True:
  for i in urls: requests.get(i,timeout=5)
  sleep(10800)
  print(Done)
