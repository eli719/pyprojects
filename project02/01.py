import requests as req
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
'Accept-Language':'zh-CN,zh;q=0.9',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
}
proxies = {
  "https": "http://41.65.244.27:8080",
}

response = req.get("https://www.baidu.com/", proxies=proxies,headers=headers)
print(response.text)
print(response.status_code)
# req.packages.urllib3.disable_warnings()
# response = req.get('https://www.ygdy8.net/html/gndy/china/index.html',headers=headers)
# print(response.status_code)
# print(response.text)
# response = req.get('http://www.nmpa.gov.cn/WS04/CL2042/',headers=headers)
# print(response.status_code)
# response = req.get('http://app1.nmpa.gov.cn/datasearchcnda/face3/dir.html',headers=headers)
# print(response.status_code)
# response = req.get('http://app1.nmpa.gov.cn/datasearchcnda/face3/base.jsp?tableId=34&tableName=TABLE34&title=%E8%8D%AF%E5%93%81%E7%94%9F%E4%BA%A7%E4%BC%81%E4%B8%9A&bcId=152911762991938722993241728138',headers=headers)
# print(response.text)
# print(response.status_code)
# while response.status_code==202:
#     response = req.get(
#         'http://app1.nmpa.gov.cn/datasearchcnda/face3/base.jsp?tableId=34&tableName=TABLE34&title=%E8%8D%AF%E5%93%81%E7%94%9F%E4%BA%A7%E4%BC%81%E4%B8%9A&bcId=152911762991938722993241728138',
#         headers=headers)
#     if response.status_code==200:
#         pass
# print(response.text)