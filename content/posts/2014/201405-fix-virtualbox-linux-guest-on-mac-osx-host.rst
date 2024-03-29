virtualbox 4.3.10用Mac OSX做宿主Linux做客户机时无法装载共享文件夹问题的修复
################################################################################

:author: Rex Zhang
:date: 2014-05-15T19:43:52+08:00
:modified: 2014-05-15T19:43:52+08:00
:status: published
:category: Linux

virtualbox 4.3.10 用 Mac OSX 做宿主 Linux 做客户机时无法装载共享文件夹，提示如下

.. code-block:: text

    mount: wrong fs type, bad option, bad superblock on hunterServer,
           missing codepage or helper program, or other error
           (for several filesystems (e.g. nfs, cifs) you might
           need a /sbin/mount.<type> helper program)
           In some cases useful info is found in syslog - try
           dmesg | tail  or so

原因是这个版本的 Extension Pack 在安装遗漏了一个符号链接，修复命令如下

.. code-block:: shell

    sudo ln -s /opt/VBoxGuestAdditions-4.3.10/lib/VBoxGuestAdditions /usr/lib/VBoxGuestAdditions

修复后重启虚拟机即可

另，挂载共享文件夹的命令如下，其中共享文件夹的名字为 shareDir 

.. code-block:: shell

    sudo mount -t vboxsf -o gid=1000,uid=1000 shareDir /mnt/shareDir/

BTW:这个版本已经支持共享名与目标名相同，前提是目标目录在书写时需要加上“/”符号结尾

另2，在客户机中也可以通过 /media/sf_* 访问共享文件夹（前提是：讲共享文件夹设置为自动挂载）,不过权限很麻烦，只能使用 root 帐号访问

Ref
---
- 官方论坛和 Bug 跟踪系统的相关信息
    - https://forums.virtualbox.org/viewtopic.php?f=9&t=25295
    - https://www.virtualbox.org/ticket/12879
- mount 挂载到指定用户的方法
    - http://superuser.com/questions/320415/linux-mount-device-with-specific-user-rights
