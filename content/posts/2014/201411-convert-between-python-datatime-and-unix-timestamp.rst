Convert between python datetime and unix timestamp
###################################################

:author: Rex Zhang
:date: 2014-11-11T02:35:08+08:00
:modified: 2015-01-28T02:35:08+08:00
:status: published
:category: Coding
:tags: Python

代码
----

.. code-block:: python

    import datetime, calendar, time

    def timestamp2datetime(timestamp):
        return datetime.datetime.fromtimestamp(timestamp)

    def date2timestamp(date):
        """local time"""
        return calendar.timegm(date.timetuple())

    def date2timestamp_utc(date):
        """utc time"""
        return int(time.mktime(date.timetuple()))

    def datetime2timestamp(year, month, day):
        return calendar.timegm(datetime.datetime(year, month, day).timetuple())

    def time2timestamp(python_time):
        return int(python_time)

    year = 2014
    month = 10
    day = 23
    timestamp = datetime2timestamp(year, month, day)
    print timestamp

    today = datetime.datetime.today()
    timestamp = date2timestamp(today)
    print timestamp
    timestamp = date2timestamp_utc(today)
    print timestamp

    date = timestamp2datetime(timestamp)
    print date

    timestamp = time2timestamp(time.time())
    print timestamp

输出
----

.. code-block:: text

    1414022400
    local timestamp: 1422462994
    utc timestamp: 1422434194
    2015-01-28 16:36:34
    1422434194

另外， unix timestamp -> python 还有 datetime.utcfromtimestamp() date.fromtimestamp() 函数可用

参考
----

-  http://ruslanspivak.com/2011/07/20/how-to-convert-python-utc-datetime-object-to-unix-timestamp/
-  http://timanovsky.wordpress.com/2009/04/09/get-unix-timestamp-in-java-python-erlang/

Update
------

-  20141215 增加 time2timestamp()
-  20150128 增加 datetime -> utc timestamp
