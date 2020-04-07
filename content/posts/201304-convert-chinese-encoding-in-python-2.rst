python 2.x 中文编码格式转换
######################################


:author: Rex Zhang
:date: 2013-04-03T01:12:54+08:00
:modified: 2013-04-03T01:12:54+08:00
:status: published
:category: Coding
:tags: unicode, Python


.. code-block:: python

    #!/usr/bin/env python
    #coding=utf-8

    uuu = u'中文'
    print type(uuu), uuu

    sss = uuu.encode('gbk')
    print type(sss), sss

    nnn = unicode(sss, 'gbk')
    print type(nnn), nnn

输出为

.. code-block::

    <type 'unicode'> 中文
    <type 'str'> 中文
    <type 'unicode'> 中文
