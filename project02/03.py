import requests
from urllib import request

if __name__ == "__main__":
    #访问网址
    url = 'https://www.baidu.com/'
    #这是代理IP
    proxy = {'https':'41.65.244.27:8080'}
    #创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    #创建Opener
    opener = request.build_opener(proxy_support)
    #添加User Angent
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    #安装OPener
    request.install_opener(opener)
    #使用自己安装好的Opener
    response = request.urlopen(url)
    #读取相应信息并解码
    html = response.read().decode("utf-8")
    #打印信息
    print(html)


# proxy = {
#     'http':'183.89.154.2:8080',
#     'https':'113.195.232.219:9999'
#
# }
# proxy_support = request.ProxyHandler(proxy)
# response=requests.get("http://httpbin.org/ip",proxies=proxy)
#
# print(response.text)