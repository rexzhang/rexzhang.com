Windows7下将IDE硬盘接口模式切换到ACHI
####################################################


:author: Rex Zhang
:date: 2009-10-18T21:47:30+08:00
:modified: 2009-10-18T21:47:30+08:00
:status: published
:category: 数字生存
:tags: Win7, ACHI

IDE是早期的硬盘接口标准，现在大容量储存设备基本都已改为SATA接口。SATA的主板和硬盘配合，如果使用IDE接口模式将不能发挥SATA的最大效能，特别是在热插拔和磁盘内部存取速度方面。

而为了保证兼容，大部分的主板BIOS默认设置都是使用的IDE模式。这导致一不小心就会将系统安装为IDE模式，而直接修改BIOS为ACHI模式后再启动Windows7会导致启动失败。其主要原因在于没有ACHI的驱动无法让系统正确的读取磁盘；而IDE模式下不会安装ACHI驱动。这是一个变相的鸡生蛋的问题。

而正好我的主板支持将2个集成的SATA控制器分别设置为两种不同的工作模式，最终得以解决。

解决方法如下：

-  系统硬件环境：技嘉GA-MA78GM-S2H（AMD芯片组SB700的南桥，其中SATA0～3端口为一组，SATA4/5为一组），支持SATAII的希捷硬盘做的Windows7的系统盘
-  初始状态为：SATA0～5端口在BIOS中均设置为IDE模式，在此模式下安装的系统。
-  首先关闭电源；将系统盘插到SATA4端口。然后启动系统，并保证系统能正常启动
-  重启电脑进入BIOS。将 Integrated Peripherals 下的 OnChip SATA Type
   设置为 ACHI 。将 OnChip SATA Prot4/5 Type 设置为 IDE
   。保存后重启进入Windows7
-  Windows7会将SATA0～4识别为通用的SATA控制器。建议运行主板的驱动安装包更新驱动。更新后会被识别为
   AMD SATA 控制器
-  关机；将系统硬盘插到SATA0端口；再开机。开机进入Windows7后会识别到新的硬盘（其实就是之前的硬盘，只不过会识别为SATA模式）。这个时候就已经切换成功了。
-  当然如果希望所有的SATA端口都能工作在ACHI模式。只需要重启；进入BIOS将
   Integrated Peripherals下的 OnChip SATA Prot4/5 Type 设置为 as SATA
   Type
   即可。这个时候SATA4/5也支持热插拔了。其意义在于：大部分的主板的SATA5端口都被做成eSATA提供在主板后端；实际使用中方面了很多

一个小小的副作用：如此操作后会导致Windows7恢复到未激活状态，需要重新激活
