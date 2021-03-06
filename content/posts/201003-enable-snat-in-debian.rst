debian开启SNAT网关
############################


:author: Rex Zhang
:date: 2010-03-25T07:20:22+08:00
:modified: 2010-03-25T07:20:22+08:00
:status: published
:category: Linux
:tags: Debian, SNAT


linux都在内核集成了iptables，可以用其实现NAT转换

开启NAT网关需要设置两个部分

- 在内核开启ip转发
- 使用iptables开始snat转换

内核中开启ip转发也有几种方式

1.执行

.. code-block:: shell

    sysctl -w net.ipv4.ip_forward=1

2.或者执行

.. code-block:: shell

    echo 1 > /proc/sys/net/ipv4/ip_forward

3.或者修改 /etc/sysctl.conf 添加

.. code-block:: text

    # Enable packet forwarding
    net.ipv4.ip_forward = 1

然后执行

.. code-block:: shell

    /etc/init.d/networking restart

在iptables中添加snat转换

执行

.. code-block:: shell

    iptables -t nat -A POSTROUTING -o eth0 -j SNAT --to-source your.public.ip.adderss

其中
- eth0 为连接公网的网络端口
- your.public.ip.adderss 为你的公网ip地址

完成后可以执行

.. code-block:: shell

    iptables -L -t nat

可以查看到新的设置

另外一个开启snat的方法

.. code-block:: shell

    Now you need to activate NAT itself in /etc/network/interfaces
    auto eth0
    iface eth0 inet static
    address 192.168.1.254
    netmask 255.255.255.0
    network 192.168.1.255
    up iptables -t nat -A POSTROUTING -o $IFACE -j SNAT

    Now you need to restart your networking services using the following command

    #/etc/init.d/networking restart

参考链接

- http://lorenzod8n.wordpress.com/2008/03/16/very-simple-nat-set-up-on-debian/

update

- 20110725:修正iptables命令的一处参数错误
