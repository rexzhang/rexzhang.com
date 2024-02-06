启动文件服务器替代计划
######################

:author: Rex Zhang
:date: 2004-12-22T00:20:17+08:00
:modified: 2004-12-22T00:20:17+08:00
:status: published
:category: Linux

这个计划酝酿很久了.现在终于抽出时间来实施.至于理由...很多...就不说了,进入正题.

现有系统/应用
-------------
- Win2KServer
- 基于用户级别的文件共享
- 基于用户级别的文件打印
- 自动接收传真,并自动打印
- IP地址分发维护

系统规划
--------
- `Debian <http://www.debian.org/>`__\ (woody)

应用规划
--------
- 基于用户级别的文件共享(`Samba <http://www.samba.org/>`__ / `Samba.Chinese <http://hk.samba.org/>`__)
- 基于用户级别的文件打印(Samba+ `Common UNIX Printing
  System <http://www.cups.org/>`__)
- 自动传真,并自动打印(`HylaFAX <http://www.hylafax.org/>`__)
- IP地址分发维护
- \ `Apache Web
  Server <http://httpd.apache.org/>`__,支持\ `PHP <http://www.php.net/>`__,Perl,\ `MySQL <http://www.mysql.com/>`__
- FTP

维护规划
--------
- 基于SSH的Telnet
- 基于HTTPs的web管理界面(`WebMin <http://www.webmin.com/>`__)
- 不安装X Window

安全规划
--------
- 安装防火墙(IPtable)
- 安装杀毒软件

进程规划
--------
- 确立目标,制定规划
- 确认将使用软件
- 确认硬件兼容性(主板,显卡,Modem,打印机)
- 安装基系统(SSH+WebMin)
- 升级基本系统至最新版本
- 实现文件共享,打印共享,传真接收功能
- 根据实际情况调整其他应用的安装以及安全部分的实现
- 收尾工作
