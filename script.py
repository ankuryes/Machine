from os import system
try:system("rm -f poetry.lock");system("rm -f pyproject.toml")
except:pass
import requests
from flask import Flask
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

app = Flask('')

@app.route('/')
def home():
    try: ip = str(requests.get("https://jsonip.com/").json()['ip'])
    except: ip = str(requests.get("http://ipinfo.io/ip").text)

    data = str(ip)
    dta = requests.post('https://Ips.ankurkumar8.repl.co/found', data=data).text
    return str(dta)

app.run(host='0.0.0.0', port=8080)
