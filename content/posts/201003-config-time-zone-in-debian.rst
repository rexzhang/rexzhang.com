debian调整系统时区
########################


:author: Rex Zhang
:date: 2010-03-24T01:50:41+08:00
:modified: 2010-03-24T01:50:41+08:00
:status: published
:category: Linux
:tags: Debian


debian调整系统时区

.. code-block::

    # dpkg-reconfigure tzdata

或者

.. code-block::

    # tzselect

查看当前时间和时区

.. code-block::

    # date

使用 NTP 同步时间

.. code-block::

    # ntpdate pool.ntp.org
