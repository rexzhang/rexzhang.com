一句话修改windows下网卡的设置
####################################


:author: Rex Zhang
:date: 2011-02-20T07:31:14+08:00
:modified: 2011-02-20T07:31:14+08:00
:status: published
:category: 数字生存
:tags: windows, 网卡


.. code-block:: shell

    netsh interface ip set address name="本地连接" source=static addr=192.168.100.100 mask=255.255.255.0 gateway=192.168.100.1 gwmetric=auto

.. code-block:: shell

   netsh interface ip set address name="本地连接" source=dhcp


参考：

- http://www.blogjava.net/qujinlong123/archive/2007/06/20/125434.html\ （这里还有python调用WMI的实现）
