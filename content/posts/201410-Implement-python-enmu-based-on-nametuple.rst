一个简洁的基于  namedtuple 的 Python 枚举实现
#############################################

:author: Rex Zhang
:date: 2014-10-30T02:04:45+08:00
:modified: 2014-10-30T02:04:45+08:00
:status: published
:category: Coding
:tags: Python

查找比对的时候是数值类型，性能还是很不错的

.. code-block:: python

    from collections import namedtuple

    def MakeEnum(enumList):
        return namedtuple('Enum', enumList)._make(range(len(enumList)))

    USER_AT = MakeEnum(['noLogined', 'logined', 'hall', 'room'])


    print USER_AT, type(USER_AT)

    print USER_AT.noLogined, type(USER_AT.noLogined)

    print USER_AT._fields[USER_AT.noLogined], type(USER_AT._fields[USER_AT.noLogined])

输出为

.. code-block:: text

    Enum(noLogined=0, logined=1, hall=2, room=3) <class '__main__.Enum'>
    0 <type 'int'>
    noLogined <type 'str'>

参考
----
- http://pythonpath.wordpress.com/2012/01/26/python-enum-with-namedtuple
- http://www.360doc.com/content/14/0417/23/9482_369900781.shtml
