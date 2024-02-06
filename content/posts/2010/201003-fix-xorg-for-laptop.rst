xorg LCD屏幕分辨率问题
##############################


:author: Rex Zhang
:date: 2010-03-10T23:09:31+08:00
:modified: 2010-03-10T23:09:31+08:00
:status: published
:category: Linux
:tags: xorg

给一个老旧的笔记本电脑换装 ubuntu ，安装完成后发现分辨率始终只能使用 800x600。无法使用更高的分辨率（笔记本的硬件支持更高的分辨率）。驱动程序什么的也没发现什么问题。

Google了下找到原因：应该是系统没识别到我的屏幕。解决办法如下

首先需要创建一个 ``xorg.conf`` 文件。我的系统安装好后没有生成的方法如下：

先用 Ctrl+Alt+F1 切换到控制台

以 root 登录，或者可 sudo 的帐号登录后 执行 sudo -s

执行 ``service gdm stop`` #停掉图形界面，不然生成 xorg.conf 的时候会报警说文件锁问题

执行 ``Xorg -configure`` #生成 /etc/X11/xorg.conf 文件

执行 ``service gdm start`` #重新启动图形界面

启动图形界面成功，不过发现依然不能设置更高的分辨率。检查后发现是：生成的 ``xorg.conf`` 文件里面关于显示设备的的设置问题。修改内容如下：

.. code-block:: text

    Section "Monitor"
        Identifier   "Monitor0"
        VendorName   "LCD"
        ModelName    "LCD"
        HorizSync    30 - 82
        VertRefresh  50 - 75
        Option       "DPMS" "true"
    EndSection

    Section "Screen"
        Identifier "Screen0"
        Device     "Card0"
        Monitor    "Monitor0"
        DefaultDepth    24 #如果不设置，可能会使用16位的色深，界面色彩差异很明显
        SubSection "Display"
            Viewport   0 0
            Depth     16
            Modes "1024x768"
        EndSubSection
        SubSection "Display"
            Viewport   0 0
            Depth     24
            Modes "1024x768"
        EndSubSection
    EndSection

重新停止、启动图形界面即可
