title: 调整VirtualBox的VDI硬盘文件大小
author: Rex Zhang
date: 2011-10-08T23:47:31+08:00
modified: 2011-10-08T23:47:31+08:00
status: published
category: 数字生存
tags: 虚拟机

VirtualBox没有提供很方便的（GUI）调整VDI格式硬盘文件的手段；但是混合使用图形界面和命令行还是可以解决这个问题。

办法如下：

- 第一步：将需要调整的虚拟硬盘复制一个新的copy用来做调整以避免失误导致数据损失** [![resize-virtualbox-vdi-file-copy-vdi](http://farm7.static.flickr.com/6106/6222484668_b7756c55e9.jpg)](http://www.flickr.com/photos/rexzhang/6222484668/ "Flickr 上 Rex Zhang 的 resize-virtualbox-vdi-file-copy-vdi")
- 第二步：在命令行中对新生成的虚拟磁盘文件调整大小。**

命令的参数如下：

```text
VBoxManage modifyhd         <uuid>|<filename>
                            [--type normal|writethrough|immutable|shareable|
                                    readonly|multiattach]
                            [--autoreset on|off]
                            [--compact]
                            [--resize <megabytes>|--resizebyte <bytes>]
```

范例如下（调整后的磁盘大小为4GB）：

```shell
VBoxManage modifyhd windows_xp_4gb.vdi --resize 4000
```

- 第三步：新建一个[gparted](http://gparted.sourceforge.net/ "gparted")的虚拟机挂载调整过大小的VDI文件调整分区即可 [![resize-virtualbox-vdi-file-gparted-vbox](http://farm7.static.flickr.com/6096/6221963657_2853f54f8e.jpg)](http://www.flickr.com/photos/rexzhang/6221963657/ "Flickr 上 Rex Zhang 的 resize-virtualbox-vdi-file-gparted-vbox")
- 最后，在调整完磁盘分区后，用WindowsXP虚拟机开机会提示磁盘异常，让操作系统自行修正即可

另，我尝试过建立 clonezilla 的虚拟机来克隆磁盘，但是出问题的概率较高，不推荐
