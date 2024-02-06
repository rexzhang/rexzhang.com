Python map class/类结构体 相互转换
###################################

:author: Rex Zhang
:date: 2014-10-17T01:18:01+08:00
:modified: 2014-10-17T01:18:01+08:00
:status: published
:category: Coding
:tags: Python

.. code-block:: python

    #!/usr/bin/env python
    #coding=utf-8

    #----------------------------------------------------------------------
    def obj2map(obj):
        """"""
        return vars(obj)

    ########################################################################
    class obj:
        def __init__(self):
            self.a = 1
            self.b = 2

    ########################################################################
    class map2struct:
        def __init__(self, **entries):
            self.__dict__.update(entries)

    o = obj()

    print '~~~~~~~~~~~~~~ obj -> map ~~~~~~~~~~~~~~'
    m = vars(o)
    print type(m), m

    print '~~~~~~~~~~~~~~ map -> obj ~~~~~~~~~~~~~~'
    o2 = map2struct(**m)
    print type(o2), o2
    print o2.a, o2.b

    print '~~~~~~~~~~~~~~ map -maker-> obj ~~~~~~~~~~~~~~'
    from collections import namedtuple
    sMaker = namedtuple('structMaker', 'a b c')
    print sMaker

    s = sMaker(a=1, b={'b': 2}, c=['c', 3])
    print s
    print s.a
    print s.b
    print s.c

输出内容

.. code-block:: text

    ~~~~~~~~~~~~~~ obj -> map ~~~~~~~~~~~~~~
    <type 'dict'> {'a': 1, 'b': 2}
    ~~~~~~~~~~~~~~ map -> obj ~~~~~~~~~~~~~~
    <type 'instance'> <__main__.map2struct instance at 0x10f0c07e8>
    1 2
    ~~~~~~~~~~~~~~ map -maker-> obj ~~~~~~~~~~~~~~
    <class '__main__.structMaker'>
    structMaker(a=1, b={'b': 2}, c=['c', 3])
    1
    {'b': 2}
    ['c', 3]
