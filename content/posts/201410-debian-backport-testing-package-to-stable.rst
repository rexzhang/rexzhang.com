Debian 使用 backports 机制在 stable 发布中安装 testing 发布中软件
#################################################################

:author: Rex Zhang
:date: 2014-10-16T22:22:08+08:00
:modified: 2014-10-16T22:22:08+08:00
:status: published
:category: 运维

当前 Debian V7.6 内置的 mongodb 未 v2.4 版本， v2.6 有一个很不错的 Aggregation Pipeline 特性。如果想使用 Debian 自己的包管理仓库就需要使用 backports 机制使用 testing 中的包 (mongodb v2.6),方法如下

首先在 /etc/apt/sources.list 添加

.. code-block:: text

    deb http://mirrors.163.com/debian wheezy-backports main contrib non-free
    deb-src http://mirrors.163.com/debian wheezy-backports main contrib non-free

然后执行

.. code-block:: shell

    sudo aptitude update

这个时候如果直接使用普通的安装命令依然会安装 v2.4

.. code-block:: text

    #aptitude show mongodb
    Package: mongodb
    State: installed
    Automatically installed: no
    Version: 1:2.4.8-2~bpo70+1

使用如下命令即可

.. code-block:: shell

    aptitude -t wheezy-backports install mongodb

另外， mongodb 官方也有一个办法，就是添加 mongodb
自己的源。\ `具体见这里`_ 参考链接

-  https://www.debian.org/distrib/packages

.. _具体见这里: http://docs.mongodb.org/manual/tutorial/install-mongodb-on-debian/
