# urllib 和 urllib2 都是接受URL请求的相关模块，但是提供了不同的功能。两个最显著的不同如下：
# urllib 仅可以接受URL，不能创建 设置了headers 的Request 类实例；
#
# 但是 urllib 提供 urlencode 方法用来GET查询字符串的产生，而 urllib2 则没有。
# （这是 urllib 和 urllib2 经常一起使用的主要原因）
#
# 编码工作使用urllib的urlencode()函数，帮我们将key:value这样的键值对转换成"key=value"这样的字符串，
# 解码工作可以使用urllib的unquote()函数。（注意，不是urllib2.urlencode() )

import urllib.parse

word = {"wd": "传智"}
print(word)

# 通过urllib.urlencode()方法，将字典键值对按URL编码转换，从而能被web服务器接受。
urlencode = urllib.parse.urlencode(word) # 在python 2.*中，直接使用urllib.urlencode(word)
print(urlencode)

# 通过urllib.unquote()方法，把 URL编码字符串，转换回原先字符串。
print(urllib.parse.unquote("wd=%E4%BC%A0%E6%99%BA"))
