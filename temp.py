import grequests
from time import sleep

while True:
    try:
        urls = []
        for i in range(9): urls.append(str(f"http://zagl{i+1}.ankurkumar8.repl.co"))
        rs = (grequests.get(u,timeout=10) for u in urls)
        grequests.map(rs)
        print("Done")
        sleep(10800)
    except:
        print("Not Fully Function")
        sleep(3600)
