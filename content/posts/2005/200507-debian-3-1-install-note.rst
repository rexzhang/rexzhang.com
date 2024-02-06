Debian 3.1r0基系统安装
#######################

:author: Rex Zhang
:date: 2005-07-13T07:49:59+08:00
:modified: 2005-07-13T07:49:59+08:00
:status: draft
:category: Linux
:tags: Debian

前几天帮一朋友架设一个BBS论坛系统.因为,选用的是[Molyx](http://www.molyx.com/) (本来是选Free Discuz,无奈Discuz的转换程序不支持附件的转移).因此环境就确定为Linux+Apache2+PHP4+MySQL+mmCache+Zend

下载就不说了,参见之前的一篇[下载Debian](http://www.flord.net/drupal/node/65).下载后,制成一张光盘,开工.

光盘启动都照例直接回车(默认选用的2.4的Kernel).不过3.1较之3.0最大的改变就是多了Installer,不再想3.0那样需要自己去选择需要加载的硬件驱动,一般比较大众化,比较普及的硬件都可以识别出来.减少了不少的工作量. 一路上的配置很简单,切有中文界面,没啥说头.一般只要选择安装程序默认值即可.唯一要提一下的就是硬盘的分区,安装程序有提供3种自动的分区,考虑到维护,不建议采用单一的分区模式.

直到基系统安装完毕.提示登陆系统.使用之前定义的根用户root以及密码登陆后.我的习惯是先安装mc(一个类似PCTOOLS的目录管理工具)和SSH(提供加密的Telnet,我一般不习惯蹲在服务器旁边维护系统,太累)

LS1:~#aptitude install mc ssh

为了在Windows下配合使用加密的ssh,可以下载[PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/)(一个开源免费的Telnet/SSH客户端软件)

另外,因为我的网络中有配置DHCP服务器,因此安装程序没有提示我配置IP地址等信息.不过这不是问题,我们可以编辑/etc/network/interfaces文件来修改她.

LS1:~# nano /etc/network/interfaces

修改

iface eth0 inet dhcp

为

iface eth0 inet static address 192.168.100.11 netmask 255.255.255.0 gateway 192.168.100.2

这样基系统就基本完成了,剩下的就是修改sources list了.不过,在服务器上一个字母一个字母的录入不是我的风格.现在回到自己的位置上去,用PuTTY登陆Server.

LS1:~# nano /etc/apt/sources.list

你会发现里面有一条

deb cdrom:\[Debian GNU/Linux 3.1 r0 \_Sarge\_ - Official i386 Binary-1 (20050605)$

这个表示现在的源是你的光盘.下面就是显示PuTTY+nano可爱之处了.首先,在复制以下的设置文本(我用的是[cn99.com](http://debian.cn99.com/sources.list.cn99)的更新镜像,同时,镜像处的设置还是3.0的,所以我稍微的修改了一下.)

deb [http://debian.cn99.com/debian](http://debian.cn99.com/debian) stable main non-free contrib  
deb [http://debian.cn99.com/debian](http://debian.cn99.com/debian) proposed-updates main contrib non-free  
deb [http://debian.cn99.com/debian-security](http://debian.cn99.com/debian-security) sarge/updates main contrib non-free  
deb-src [http://debian.cn99.com/debian](http://debian.cn99.com/debian) stable main non-free contrib  
deb-src [http://debian.cn99.com/debian](http://debian.cn99.com/debian) proposed-updates main contrib non-free

然后切换到PuTTY,在PuTTY中点击鼠标右键.你会发现PuTTY会将以上信息自动填入正在编辑的文件中.让我们Ctrl+X, Y, 回车存盘推出编辑器.

更新

LS1:~#aptitude update

升级

LS1:~#aptitude upgrade

最后,再把webmin也装上,不过我除了修改一下Cron以为实在用的很少.

LS1:~#aptitude install webmin

webmin默认是只能在本机上访问的,不过为了方便远程维护.修改其配置实现指定的IP地址可访问

~# nano /etc/webmin/miniserv.conf

修改

allow=127.0.0.1

为

allow=192.168.100.100

这里的IP地址192.168.100.100为你平常维护服务器常用的工作站的IP地址. 最后,重启一下webmin服务 ~# /etc/init.d/webmin restart
