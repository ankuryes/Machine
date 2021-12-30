# from os import system
# try:system("rm -f poetry.lock");system("rm -f pyproject.toml")
# except:pass
# import requests
# from flask import Flask
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# app = Flask('')

# @app.route('/')
# def home():
#     try: ip = str(requests.get("https://jsonip.com/").json()['ip'])
#     except: ip = str(requests.get("http://ipinfo.io/ip").text)

#     data = str(ip)
#     dta = requests.post('https://Ips.ankurkumar8.repl.co/found', data=data).text
#     return str(dta)

# app.run(host='0.0.0.0', port=8080)
from os import system
system("pip install bs4")
ststem("pip install PIL")
import requests
from time import sleep
from bs4 import BeautifulSoup
from urllib import parse as Encode1
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
req = requests.Session()

#-------------Zagl Captcha Solver-----------------------------------------
import base64
from PIL import Image
from io import BytesIO
def get_Color_Pixel_Cordinate(data, color=(56, 178, 73)):
    image = Image.open(BytesIO(base64.b64decode(data))).convert('RGB').resize((300, 300))

    Total_pixel = []
    for x in range(0, image.size[0]):
        for y in range(0, image.size[1]):
            if image.getpixel((x, y)) == color: Total_pixel.append((x, y))

    click_ele = list(Total_pixel[532])
    return click_ele


def internet_on():
    try:
        global System_IP
        req.get('https://www.google.com/')
        try: System_IP = str(req.get("https://jsonip.com/").json()['ip'])
        except: System_IP = str(req.get("http://ipinfo.io/ip").text)
        print('+',System_IP)
        return str(System_IP)
    except: return False
# ________________________________________________________________________

System_IP = ""
if bool(internet_on())==True:
    url = "https://za.uy/myhello4299"

    sp_url = url.split('/')
    headers = {
        'Host': sp_url[2],
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://web.telegram.org/'
    }
    res1 = req.get(url, headers=headers)
    res1_cookies = res1.cookies.get_dict();res1_cookies.update({'ab': '2'})
    soup = BeautifulSoup(res1.text, 'html.parser')
    Token = Encode1.quote(soup.find('input', {'name': '_Token[fields]'})['value'])
    Token_unlocked = Encode1.quote(soup.find('input', {'name': '_Token[unlocked]'})['value'])
    givenX = Encode1.quote(soup.find('input', {'name': 'givenX'})['value'])
    givenY = Encode1.quote(soup.find('input', {'name': 'givenY'})['value'])
    data = str(soup.find('button', {'id': 'greendot'}).find('img')['src']).split('png;base64,')[1]
    base64data = list(str(get_Color_Pixel_Cordinate(data)).replace('[', '').replace(']', '').replace(' ', '').split(','))
    print('Task 1',base64data)


    headers = {
        'Host': sp_url[2],
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': f'{sp_url[0]}//{sp_url[2]}',
        'Referer': url,
    }
    data = f'_method=POST&_csrfToken={res1_cookies["csrfToken"]}&ref={Encode1.quote(url)}&f_n=slc&dot=1&givenX={givenX}&givenY={givenY}&X={base64data[0]}&Y={base64data[1]}&_Token%5Bfields%5D={Token}&_Token%5Bunlocked%5D={Token_unlocked}'
    res2 = requests.post(url, headers=headers, cookies=res1_cookies, data=data)
    res2_cookies = res2.cookies.get_dict();res2_cookies.update(res1_cookies)
    soup = BeautifulSoup(res2.text, 'html.parser')
    ad_form = Encode1.quote(soup.find('input', {'name': 'ad_form_data'})['value'])
    Token = Encode1.quote(soup.find('input', {'name': '_Token[fields]'})['value'])
    Token_unlocked = Encode1.quote(soup.find('input', {'name': '_Token[unlocked]'})['value'])
    print('Task 2',res2_cookies)

    sleep(5)
    headers.update({'X-Requested-With': 'XMLHttpRequest'})
    data = f'_method=POST&_csrfToken={res2_cookies["csrfToken"]}&ad_form_data={ad_form}&_Token%5Bfields%5D={Token}&_Token%5Bunlocked%5D={Token_unlocked}'
    res3 = req.post(f'https://{sp_url[2]}/links/go', headers=headers, cookies=res2_cookies, data=data)
    print('Complete',res3.text)
