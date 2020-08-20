import time

import requests


def get_one_page(url, headers):
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        return response.content.decode("utf-8")
    return None


def login(url,headers,data):
    response = requests.post(url, headers=headers,data=data)
    if response.status_code == 200:
        return response.content.decode("utf-8")
    return None

if __name__ == '__main__':
    url = "http://220.163.129.204:7788/#/login"
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    data = {
        "params": "{\"type\":\"read\",\"userid\":\"''\",\"commandcode\":\"Ruser\",\"returndata\":0,\"inparameters\":{\"userid\":\"''\",\"username\":\"'西安杨森'\",\"pwd\":\"'81dc9bdb52d04dc20036dbd8313ed055'\"}}"
        }
    login(url, headers, data)