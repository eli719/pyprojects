import time

import requests
import json
import re
import os

headers={
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

response=requests.get('https://www.vmgirls.com/13344.html',headers=headers)

html=response.text

dir_name=re.findall('<h1 class="post-title h3">(.*?)</h1>',html)[-1]
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
urls= re.findall('<a href="(.*?)" alt=".*?" title=".*?">',html)

for url in urls:
    time.sleep(1)
    print(url)
    file_name = url.split('/')[-1]
    response = requests.get(url,headers=headers)
    with open(dir_name+"/"+file_name,'wb') as f:
        f.write(response.content)

