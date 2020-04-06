Debian v3.1r0 下架设Apache2 + PHP4 + MySQL + mmCache + Zend环境
##################################################################

:author: Rex Zhang
:date: 2005-07-26T00:05:57+08:00
:modified: 2005-07-26T00:05:57+08:00
:status: published
:category: Linux
:tags: Debian

1.安装Apache2以及MySQL,PHP4以Apache2的模块的方式运行

.. code-block::

   aptitude install apache2-common apache2-mpm-prefork
   libapache2-mod-php4 mysql-server php4-mysql php4-gd phpmyadmin

其中phpadmin是一个基于web界面的MySQL管理工具.另外,在这一版的Debian中,安装PHP等跟Apache相关的程序时都会询问与那个版本的Apache关联(以方便安装程序进行自动配置),只需要选Apache2即可.

2. 修改 /etc/php4/apache2/php.ini 使PHP可以存取MySQL数据库

把
   
    #extension=mysql.so

改成
   
    extension=mysql.so

3. 设置MySQL root帐号初始秘密码

可先用命令检查是否有密码

    LS1:~# mysqladmin version

在没有设置密码时,会显示版本信息.一旦设置了root帐号密码,就会提示存取限制错误

    LS1:~# mysqladmin password YourPassword

4.安装PHP网页缓存引擎(Cache Engine)mmCache
因为mmCache现在还处于unstable阶段,所以不使用变通手段是无法直接获取的.当然如果你用的源是unstable或者是test.那就另当别论了.

获取mmCache安装包.

    LS1:~# cd /tmp

    LS1:~# wget http://debian.cn99.com/debian/pool/main/t/turck-mmcache/turck-mmcache_2.4.6-12_i386.deb

因为版本更新的缘故,具体的文件名需要在 http://debian.cn99.com/debian/pool/main/t/turck-mmcache 确认一下.主要是版本号可能有变化.

安装mmCache包

    LS1:~# dpkg -i turck-mmcache_2.4.6-12_i386.deb

因为mmCache的默认安装是Apache,Apache2需要手动添加配置信息(可能就是这个缘故没有进stable).配置的方法可参考 http://turck-mmcache.sourceforge.net/index_old.html

    LS1:~# nano /etc/php4/apache2/php.ini

添加如下信息

.. code-block::

    ####mmCache###########################
    extension="mmcache.so"
    mmcache.shm_size="16"
    mmcache.cache_dir="/tmp/mmcache"
    mmcache.enable="1"
    mmcache.optimizer="1"
    mmcache.check_mtime="1"
    mmcache.debug="0"
    mmcache.filter=""
    mmcache.shm_max="0"

创建mmCache的保存缓存文件的目录

.. code-block::

    LS1:~# mkdir /tmp/mmcache
    LS1:~# chmod 0777 /tmp/mmcache

5.安装Zend Optimizer

因为Molyx使用Zend Optimizer对其PHP源代码进行了加密.所以必须安装Zend Optimizer才能够工作.如果没有这个要求.个人觉得没有必要再安装Zend Optimizer.因为其包含的缓存加速功能mmCache已经提供了.

下载

.. code-block::

    LS1:~# cd /tmp
    LS1:~# wget http://downloads.zend.com/optimizer/2.5.7/ZendOptimizer-2.5.7-linux-glibc21-i386.tar.gz

安装

.. code-block::

    LS1:~# tar -zxvf  ZendOptimizer-2.5.7-linux-glibc21-i386.tar.gz
    LS1:~# cd ZendOptimizer-2.5.7-linux-glibc21-i386
    LS1:~# sh install.sh

同样可到Zend的下载页面 http://downloads.zend.com/optimizer/ 查找最新版安装包文件名

安装完毕后,会提示 `php.ini` 配置文件移动到了/usr/local/Zend/etc

6.重启Apache

   LS1:~# /etc/init.d/apache2 restart

7.检验php配置

首先创建一个测试文件

    LS1:~# nano /var/www/test.php

内容如下

.. code-block::

    <?php phpinfo()?>

按Ctrl+X,y,回车.保存并退出

使用浏览器访问 `http://yourDebianIPAddress/test.php <http://yourdebianipaddress/test.php>`__

如一切正常的话,就会有相应的PHP环境显示.
