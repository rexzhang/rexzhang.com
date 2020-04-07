debian上安装设置socks5 proxy
##############################################


:author: Rex Zhang
:date: 2010-03-25T06:45:42+08:00
:modified: 2010-03-25T06:45:42+08:00
:status: published
:category: Linux
:tags: Debian, Proxy, socks


debian上有一个很不错的socks5的实现：dante http://www.inet.no/dante/

服务端设置
----------

我的环境如下

-  内网网卡为 tun0 ，ip 地址 192.168.x.x
-  外网网卡为 eth0
-  需要使用代理的客户机 ip 地址段为192.168.0.0/16
-  socks5 的端口为 1080

安装

.. code-block::

    # aptitude install dante-server

编辑配置文件

.. code-block::

    # nano /etc/danted.conf

修改内容如下

.. code-block::

    logoutput: /var/log/danted/danted-server.log #将 log 输出到文件，需要手工建立目录 /var/log/danted

    internal: tun0 port = 1080 #指定提供代理服务的网络端口为 tun0

    # all outgoing connections from the server will use the IP address
    # 195.168.1.1
    external: eth0 #指定访问外网的网络端口为 eth0# methods for socks-rules.
    method: username none #rfc931

    # methods for client-rules.
    clientmethod: none
    # when doing something that can require privilege, it will use the
    # userid:
    user.privileged: proxy

    # when running as usual, it will use the unprivileged userid of:
    user.notprivileged: nobody

    # If you compiled with libwrap support, what userid should it use
    # when executing your libwrap commands?  "libwrap".
    user.libwrap: nobody

    client pass {
    from: 192.168.0.0/16 to: 0.0.0.0/0 #定义允许的客户端ip地址范围
    log: connect disconnect
    }

    #allow bind to ports greater than 1023
    pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0 port gt 1023
    command: bind
    log: connect disconnect
    }

    #allow outgoing connections (tcp and udp)
    pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0
    command: connect udpassociate
    log: connect disconnect
    }

    #allow replies to bind, and incoming udp packets
    pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0
    command: bindreply udpreply
    log: connect error
    }

    #log the rest
    block {
    from: 0.0.0.0/0 to: 0.0.0.0/0
    log: connect error
    }


然后重启服务即可

检查是否已经有 danted 进程

.. code-block::

    # ps -A | grep dante

如果提示没有运行，可以手工将服务放在到后台运行

.. code-block::

    # danted -D #启动服务 #可以用来检查配置文件是否正确

如果已经在后台运行，可以重启服务使新设置生效

.. code-block::

    # /etc/init.d/danted restart

客户端设置
----------

安装 socks 客户端软件

.. code-block::

    # aptitude install dante-client

编辑 socks 客户端配置文件 /etc/dante.conf ；其中 10.10.10.10 为 socks 服务器的 ip 地址

.. code-block::

    logoutput: /var/log/dante.log
    resolveprotocol: udp

    route {
            from: 0.0.0.0/0   to: 0.0.0.0/0   via: 10.10.10.10 port = 1080
            protocol: tcp udp                # server supports tcp and udp.
            proxyprotocol: socks_v4 socks_v5 # server supports socks v4 and v5.
            method: none #username           # we are willing to authenticate via
                                             # method "none", not "username".
    }
    route {
            from: 0.0.0.0/0   to: .   via: 10.10.10.10 port = 1080
            protocol: tcp udp                # server supports tcp and udp.
            proxyprotocol: socks_v4 socks_v5 # server supports socks v4 and v5.
            method: none #username           # we are willing to authenticate via
                                             # method "none", not "username".
    }

命令行下客户端的参数格式

.. code-block::

    socksify program [ arguments ]

以下载 python.org 下的文件为例；不使用代理时的命令为

.. code-block::

    wget http://www.python.org/download/xxxxxx.tgz

使用代理的命令为

.. code-block::

    socksify wget http://www.python.org/download/xxxxxx.tgz

UPDATE：
---------

-  20110316:添加log定义；第一次启动的命令
-  20110728:添加客户端安装和使用
