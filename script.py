# from os import system
# system("pip install bs4 >null")
# system("pip install lxml >null")
# import base64,random
# import requests
# from time import sleep
# import datetime
# from flask import Flask
# from threading import Thread
# from urllib import parse as Encode1
# from bs4 import BeautifulSoup
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# system("clear")

# app = Flask('')
# @app.route('/')
# def home():
#     resp = Main_dta()
#     return str(resp)

# def run():
#   app.run(host='0.0.0.0',port=random.randint(2000, 9000))

# def keep_alive():
#     t = Thread(target=run)
#     t.start()

# def Main_dta(): 
# 	Mn_urls = str(requests.get("https://raw.githubusercontent.com/AnkurKumarji/Machine/feat/add-feedback-section/Zagl.Links").text).splitlines()
# 	Selected_Link = str(requests.get("https://Armitage.ankurkumar8.repl.co").text).split(".")
# 	if len(Mn_urls)<=int(Selected_Link[1]): Selected_Url = Mn_urls[0];requests.get("https://Armitage.ankurkumar8.repl.co/reset.php")
# 	else:
# 		Selected_Url = Mn_urls[int(Selected_Link[1])]
# 		print(len(Mn_urls),Selected_Link,Selected_Url)
	 
# 	s,url = 'Ankur Kumar',"https://za.gl/links/go"
# 	headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36", "accept": "text/html", "sec-fetch-site": "none", "sec-fetch-mode": "navigate", "sec-fetch-dest": "document", "accept-language": "en-GB,en;q=0.9"}
# 	response = requests.get(Selected_Url,headers=headers)
# 	Cook = response.cookies.get_dict()
# 	soup = BeautifulSoup(response.content, 'lxml')
# 	ad_form,Token,Token_unlocked = Encode1.quote(soup.find('input',{'name': 'ad_form_data'})['value']),Encode1.quote(soup.find('input',{'name': '_Token[fields]'})['value']),Encode1.quote(soup.find('input',{'name': '_Token[unlocked]'})['value'])
# 	sleep(3)
# 	headers = {"accept": "application/json, text/javascript, */*; q=0.01", "x-requested-with": "XMLHttpRequest", "user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "origin": "https://za.gl", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://za.gl/yesankur", "accept-language": "en-GB,en;q=0.9"}
# 	cookies = {"AppSession": Cook['AppSession'], "zagl_publisher": Cook['zagl_publisher'], "scr": Cook['scr'], "csrfToken": Cook['csrfToken'], "visitor": Cook['visitor'], "hash": Cook['hash'], "sls": "0", "ref": "admin", "browserprint": "724483257531cc15c2c696e1c3b033a425feed4e3c8d0bfd759c5fe964cc61f5", "overlay": "1", "ab": "2", "sb_main_29b552ac181cd0b221e0fcc9e06f6754": "1", "slv": "-1", "sb_count_29b552ac181cd0b221e0fcc9e06f6754": "1", "pbpr0tpuw4isk85t8yg3jb2lj5vqf": "wilfulpessimistic.com", "_ga": "GA1.2.1726704085.1610002127", "_gid": "GA1.2.394003706.1610002127", "_gat_gtag_UA_120643151_1": "1"}
# 	data = f"_method=POST&_csrfToken={Cook['csrfToken']}&ad_form_data={ad_form}&_Token%5Bfields%5D={Token}&_Token%5Bunlocked%5D={Token_unlocked}"
# 	response = requests.post(url,headers=headers,cookies=cookies,data=data)
# 	resp = response.text
# 	print(response.text)
# 	print(base64.b64encode(s.encode('ascii')))
# 	return str(resp)

# keep_alive()
# while True:
# 	while True:
# 		sleep(24*61*60)
# 	sleep(60*5)


from selenium import webdriver
import requests
from selenium.webdriver.chrome.options import Options

Mn_urls = str(requests.get("https://raw.githubusercontent.com/AnkurKumarji/Machine/feat/add-feedback-section/Zagl.Links").text).splitlines()
Selected_Link = str(requests.get("https://Armitage.ankurkumar8.repl.co").text).split(".")
if len(Mn_urls)<=int(Selected_Link[1]): Selected_Url = Mn_urls[0];requests.get("https://Armitage.ankurkumar8.repl.co/reset.php")
else:
	Selected_Url = Mn_urls[int(Selected_Link[1])]
	print(len(Mn_urls),Selected_Link,Selected_Url)
  
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get(Selected_Url)
