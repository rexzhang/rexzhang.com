debian 开启 SNMPv3 支持
######################################


:author: Rex Zhang
:date: 2011-04-21T05:40:31+08:00
:modified: 2011-04-21T05:40:31+08:00
:status: published
:category: Linux
:tags: SNMP


首先确定已经安装 snmpd

然后停掉 snmpd 服务

.. code-block:: shell

    /etc/init.d/snmpd stop

创建 SNMPv3 内的访问帐号

.. code-block:: shell

    net-snmp-config --create-snmpv3-user -ro -a MD5 -x DES snmpv3readonly

或者

.. code-block:: shell

    net-snmp-config --create-snmpv3-user -ro -A authpass -X privpass -a MD5 -x DES snmpv3readonly

其中 snmpv3readonly 为帐号的用户名

修改 /etc/snmp/snmpd.conf

.. code-block:: text

    agentAddress udp:xxx.xxx.xxx.xxx:161 #添加 snmpd 监听的网络端口

或者

.. code-block:: text

    agentAddress udp:161,udp6:[::1]:161 #监听所有端口

根据需要打开需要监控的系统信息

重启 snmpd 服务

.. code-block:: shell

    /etc/init.d/snmpd restart
