import time

import requests

# 设置请求的URL
url = 'http://127.0.0.1:8080/register'

for item in range(100,201):
    # 设置请求的数据
    data = {'name': 'a{0}'.format(str(item)), 'password': '123456','confirm_password': '123456'}

    time.sleep(1)

    # 发送post请求
    response = requests.post(url, data=data)

    # 获取响应结果
    print(response.text)
