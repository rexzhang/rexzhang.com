Debian下开启snmpd
############################


:author: Rex Zhang
:date: 2009-08-31T22:22:16+08:00
:modified: 2009-08-31T22:22:16+08:00
:status: published
:category: Linux
:tags: Debian, SNMP


安装

.. code-block:: shell

    # aptitude install snmpd snmp

修改 ``/etc/default/snmpd``。让snmpd监听所有的网卡（默认只监听回环地址127.0.0.1，这种状况下只能本机访问snmp信息）

.. code-block:: text

    # snmpd options (use syslog, close stdin/out/err).
    #SNMPDOPTS='-Lsd -Lf /dev/null -u snmp -I -smux -p /var/run/snmpd.pid 127.0.0.1'
    SNMPDOPTS='-Lsd -Lf /dev/null -u snmp -I -smux -p /var/run/snmpd.pid'

修改 ``/etc/snmp/snmpd.conf``。配置snmpd服务。建议参考 http://www.debianhelp.co.uk/snmp.htm

.. code-block:: text

    ####
    # First, map the community name (COMMUNITY) into a security name
    # (local and mynetwork, depending on where the request is coming
    # from):
    #       sec.name  source          community
    #com2sec paranoid  default         public
    #com2sec readonly  default         public
    com2sec local      localhost       public
    com2sec localnet   192.168.100.0/24 public
    #com2sec readwrite default         private
    ####
    # Second, map the security names into group names:
    #               sec.model  sec.name
    #group MyROSystem v1        paranoid
    #group MyROSystem v2c       paranoid
    #group MyROSystem usm       paranoid
    #group MyROGroup v1         readonly
    #group MyROGroup v2c        readonly
    #group MyROGroup usm        readonly
    group MyRWGroup v1         readwrite
    group MyRWGroup v2c        readwrite
    group MyRWGroup usm        readwrite
    group MyROSystem v1        local
    group MyROSystem v2c       local
    group MyROSystem usm       local
    group MyROGroup v1         localnet
    group MyROGroup v2c        localnet
    group MyROGroup usm        localnet

基于安全的角度建议，MyRWGroup保留原状，即不开放写权限

.. code-block:: text

    #  Make sure mountd is running
    proc mountd

打开磁盘使用情况监控

.. code-block:: text

    ###############################################################################
    # disk checks
    #
    # The agent can check the amount of available disk space, and make
    # sure it is above a set limit.
    # disk PATH [MIN=DEFDISKMINIMUMSPACE]
    #
    # PATH:  mount path to the disk in question.
    # MIN:   Disks with space below this value will have the Mib's errorFlag set.
    #        Default value = DEFDISKMINIMUMSPACE.
    # Check the / partition and make sure it contains at least 10 megs.
    disk / 10000
    disk /home 10000
    disk /var 10000

打开CPU负载均衡监控

.. code-block:: text

    ###############################################################################
    # load average checks
    #
    # load [1MAX=DEFMAXLOADAVE] [5MAX=DEFMAXLOADAVE] [15MAX=DEFMAXLOADAVE]
    #
    # 1MAX:   If the 1 minute load average is above this limit at query
    #         time, the errorFlag will be set.
    # 5MAX:   Similar, but for 5 min average.
    # 15MAX:  Similar, but for 15 min average.
    # Check for loads:
    load 12 14 14

重启snmpd服务

.. code-block:: shell

    # /etc/init.d/snmpd restart

本机检查

.. code-block:: shell

    # snmpwalk localhost -c public -v1

远端检查

.. code-block:: shell

    # snmpwalk 192.168.100.15 -c public -v1
