修改 debian locales 设置
########################################


:author: Rex Zhang
:date: 2011-02-13T04:42:40+08:00
:modified: 2011-02-13T04:42:40+08:00
:status: published
:category: Linux
:tags: Debian, 本地化


很多时候 debian 的默认安装使用的语言为 ANSI（POSIX）。这种情况下在终端里面中文是乱码，文本全屏软件不能显示制表符，非常难看。解决办法如下


1.安装 locales 包

.. code-block:: shell

    aptitude install locales

2.默认状态下，安装程序并不会改变语言设置，所以需要手动执行这个操作

.. code-block:: shell

    dpkg-reconfigure locales

建议选择 en_US.UTF-8 ，当然 zh_CN.UTF-8 也是可以的，不过部分命令行软件对中文支持不是很完美，不推荐

3.改变操作是及时生效的，不过因为当前帐号已经登录。要看到效果需要 logout ，然后再 login 即可
