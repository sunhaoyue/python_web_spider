# -*- coding:UTF-8 -*-
import requests

if __name__ == '__main__':
    target = 'http://gitbook.cn/'
    req = requests.get(url=target)
    print(req.text)
