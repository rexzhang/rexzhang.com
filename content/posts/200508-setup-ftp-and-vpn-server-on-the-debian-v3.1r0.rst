Debian v3.1r0 下架设FTP以及VPN服务
###################################

:author: Rex Zhang
:date: 2005-08-04T00:40:26+08:00
:modified: 2005-08-04T00:40:26+08:00
:status: published
:category: Linux
:tags: Debian


FTP Server
----------

其中FTP服务选用的是wu-ftpd,老牌的FTP服务器软件.

1.安装wu-ftpd

.. code-block:: shell

   LS1:~# aptitude install wu-ftpd

同时也可安装webmin-wuftpd,不过在这里,这个FTP只是为了配合维护Web系统的,不会做太多的配置.就省了.

2.做一些权限设置(网上抄的我也不是完全理解...汗)

.. code-block:: shell

    LS1:~# chmod 555 /home/ftp
    LS1:~# chmod 111 /home/ftp/bin/\*
    LS1:~# chmod 555 /home/ftp/lib/\*
    LS1:~# chmod 444 /home/ftp/etc/\*

3.配置

配置文件直接套用了/usr/share/doc/wu-ftpd/examples/下的ftpaccess.heavy

.. code-block:: shell

   LS1:~# cp /usr/share/doc/wu-ftpd/examples/ftpaccess.heavy /etc/wu-ftpd/ftpaccess

后稍作修改

.. code-block:: shell

   LS1:~# nano ftpaccess

添加如下信息

.. code-block:: text

   guest-root ~
   restricted-uid ftpusername

其中ftpusername是系统中已经存在的普通帐号.目的是:限定ftpusername用户在其自己的根目录下,即目录/home/ftpusername下.
如果需要的用户名没有可以用adduser命令添加普通帐号

4.重启wu-ftpd

.. code-block:: shell

   LS1:~# /etc/init.d/wu-ftpd restart

5.最后使用FTP客户段软件尝试登陆检查服务是否工作

VPN Server
----------

VPN选用的PPTP包

使用VPN是基于安全上的考虑.因为这个服务器是放在内网(网络拓扑为:Internet --- NAT --- LS1),通过一个NAT与外界通信,而对外只有一个必要的服务,即HTTP(端口80),所以只需在NAT上做一个端口映射到服务器即可.但考虑到维护需要FTP,Telnet(SSH),甚至是MySQL;如果将这些端口都暴露出来,维护和监控的工作量将会大大的增加.现在想到的一个办法就是;用VPN建立一个隧道,并在隧道中跑这些应用.这样服务器暴露在外的就只有HTTP(80)和PPTP(1723)这两个端口,尽可能的减少了风险.

1.安装PPTP服务

.. code-block:: shell

    LS1:~# apt-get install pptpd
    LS1:~# apt-get install webmin-pptp-server //可选

2.配置PPTP

.. code-block:: shell

   ~# nano /etc/pptpd.conf

一般使用默认即可,需要修改的就是分配IP地址部分

.. code-block:: text

    #本地(PPTP隧道服务器端)的IP地址.
    localip 192.168.100.50
    #远端(PPTP隧道客户端)的IP地址段,PPTP服务会分配这些IP地址给连接上来的客户.这里需要补充说明的是:如果只这样配置PPTP客户端就只能访问PPTP服务端,而无法进入与PPTP服务器相连的本地网络.如果有这个需求,就需要考虑IP地址的划分问题,并在Linux内做相应的路由配置.
    remoteip 192.168.100.51-60

3.配置PPTP服务参数

.. code-block:: shell

    LS1:~# nano /etc/ppp/pptpd-options

.. code-block:: text

    # Name of the local system for authentication purposes
    # (must match the second field in /etc/ppp/chap-secrets entries)
    #name pptpd
    name LS1
    #修改你PPTP服务名,名字是随便取的,关键是要和用户认证信息中的服务器名一致

    # Optional: domain name to use for authentication
    # domain mydomain.net
    domain YouDomain.COM #这台Linux机器的域名,没看到有什么用

    # Encryption
    # Debian: on systems with a kernel built with the package
    # kernel-patch-mppe >= 2.4.2 and using ppp >= 2.4.2, ...
    #如要使用MS的加密认证,就需要服务器端支持mppe,默认的内核是不支持的,内核补丁的安装现在好没搞定;PAP方式太不安全,所以把系统配置为只使用不加密的CHAP认识模式
    # {{{
    refuse-pap
    #refuse-chap
    refuse-mschap
    # Require the peer to authenticate itself using MS-CHAPv2
    [Microsoft
    # Challenge Handshake Authentication Protocol, Version 2]
    authentication.
    #require-mschap-v2
    # Require MPPE 128-bit encryption
    # (note that MPPE requires the use of MSCHAP-V2 during
    authentication)
    #require-mppe-128
    # }}}

4.添加PPTP客户帐号

.. code-block:: shell

    LS1:~# nano /etc/ppp/chap-secrets

.. code-block:: text

    # Secrets for authentication using CHAP
    # client server secret IP addresses
    pptpUser LS1 pptpPassword "*"
    #这里的*表示不对PPTP客户端IP地址做限制

5.重启pptpd服务

.. code-block:: shell

   LS1:~# /etc/init.d/pptpd restart

6.配置客户端

以Win2K为例,新建一个网络连接,选VPN.创建后需要修改的是:

网络部分,VPN服务器类型选"PPTP".安全措施部分,数据加密选"不允许加密",而允许的协议只选CHAP\ |PPTPWin2K客户端配置|

.. |PPTP Win2K客户端配置| image:: /files/cap2.jpg
