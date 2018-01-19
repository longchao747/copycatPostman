# 动态创建类

from abc import abstractmethod, abstractproperty


class Hander:
    def __init__(self):
        pass

    def createurl(self, baseurl, url):
        return baseurl + url


def add(a, b):
    return a + b


class Headers:
    def __init__(self):
        print('调用了init方法')
        pass

    @abstractmethod
    def getBaiduHeadres(self):
        pass

    def run(self):
        print("haha")

    def __new__(cls, *args, **kwargs):
        print('调用了new方法')
        return object.__new__(cls, *args, **kwargs)


class_map = {
    "haha": Headers
}

head1 = Headers()
print(type(head1))

# head2 = Headers.__new__(Headers)
# Headers.__init__(head2)

cls_obj = class_map.get("haha")
print(type(cls_obj))

cls = cls_obj.__new__(cls_obj)
cls_obj.__init__(cls)
print(type(cls))
cls.run()
