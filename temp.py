import requests
from time import sleep

while True:
    try:
        requests.get("https://Zaglmain.ankurkumar8.repl.co")
        print("Done")
        sleep(3*3600)
    except:
        print("Not Fully Load")
        sleep(3600)
