title: 在 python 类范围内使用装饰符
author: Rex Zhang
date: 2014-11-17T02:28:27+08:00
modified: 2014-11-17T02:28:27+08:00
status: published
category: Coding
tags: Python

装饰符函数的传入变量为：使用装饰符的函数（目标函数）。其本质是：在调用目标函数之前，插入调用装饰符函数，然后由装饰符函数调用目标函数。

使用的优势：

- 剥离高度重复，同时又需要共享变量（一般是局部变量，如果扩展变量作用域会引发更多麻烦）的代码
- 便于函数扩展行为切换
- 将一些通用行为（代码片段）做成装饰符方便使用和在需求发生变化时随时移除

网上装饰符的文章很多，但是在类范围内使用的很少；所以范例代码如下：

```python
class dater(object):
    """"""
    def __init__(self, year=None, month=None, day=None):
        """Constructor"""
        if year == None and month == None and day == None:
            self.SetToday()
        return

    def get_self_date(func):
        """@"""
        def __call__(self, year=None, month=None, day=None):
            if year == None and month == None and day == None: #使用此装饰符的函数不用重复写相同代码来做输入参数判断和赋值
                year = self.year
                month = self.month
                day = self.day

            return func(self, year, month, day) #执行完装饰符函数后执行目标函数
        return __call__

    def set_date(func):
        """@"""
        def __call__(self):
            func(self) #先执行使用装饰符的函数内容，然后再执行装饰符函数内代码
            self.year = self.date.year
            self.month = self.date.month
            self.day = self.date.day
            self.week = self.date.isocalendar()[1]

            return
        return __call__

    def SetToday(self):
        """"""
        day = datetime.datetime.today()

        self.year = day.year
        self.month = day.month
        self.day = day.day
        return

    @set_date
    def SetYesterday(self):
        """"""
        self.date = datetime.datetime.today()
        self.date += datetime.timedelta(days=-1)
        return

    def SetDay(self, year, month, day):
        """"""
        self.year = year
        self.month = month
        self.day = day
        return

    def SetYday(self, year, yday):
        """"""
        day = datetime.datetime(year, 1, 1)
        day += datetime.timedelta(days=yday-1)

        self.year = day.year
        self.month = day.month
        self.day = day.day
        return

    @set_date
    def SetLastWeek(self):
        """"""
        self.date = datetime.datetime.today()
        self.date += datetime.timedelta(weeks=-1)
        return

    @set_date
    def SetLastMonth(self):
        """"""
        date = datetime.datetime.today()
        year = date.year

        month = date.month
        if month == 1:
            year -= 1
            month = 1
        else:
            month -= 1

        day = 1

        self.date = datetime.datetime(year, month, day)
        return

    @get_self_date
    def GetDetail(self, year, month, day):
        """"""
        dt = datetime.datetime(year, month, day)
        tt = dt.timetuple()

        date = {
            'year': tt[0],
            'yday': tt[7],
            'month': tt[1],
            'mday': tt[2],
            'week': dt.isocalendar()[1],
            'wday': dt.isocalendar()[2],
        }
        return date
```
