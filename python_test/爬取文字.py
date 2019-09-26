# -*- coding:UTF-8 -*-
import requests

if __name__ == '__main__':
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(url=target).content.decode('gbk','ignore')
    print(req.title())