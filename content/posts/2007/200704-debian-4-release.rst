Debian 4.0发布
########################

:author: Rex Zhang
:date: 2007-04-11T22:55:47+08:00
:modified: 2007-04-11T22:55:47+08:00
:status: published
:category: Linux
:tags: Debian

Debian 4.0 终于还是来了。感觉最明显的就是默认http server终于升级到了Apache2；MySQL也升级到了5.0；php默认是升级到4.4。据说新装是5。

升级步骤非常轻松：

#. 确认你的apt源为stable而非sarge
#. 检查、更新包列表：``LS3:~# aptitude update``
#. 开始升级：``LS3:~# aptitude dist-upgrade``
#. 大概有230多个包需要下载
#. 下载后的预设值一般用默认即可
#. 清理老旧的更新包（因为更新量很大，遗留了不少的垃圾）：``LS3:~# aptitude autoclean``

值得注意的是：

#. 最好是在本地控制台升级；因为ssh和iptables均有更新
#. 如果当前使用的是2.4的内核强烈建议先将内核升级至2.6再作整体升级

另外，因为默认升级后php是4.4版。如果要使用php5。就需要强行升级

#. 升级到php5：``LS3:~# aptitude install php5 php5-mysql php5-gd php5-cli``
#. 清理掉php4：``LS3:~# aptitude purge php4 php4-common php4-mysql php4-gd php4-cli``
#. 编辑 ``/etc/php5/apache2/php.ini`` 打开mysql和gd支持；修改内存使用限制由8M->16M

关于升级的其他注意事项可以参考\ `Debian GNU/Linux 4.0 ("etch"), Intel x86 的發行情報 <http://www.debian.org/releases/stable/i386/release-notes/index.zh-tw.html#contents>`__
