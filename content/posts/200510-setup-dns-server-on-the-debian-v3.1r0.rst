Debian v3.1r0 下架设DNS服务，并在本地DNS服务器上替换解析部分域名
################################################################

:author: Rex Zhang
:date: 2005-10-19T23:40:14+08:00
:modified: 2005-10-19T23:40:14+08:00
:status: published
:category: Linux
:tags: Debian

先在网上搜索了一下BIND8和BIND9的区别，感觉不大，完全可以先用着相对较旧的版本，毕竟旧版本意味着接受考验的时间更长；而且，资料也相对多些。因此，DNS服务器软件选用的是BIND8，没有使用BIND9。

1.安装BIND8

.. code-block:: shell

   LS1:~# aptitude install bind

如果只是把BIND作为本地的一个DNS代理服务器,用于减少对外部DNS访问流量的话.安装好后不用设置即可工作.

2.安装Web-min的bind8支持模块(因为是我第一次用BIND,有个图形界面的比较容易上手,呵呵)

.. code-block:: shell

   LS1:~# aptitude install webmin-bind

3.使用BIND替换解析部分域名

要实现的目的其实很简单,只是说起来要费些口舌.起因是这样的:

我的网络环境如下:

    Internet<->NAT<->LAN<->WebServer

其他PC也接在LAN上,并透过NAT访问Internet.并且在NAT处使用PortMapping(端口映射)的方式把对外的80端口指向到WebServer.以实现的WEB服务.www.flord.net这个域名在Internet上是解析到NAT上的公网IP(Public IPAddress)的.在内网(LAN)上的PC访问www.flord.net,会被解析到NAT上的公网IP.要想透过渔民访问放在WebServer上www.flord.net域名下的网页.必须用修改本地hosts文件的方式解决.很是繁琐.

因此,最终实际上是要实现:BIND为内网(LAN)上PC提供正常的域名解析的同时,将特定的域名解析到内网的IP地址

    1>首先,进入Web-min的BIND模块

    2>创建一个新的"主区域"选"正向",因为,我们是要解决域名到IP的解析问题

        |image0|

        点新建后,web-min创建完毕,并自动进入"主区域"编辑界面

    3>现在我们新建一个A记录(地址)

    4>在名称处填写需要本地解析的域名(注意,一定要在域名后面添加一个英文的句号).在地址处填写这个域名在内网的IP地址.同时,关掉反向更新.

        |image1|

    4> 返回web-min的"BIND DNS 服务器"页面,点"应用更改"后.以上设置即可生效

4.将内网PC网卡上的的DNS服务器地址修改为安装BIND的机器的IP地址.

现在LAN上的PC访问www.flord.net都将直接解析到WebServer.

.. |image0| image:: /files/debian-bind8-1.png
.. |image1| image:: /files/debian-bind8-2.png
