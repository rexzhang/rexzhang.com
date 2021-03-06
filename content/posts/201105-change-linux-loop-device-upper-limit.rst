添加系统允许的最大 loop 设备数量
######################################


:author: Rex Zhang
:date: 2011-05-28T08:05:59+08:00
:modified: 2011-05-28T08:05:59+08:00
:status: published
:category: Linux
:tags: xen


今天在创建和加载 Xen 虚拟机时遇到一个错误

.. code-block:: text

    Error: Device 51714 (vbd) could not be connected. Failed to find an unused loop device

才意识到我的 Xen 客户机的磁盘都是以文件形式存在的。每个客户机需要使用两个磁盘分区(/ 和 swap)；刚好 Linux 下面 loop 的默认最大值（max_loop）为 8 ，每挂载一个磁盘分区文件消耗一个 loop 设备；4个虚拟机刚好用光。

解决方法如下：

修改 /etc/modules 文件

.. code-block:: text

    loop max_loop=64

重启系统即可

一些参考命令：

.. code-block::  shell

    losetup -a #显示所有当前使用中的 loop 设备信息
    ls /dev/loop* #列出所有 loop 设备
    rmmod loop #移除 loop 模块
    modprobe loop #重新加载 loop 模块
    dmesg | grep loop # 应当能见到 loop: loaded (max 64 devices)，没有看到，似乎不是这里

参考：

-  http://blog.rootk.com/archives/984
-  http://blog.csdn.net/kivenlee/archive/2011/05/23/6440626.aspx
-  http://tilt.lib.tsinghua.edu.cn/node/310
-  http://yutok2c.blog136.fc2.com/blog-entry-16.html
