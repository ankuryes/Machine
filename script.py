from os import system
system("pip install bs4 >null")
system("pip install lxml >null")
import base64
import requests
from time import sleep
from threading import Thread
from urllib import parse as Encode1
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def Main_dta(): 
  # -----Request 1-------
  req1 = requests.get("https://droplink.co/Zagl")
  main_cook = req1.cookies.get_dict()
  # print(req1.text,main_cook)

  # -----Request 2-------
  headers = {'Host': 'yoshare.net','User-Agent': 'Mozilla/5.0','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded'}
  data = 'clickarlink=Zagl'
  req2 = requests.post('https://yoshare.net/', headers=headers,data=data)
  soup = BeautifulSoup(req2.content, 'lxml')
  redi_url = str(soup.find("form", {"id": "yuidea"})['action'])
  # print(req2.text,req2.cookies.get_dict(),redi_url)

  # -----Request 3-------
  headers = {'Host': 'yoshare.net','User-Agent': 'Mozilla/5.0','Accept': 'text/html','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://yoshare.net','Referer': 'https://yoshare.net/','Sec-Fetch-User': '?1'}
  data = 'clikarlink=Zagl&yuidea=&verify=Click+here+to+continue'
  req3 = requests.post(f'{redi_url}', headers=headers,data=data)
  # print(req3.text,req3.cookies.get_dict())

  # -----Request 4-------
  headers = {'Host': 'droplink.co','User-Agent': 'Mozilla/5.0','Accept': 'text/html','Accept-Encoding': 'gzip, deflate','Referer': 'https://yoshare.net/','Sec-Fetch-User': '?1'}
  req4 = requests.get('https://droplink.co/Zagl', headers=headers, cookies=main_cook)
  soup = BeautifulSoup(req4.content, 'lxml')
  ad_form,Token,Token_unlocked = Encode1.quote(soup.find('input',{'name': 'ad_form_data'})['value']),Encode1.quote(soup.find('input',{'name': '_Token[fields]'})['value']),Encode1.quote(soup.find('input',{'name': '_Token[unlocked]'})['value'])
  # print(req4.text,req4.cookies.get_dict(),main_cook)

  sleep(3)
  # -----Request 5-------
  main_cook['ab'] = '2'
  # main_cook['AdskeeperStorage'] = str(Encode1.quote('{"0":{},"C1144333":{"page":1,"time":1629891515406}}'))
  headers = {'Host': 'droplink.co','User-Agent': 'Mozilla/5.0s','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest','Origin': 'https://droplink.co','Referer': 'https://droplink.co/Zagl','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin'}
  data = f"_method=POST&_csrfToken={main_cook['csrfToken']}&ad_form_data={ad_form}&_Token%5Bfields%5D={Token}&_Token%5Bunlocked%5D={Token_unlocked}"

  Fnl_req = requests.post('https://droplink.co/links/go', headers=headers, cookies=main_cook, data=data)
  print(Fnl_req.text,Fnl_req.cookies.get_dict(),"Ankur Kumar")
  return str(Fnl_req.text)

Main_dta()
