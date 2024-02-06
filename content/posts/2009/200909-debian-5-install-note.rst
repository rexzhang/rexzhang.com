Debian 5 新系统安装笔记
################################


:author: Rex Zhang
:date: 2009-09-01T01:18:51+08:00
:modified: 2009-09-01T01:18:51+08:00
:status: published
:category: Linux
:tags: Debian


硬件环境
--------

AMD785G,AMDx3 720,2x2G DDR3-1333,Realtek的千兆网卡

在官方网站上下载镜像 debian-502a-amd64-DVD-1.iso。光盘启动后：Installer启动前提示BIOS未开启 IOMMU，查询后发现是主板不支持（未提供相关的BIOS选项），作罢

网络设置默认是DHCP自动获取了一个IP地址，可以在获取后使用（BACK）手工修改为自己需要的

在选择安装包时，取消掉所有的包，包括 standard。这样安装出来是最精简的基系统

安装常用工具
------------

.. code-block:: shell

    # aptitude install sudo ssh mc

配置sudo
---------

用root帐号登录，执行 ``# visudo`` 。进入一个像nano一样的文本编辑器修改权限。然后重新用一个允许执行sudo的普通帐号登录，再执行 ``# sudo -s`` 即可

配置apt源
---------

先下载 ``http://mirrors.163.com/sources.list.lenny``, 添加内容到 /etc/apt/sources.list 。其内容如下

.. code-block:: text

    deb http://mirrors.163.com/debian lenny main non-free contrib
    deb http://mirrors.163.com/debian lenny-proposed-updates main contrib non-free
    deb http://mirrors.163.com/debian-security lenny/updates main contrib non-free
    deb-src http://mirrors.163.com/debian lenny main non-free contrib
    deb-src http://mirrors.163.com/debian lenny-proposed-updates main contrib non-free
    deb-src http://mirrors.163.com/debian-security lenny/updates main contrib non-free

然后屏蔽掉默认的internet源信息，和cd-rom源信息（在拆走光驱时）

更新源信息，并升级系统到最新

.. code-block:: shell

    # aptitude update
    # aptitude upgrade

会更新内核镜像，所以完了后

.. code-block:: shell

    # reboot

安装python
-----------

.. code-block:: shell

    # aptitude install python

实际安装的是2.5

安装apache2，mysql和phpmyadmin
-------------------------------

.. code-block:: shell

    # aptitude install apache2 apache2-mpm-prefork mysql-server php5 phpmyadmin

其中：apache2-mpm-prefork表示是多进程版本，使用多进程的方式管理内存。据官方说会比较消耗内存。如果需要使用多线程可以安装worker版。完成后访问 http://192.168.100.15 显示 It works! 。表示apache2正常

配置phpmyadmin
--------------

访问 http://192.168.100.15/phpmyadmin ，检查ok

安装postgreSQL
--------------

.. code-block:: shell

    aptitude install postgresql python-psycopg2 phppgadmin

添加postgreSQL用户
------------------

先在 ``sudo`` 到 ``postgres`` 用户默认是没有密码的

.. code-block:: shell

    root@CD-LS5:~# su - "postgres"

创建一个pg管理用户

.. code-block:: shell

    postgres@CD-LS5:~$ createuser -s yourPgUser
    createuser: creation of new role failed: ERROR:  role "yourPgUser"  already exists #如果提示已经存在
    postgres@CD-LS5:~$ dropuser yourPgUser #删除现有的
    postgres@CD-LS5:~$ createuser -P -s -e yourPgUser
    Enter password for new role:
    Enter it again:
    CREATE ROLE yourPgUser PASSWORD 'md5xxxxxxxxxxxxxxxxx' SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN; #是超级用户，可以创建数据库和访问规则

然后修改 phppgadmin的配置文件 ``/etc/phppgadmin/config.inc.php``, 关闭对登录安全的限制（允许空密码帐号存在）

.. code-block:: text

    修改 $conf['extra_login_security'] = true;
    变为 $conf['extra_login_security'] = false;

就可以用yourPgUser在web上登录了。还有apache2的主机设置也要添加可访问ip域规则

update 20110326:phppgadmin 关闭对登录安全的限制不是必须的
