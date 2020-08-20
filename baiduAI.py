import requests
import base64

'''
通用文字识别（高精度版）
'''
# appId=18133392
# apiKey='AoB0l1kaD644BWz0KWxKDwTc'
# secretKey='2xKmo6y4UukKz2ivZ7WjoD03MFalCXYL'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=AoB0l1kaD644BWz0KWxKDwTc&client_secret=2xKmo6y4UukKz2ivZ7WjoD03MFalCXYL'
response = requests.get(host)
if response:
    print(response.json())

s=response.json().get('access_token')

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 二进制方式打开图片文件
image_name='image_del_crop1.jpg'
f = open(image_name, 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = s
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())