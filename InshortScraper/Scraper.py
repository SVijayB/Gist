import json
import requests

import redis
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
#redis = redis.Redis(host='localhost',port='6379')
headers={
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36',
}
s = requests.Session()
s.headers=headers

r=s.get("https://www.inshorts.com/en/read",proxies=proxies,verify=False)

response=r.text
print(response.split("min_news_id = \"")[1].split("\"")[0])

offset=response.split("min_news_id = \"")[1].split("\"")[0]
print(s.headers)
data={
"category": "",
"news_offset": f"{offset}"
}


jsonData=json.dumps(data)
print(jsonData)
r=s.post("https://inshorts.com/en/ajax/more_news",data=f"category=&news_offset={offset}",proxies=proxies,verify=False)
print(s.headers)

#redis.set('mykey',str(r.json()))

print(r.text)


'''headers={
"Sec-Ch-Ua": 'Not;A=Brand";v="99", "Chromium";v="106',
"Accept": "*/*",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"X-Requested-With": "XMLHttpRequest",
"Sec-Ch-Ua-Mobile": "?0",
"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36',
"Sec-Ch-Ua-Platform": "Windows",
"Origin": "https://www.inshorts.com",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Referer": "https://www.inshorts.com/en/read",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "en-US,en;q=0.9"
}'''