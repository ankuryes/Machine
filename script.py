import requests
from time import sleep
from urllib import parse as Encode1
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


while True:
    try:
        ip = str(requests.get("http://ipinfo.io/ip").text)
        
        Mn_urls = str(requests.get("https://raw.githubusercontent.com/AnkurKumarji/Machine/feat/add-feedback-section/Zagl.Links").text).splitlines()
        Selected_Link = str(requests.get("https://Armitage.ankurkumar8.repl.co/").text).split(".")
        if int(Selected_Link[1]) >= len(Mn_urls):
            requests.get("https://Armitage.ankurkumar8.repl.co/reset.php");Selected_Url = Mn_urls[0]
        else:
            Selected_Url = Mn_urls[int(Selected_Link[1])];print(len(Mn_urls), Selected_Link, Selected_Url)
        Selected_Url = Selected_Url.replace("zee.gl","za.gl")

        req = requests.Session()
        useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"

        headers = {"user-agent": useragent,"accept": "text/html", "sec-fetch-site": "none", "sec-fetch-mode": "navigate", "sec-fetch-dest": "document","accept-language": "en-GB,en;q=0.9"}
        res1 = req.get(Selected_Url, headers=headers)
        soup = BeautifulSoup(res1.text, 'html.parser')
        Token = Encode1.quote(soup.find('input', {'name': '_Token[fields]'})['value'])
        Token_unlocked = Encode1.quote(soup.find('input', {'name': '_Token[unlocked]'})['value'])
        givenX = Encode1.quote(soup.find('input', {'name': 'givenX'})['value'])
        givenY = Encode1.quote(soup.find('input', {'name': 'givenY'})['value'])
        data = str(soup.find('button',{'id': 'greendot'}).find('img')['src']).split('png;base64,')[1]
        base64data = list(str(requests.post("https://ImageCord.ankurkumar8.repl.co",data=data).text).replace('[','').replace(']','').replace(' ','').split(','))


        headers = {'Host': 'za.gl','User-Agent': useragent,'Accept': 'text/html','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://za.gl','Referer': Selected_Url}
        data = f'_method=POST&_csrfToken={res1.cookies.get_dict()["csrfToken"]}&ref=&f_n=slc&dot=1&givenX={givenX}&givenY={givenY}&X={base64data[0]}&Y={base64data[1]}&_Token%5Bfields%5D={Token}&_Token%5Bunlocked%5D={Token_unlocked}'
        res2 = req.post(Selected_Url, headers=headers,data=data,timeout=10)
        soup = BeautifulSoup(res2.content, 'lxml')
        ad_form = Encode1.quote(soup.find('input', {'name': 'ad_form_data'})['value'])
        Token = Encode1.quote(soup.find('input', {'name': '_Token[fields]'})['value'])
        Token_unlocked = Encode1.quote(soup.find('input', {'name': '_Token[unlocked]'})['value'])
        Cook = res1.cookies.get_dict()
        Cook.update(res2.cookies.get_dict())
        Cook.update({'ab':'2', 'ref':'adimin', 'sls':'0'})

        sleep(3)

        headers = {"accept": "application/json, text/javascript, */*; q=0.01", "x-requested-with": "XMLHttpRequest","user-agent": useragent,"content-type": "application/x-www-form-urlencoded; charset=UTF-8", "origin": "https://za.gl","sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty","referer": Selected_Url}
        cookies = {"AppSession": Cook['AppSession'],"zagl_publisher": Cook['zagl_publisher'],"scr": Cook['scr'],"csrfToken": Cook['csrfToken'],"visitor": Cook['visitor'],"hash": Cook['hash'],"sls": "0","ref": "admin","browserprint": "8b009e12f3bad328ce10f5803a223ca11621cb5cdb5a207dca519f2e50565610","overlay": "1","ab": "2","sb_main_29b552ac181cd0b221e0fcc9e06f6754": "1","slv": "-1","sb_count_29b552ac181cd0b221e0fcc9e06f6754": "1"}
        data = f"_method=POST&_csrfToken={Cook['csrfToken']}&ad_form_data={ad_form}&_Token%5Bfields%5D={Token}&_Token%5Bunlocked%5D={Token_unlocked}"
        mn_req = requests.post("https://za.gl/links/go", headers=headers, cookies=Cook, data=data, timeout=3)
        print(mn_req.text)

        # ----------------------------------------------------------------------------------

        # -----Request 1-------
        req1 = requests.get("https://droplink.co/Zagl")
        main_cook = req1.cookies.get_dict()
        # print(req1.text,main_cook)

        # -----Request 2-------
        headers = {'Host': 'yoshare.net','User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36','Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded'}
        data = 'clickarlink=Zagl'
        req2 = requests.post('https://yoshare.net/', headers=headers, data=data)
        redi_url = str(req2.text[str(req2.text).find('name="sujitsure4" action="') + 26:str(req2.text).find('name="sujitsure4" action="') + 100]).split('" method')[0]
        # print(req2.text, req2.cookies.get_dict(), redi_url)

        # -----Request 3-------
        headers = {'Host': 'yoshare.net', 'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36', 'Accept': 'text/html','Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'https://yoshare.net','Referer': 'https://yoshare.net/', 'Sec-Fetch-User': '?1'}
        data = 'clikarlink=Zagl&yuidea=&verify=Click+here+to+continue'
        req3 = requests.post(f'{redi_url}', headers=headers, data=data)
        # print(req3.text,req3.cookies.get_dict())

        # -----Request 4-------
        headers = {'Host': 'droplink.co', 'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36', 'Accept': 'text/html','Accept-Encoding': 'gzip, deflate', 'Referer': 'https://yoshare.net/', 'Sec-Fetch-User': '?1'}
        req4 = requests.get('https://droplink.co/Zagl', headers=headers, cookies=main_cook)
        ad_form = Encode1.quote(str(req4.text[str(req4.text).find('ad_form_data" value="') + 21:str(req4.text).find('ad_form_data" value="') + 500]).split('" />')[0])
        Token = Encode1.quote(str(req4.text[str(req4.text).find('_Token[fields]" autocomplete="off" value="') + 42:str(req4.text).find('_Token[fields]" autocomplete="off" value="') + 200]).split('" />')[0])
        Token_unlocked = Encode1.quote(str(req4.text[str(req4.text).find('_Token[unlocked]" autocomplete="off" value="') + 44:str(req4.text).find('_Token[unlocked]" autocomplete="off" value="') + 200]).split('" />')[0])
        # print(req4.text,req4.cookies.get_dict(),main_cook)

        sleep(3)

        # -----Request 5-------
        main_cook['ab'] = '2'
        # main_cook['AdskeeperStorage'] = str(Encode1.quote('{"0":{},"C1144333":{"page":1,"time":1629891515406}}'))
        headers = {'Host': 'droplink.co', 'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36', 'Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'X-Requested-With': 'XMLHttpRequest','Origin': 'https://droplink.co', 'Referer': 'https://droplink.co/Zagl', 'Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin'}
        data = f"_method=POST&_csrfToken={main_cook['csrfToken']}&ad_form_data={ad_form}&_Token%5Bfields%5D={Token}&_Token%5Bunlocked%5D={Token_unlocked}"
        Fnl_req = requests.post('https://droplink.co/links/go', headers=headers, cookies=main_cook, data=data)

        print("Droplink",Fnl_req.text)


        while True:
            new_ip = str(requests.get("http://ipinfo.io/ip").text)
            if ip != new_ip:break
            else:sleep(3)
    except: sleep(2)
