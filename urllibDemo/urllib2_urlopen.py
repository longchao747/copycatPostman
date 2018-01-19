# coding=utf-8
# urllib2 在 python3.x 中被改为urllib.request

import urllib.request

# 向指定的url发送请求，并返回服务器响应的类文件对象
response = urllib.request.urlopen("http://www.baidu.com")

# 类文件对象支持 文件对象的操作方法，如read()方法读取文件全部内容，返回字符串
html = response.read()

print(html)


