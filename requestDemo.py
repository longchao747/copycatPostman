# coding=utf-8
import json
import requests
import ModelDemo

# 安装requests: pip install requests

baseurl = "http://192.168.199.228:8000"
api1 = "/api/lottery"
api2 = "/api/getlotterybyid"
api3 = "/api/getlotterycodehighrate"

baiduUrl = "http://www.baidu.com"


def getRequest():
    """get请求"""

    # 发送get请求
    demo = ModelDemo.Hander()
    url = demo.createurl(baseurl, api1)
    print (url)

    print (ModelDemo.add(1,2))


    res = requests.get(baseurl + api1)

    content = res.content
    print (content)
    print (res.text)

    # 请求参数
    payload = {'key1': 'value1', 'key2': 'value2'}

    res = requests.get("http://httpbin.org/get", params=payload)  # 注意是params参数

    # requests 会自动帮我们拼接请求地址
    # url= http://httpbin.org/get?key1=value1&key2=value2

    # 针对get请求使用的即使params参数，post请求使用的是data参数


def postRequest():
    """post请求"""

    params = {"id": "17149"}

    # 发送post请求 表单提交
    res = requests.post(baseurl + api2, data=params)  # 注意是data参数
    print (res.content)

    # post提交 json对象数据
    # 第一种方式 此方式还需要手动添加 application/json，不建议使用
    res = requests.post(baseurl + api2, data=json.dumps(params))
    print (res.content)

    # 第二种方式 此方式会自动添加 application/json 建议使用
    res = requests.post(baseurl + api2, json=params)
    print (res.content)


def createHeader():
    """构造请求头"""
    headers = {'user-agent': 'my-app/0.0.1'}
    res = requests.get(baiduUrl, headers=headers)


def createCookies():
    """构造cookies"""
    cookies = dict(sessionId="Jsession31313")
    requests.get(baseurl + api1, cookies=cookies)


def timeoutRequest():
    """设置请求超时时间"""
    requests.get(baseurl + api1, timeout=0.01)  # 超时时间：0.01秒


def responseContent():
    """response响应内容"""
    res = requests.get(baiduUrl)
    content = res.content  # 原始二进制数据

    # 大部分情况使用这个方法
    text = res.text  # 文本数据信息，requests自动帮我们以指定编码解析出来的内容

    # 响应json数据信息，通常我们使用json模块来处理
    json_data = res.json

    # 响应状态码
    status_code = res.status_code

    # 响应头
    headers = res.headers
    print (headers)

    # 响应cookies
    cookies = res.cookies


if __name__ == '__main__':
    getRequest()
    # postRequest()
    # createHeader()
    # createCookies()
    # timeoutRequest()
    # responseContent()
    pass
