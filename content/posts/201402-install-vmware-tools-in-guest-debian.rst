在 Debian 虚拟机中安装 VMware Tools
########################################################


:author: Rex Zhang
:date: 2014-02-07T22:34:18+08:00
:modified: 2014-02-07T22:34:18+08:00
:status: published
:category: 运维
:tags: Debian, VMware


VMware 虚拟机在没有安装 VMware Tools 之前是不支持在 vSphere Client 自动关闭操作系统（只能关闭虚拟机电源）、查看网卡 IP 地址等信息。安装步骤如下：

在 VMware 官网搜索 VMware Tools CD image for Linux Guest Oses 下载光盘 ISO 文件。可能需要注册一个帐号（免费的）

1.启动 Debian 虚拟机，在 vSphere Client 中设置挂载光盘镜像文件

2.Debian 中挂载光盘

.. code-block:: shell

    mount /dev/cdrom /mnt

3.将光盘中的 VMwareTools-xxxxxxxxxx.tar.gz 解出到 /root/vmware-tools

4.安装 VMware Tools 需要安装 gcc make 以及 Linux 当前版本内核的头文件

.. code-block:: shell

    aptitude install gcc make
    aptitude install linux-headers-$(uname -r)

5.执行安装脚本

.. code-block:: shell

    cd /root/vmware-tools
    ./vmware-install.pl

执行安装脚本的时候一路选择默认即可

参考链接

-  http://www.thomas-krenn.com/de/wiki/VMware_Tools_in_Debian_installieren
-  http://www.cyberciti.biz/faq/howto-install-kernel-headers-package/
-  http://blog.mwpreston.net/2011/10/12/installing-vmware-tools-on-debian-6-squeeze/
