检查硬件兼容性
##############


:author: Rex Zhang
:date: 2004-12-22T23:44:22+08:00
:modified: 2004-12-22T23:44:22+08:00
:status: published
:category: Linux


检查硬件兼容性其实很简单在\ `TLDP(The Linux Documentation Project) <http://www.tldp.org/>`__\ 下有一个\ `Linux Hardware Compatibility HOWTO <http://www.tldp.org/HOWTO/Hardware-HOWTO/>`__.绝大部分的硬件只要简单的用搜索功能查找一下即可.如果使用CUPS基本上不用担心打印机的支持问题.就是内置Modem比较麻烦.

以我的硬件为例:

1.主板

用的是很早以前的SiS的主板,Intel的CPU,IDE的硬盘应该没什么问题

2.显卡

虽然我不上X系统,但还是顺便查查.集成显卡SiS 530/620在\ `Video cards <http://www.tldp.org/HOWTO/Hardware-HOWTO/video.html>`__\ 里面的清单内找到部分没有问题.

3.网卡

D-Link DFE-500TX Rev B/C这是个非常常见的东东,自然在\ `Network
apapters-Supported <http://www.tldp.org/HOWTO/Hardware-HOWTO/nic.html>`__\ 中也有

4.Modem

看来以前买Inter 536EP V.92实在是明智啊,哈哈便宜又有免费的Linux驱动(`Intel官方的 <http://developer.intel.com/design/modems/support/drivers.htm>`__,\ `第三方的 <http://linmodems.technion.ac.il/packages/Intel/ham/>`__),当然如果有用串口(RS-232)的外猫那就更爽了.

推荐一个查找Modem Linux驱动的\ `好地方 <http://dmoz.org/Computers/Software/Operating_Systems/Linux/Hardware_Support/Modems/>`__,还有\ `LinuxSir上的一个专题 <http://www.linuxsir.org/bbs/showthread.php?t=3007>`__

5.打印机

HP6L,HP4L都是大路货,在CUPS上都有支持.

6.声卡

暂时不去找他.反正从来就没用过,呵呵 ;-)
