Debian v3.1r0 下架设DHCP服务
##############################

:author: Rex Zhang
:date: 2005-11-23T16:56:57+08:00
:modified: 2005-11-23T16:56:57+08:00
:status: published
:category: Linux
:tags: Debian

Debian中的DHCP服务器软件是ISC的dhcpd。有V2和V3两个版本可选。之前一直装的是V2，这次试试V3。发现V3的Webmin安装包做的不好，需要自己修改一些模块参数。

1。先安装服务和Webmin模块

.. code-block:: shell

    LS2:~# aptitude install dhcp3-server webmin-dhcpd

..

    \*注意webmin-dhcpd3这个包有问题（其实这个包是个虚拟包实际指向的webmin-dhcpd）。安装后在Webmin界面找不打DHCP模块。安装结束时，就被提示dhcpd3的很多文件搬移了位置。

2。进入Webmin界面，在Server部分点击"DHCP服务器"模块图标Webmin会报模块配置错误。因为，webmin-dhcpd是对应dhcpd（V2）这个版本的。

3。这时候需要点击屏幕左上的模块配置;，进入模块配置修改界面

其中：

   "DHCP服务器配置文件"修改为：/etc/dhcp3/dhcpd.conf

   "DHCP服务器执行文件"修改为：/usr/sbin/dhcpd3

   "Command to start DHCP server"修改为：/etc/init.d/dhcp3-server start

   "Command to apply configuration"修改为：/etc/init.d/dhcp3-server
   restart

   "DHCP服务器租赁文件"修改为：/var/lib/dhcp3/dhcpd.leases

   |debian-webmin-dhcpd3-with-dhcpd3-server.png|

4。点保存即可。

配置方法同V2版。

.. |debian-webmin-dhcpd3-with-dhcpd3-server.png| image:: /files/113273620235_tn.jpg
   :target: /files/113273620235.png
