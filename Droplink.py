import requests
from time import sleep
from bs4 import BeautifulSoup
from urllib import parse as Encode1
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def internet_on():
    try: requests.get('https://www.google.com/');return True
    except: return False

while True:
    try:
        useragent = str(requests.get("https://urlshortxSelectLink.ankurkumar8.repl.co").text)

        try: ip = str(requests.get("https://jsonip.com/").json()['ip'])
        except: ip = str(requests.get("http://ipinfo.io/ip").text)

        print("+",ip)

        try:
            #urlshortx.com Req1
            urlshortx = str(requests.get("https://urlshortxSelectLink.ankurkumar8.repl.co").text)
            shortx_headers = {'Host': 'm.bdnewsx.com','User-Agent': useragent,'Accept': 'text/html','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate','Referer': 'https://techrfour.com/2021/05/17/top-reason-to-buy-a-child-education-insurance-plan/'}
            shortx_res1 = requests.get(urlshortx , headers=shortx_headers)
            shortx_Cook = shortx_res1.cookies.get_dict()
            shortx_Cook.update({'ab': '2','prefetchAd_3113442': 'true'})

            soup = BeautifulSoup(shortx_res1.text, 'html.parser')
            shortx_ad_form = Encode1.quote(soup.find('input', {'name': 'ad_form_data'})['value'])
            shortx_Token = Encode1.quote(soup.find('input', {'name': '_Token[fields]'})['value'])
            shortx_Token_unlocked = Encode1.quote(soup.find('input', {'name': '_Token[unlocked]'})['value'])
        except:pass

        #Droplink.co Req1
        drop_Select_link = str(requests.get("https://selectlink.ankurkumar8.repl.co/").text)
        drop_req1 = requests.get(drop_Select_link)
        drop_main_cook = drop_req1.cookies.get_dict()

        drop_headers = {'Host': 'yoshare.net', 'User-Agent': useragent, 'Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded'}
        drop_data = 'clickarlink=Zagl'
        drop_req2 = requests.post('https://yoshare.net/', headers=drop_headers, data=drop_data)
        soup = BeautifulSoup(drop_req2.text, 'html.parser')
        redi_url = str(soup.find("form", {"id": "yuidea"})['action'])

        drop_headers = {'Host': 'yoshare.net', 'User-Agent': useragent, 'Accept': 'text/html', 'Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://yoshare.net', 'Referer': 'https://yoshare.net/', 'Sec-Fetch-User': '?1'}
        drop_data = f'clikarlink={drop_Select_link.split("droplink.co/")[1]}&yuidea=&verify=Click+here+to+continue'
        drop_req3 = requests.post(f'{redi_url}', headers=drop_headers, data=drop_data)

        drop_headers = {'Host': 'droplink.co', 'User-Agent': useragent, 'Accept': 'text/html', 'Accept-Encoding': 'gzip, deflate','Referer': 'https://yoshare.net/', 'Sec-Fetch-User': '?1'}
        drop_req4 = requests.get(drop_Select_link, headers=drop_headers, cookies=drop_main_cook)
        soup = BeautifulSoup(drop_req4.text, 'html.parser')
        drop_ad_form = Encode1.quote(soup.find('input', {'name': 'ad_form_data'})['value'])
        drop_Token = Encode1.quote(soup.find('input', {'name': '_Token[fields]'})['value'])
        drop_Token_unlocked = Encode1.quote(soup.find('input', {'name': '_Token[unlocked]'})['value'])


        #Za.gl Req1
        Selected_Url = str(requests.get("https://SelectZagl.ankurkumar8.repl.co").text)

        req = requests.Session()
        zagl_headers = {"user-agent": useragent, "accept": "text/html", "sec-fetch-site": "none", "sec-fetch-mode": "navigate","sec-fetch-dest": "document", "accept-language": "en-GB,en;q=0.9"}
        zagl_res1 = req.get(Selected_Url, headers=zagl_headers)
        soup = BeautifulSoup(zagl_res1.text, 'html.parser')
        zagl_Token = Encode1.quote(soup.find('input', {'name': '_Token[fields]'})['value'])
        zagl_Token_unlocked = Encode1.quote(soup.find('input', {'name': '_Token[unlocked]'})['value'])
        givenX = Encode1.quote(soup.find('input', {'name': 'givenX'})['value'])
        givenY = Encode1.quote(soup.find('input', {'name': 'givenY'})['value'])
        data = str(soup.find('button', {'id': 'greendot'}).find('img')['src']).split('png;base64,')[1]
        base64data = list(str(requests.post("https://ImageCord.ankurkumar8.repl.co", data=data).text).replace('[', '').replace(']','').replace(' ', '').split(','))

        zagl_headers = {'Host': 'za.gl', 'User-Agent': useragent, 'Accept': 'text/html', 'Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://za.gl', 'Referer': Selected_Url}
        zagl_data = f'_method=POST&_csrfToken={zagl_res1.cookies.get_dict()["csrfToken"]}&ref=&f_n=slc&dot=1&givenX={givenX}&givenY={givenY}&X={base64data[0]}&Y={base64data[1]}&_Token%5Bfields%5D={zagl_Token}&_Token%5Bunlocked%5D={zagl_Token_unlocked}'
        zagl_res2 = req.post(Selected_Url, headers=zagl_headers, data=zagl_data)
        soup = BeautifulSoup(zagl_res2.text, 'html.parser')
        zagl_ad_form = Encode1.quote(soup.find('input', {'name': 'ad_form_data'})['value'])
        zagl_Token = Encode1.quote(soup.find('input', {'name': '_Token[fields]'})['value'])
        zagl_Token_unlocked = Encode1.quote(soup.find('input', {'name': '_Token[unlocked]'})['value'])
        zagl_Cook = zagl_res1.cookies.get_dict()
        zagl_Cook.update(zagl_res2.cookies.get_dict())
        zagl_Cook.update({'ab': '2', 'ref': 'adimin', 'sls': '0', 'overlay': '1'})

        sleep(4)

        #Earning requests...........................................................................
        #Droplink
        drop_main_cook['ab'] = '2'
        drop_headers = {'Host': 'droplink.co', 'User-Agent': useragent, 'Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'X-Requested-With': 'XMLHttpRequest','Origin': 'https://droplink.co', 'Referer': drop_Select_link, 'Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin'}
        drop_data = f"_method=POST&_csrfToken={drop_main_cook['csrfToken']}&ad_form_data={drop_ad_form}&_Token%5Bfields%5D={drop_Token}&_Token%5Bunlocked%5D={drop_Token_unlocked}"

        drop_Mn_req = requests.post('https://droplink.co/links/go', headers=drop_headers, cookies=drop_main_cook, data=drop_data)
        if "Go With earning :)" in drop_Mn_req.text:print('Req1')
        else: print('Req1_Err.')

        try:
            #urlshortx
            shortx_headers = {'Host': 'm.bdnewsx.com','User-Agent': useragent,'Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest','Origin': 'https://m.bdnewsx.com','Referer': urlshortx,'Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers'}
            shortx_data = f'_method=POST&_csrfToken={shortx_Cook["csrfToken"]}&ad_form_data={shortx_ad_form}&_Token%5Bfields%5D={shortx_Token}&_Token%5Bunlocked%5D={shortx_Token_unlocked}'
            shortx_Mn_req = requests.post('https://m.bdnewsx.com/links/go', headers=shortx_headers, cookies=shortx_Cook, data=shortx_data)
            # if "Go With earning :)" in shortx_Mn_req.text:print('Req working')
            # else: print('Req_shortx_Err. short')
        except:pass

        #zagl
        zagl_headers = {"accept": "application/json, text/javascript, */*; q=0.01", "x-requested-with": "XMLHttpRequest","user-agent": useragent, "content-type": "application/x-www-form-urlencoded; charset=UTF-8","origin": "https://za.gl", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors","sec-fetch-dest": "empty", "referer": Selected_Url}
        zagl_data = f"_method=POST&_csrfToken={zagl_Cook['csrfToken']}&ad_form_data={zagl_ad_form}&_Token%5Bfields%5D={zagl_Token}&_Token%5Bunlocked%5D={zagl_Token_unlocked}"
        zagl_Mn_req = requests.post("https://za.gl/links/go", headers=zagl_headers, cookies=zagl_Cook, data=zagl_data, timeout=3)
        if "Go With earning :)" in zagl_Mn_req.text:print('Req2')
        else:print('Req2_Err.')

        print('Complete')

        while True:
            try : new_ip = str(requests.get("https://jsonip.com/").json()['ip'])
            except: new_ip = str(requests.get("http://ipinfo.io/ip").text)
            if (new_ip!=ip) and (internet_on()==True):break
            sleep(3)
    except:
        while True:
            if internet_on() == True:break
            sleep(2)
