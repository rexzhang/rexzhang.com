Debian 3.1r0基系统安装
#######################

:author: Rex Zhang
:date: 2005-07-13T07:49:59+08:00
:modified: 2005-07-13T07:49:59+08:00
:status: draft
:category: Linux
:tags: Debian

<p>
   前几天帮一朋友架设一个BBS论坛系统.因为,选用的是<a href="http://www.molyx.com/">Molyx</a> (本来是选Free Discuz,无奈Discuz的转换程序不支持附件的转移).因此环境就确定为Linux+Apache2+PHP4+MySQL+mmCache+Zend 
</p>
<p>
   下载就不说了,参见之前的一篇<a href="http://www.flord.net/drupal/node/65">下载Debian</a>.下载后,制成一张光盘,开工. 
</p>
<p>
   光盘启动都照例直接回车(默认选用的2.4的Kernel).不过3.1较之3.0最大的改变就是多了Installer,不再想3.0那样需要自己去选择需要加载的硬件驱动,一般比较大众化,比较普及的硬件都可以识别出来.减少了不少的工作量.
   一路上的配置很简单,切有中文界面,没啥说头.一般只要选择安装程序默认值即可.唯一要提一下的就是硬盘的分区,安装程序有提供3种自动的分区,考虑到维护,不建议采用单一的分区模式. 
</p>
<p>
   直到基系统安装完毕.提示登陆系统.使用之前定义的根用户root以及密码登陆后.我的习惯是先安装mc(一个类似PCTOOLS的目录管理工具)和SSH(提供加密的Telnet,我一般不习惯蹲在服务器旁边维护系统,太累) 
</p>
<p>
   LS1:~#aptitude install mc ssh 
</p>
<p>
   为了在Windows下配合使用加密的ssh,可以下载<a href="http://www.chiark.greenend.org.uk/~sgtatham/putty/">PuTTY</a>(一个开源免费的Telnet/SSH客户端软件) 
</p>
<p>
   另外,因为我的网络中有配置DHCP服务器,因此安装程序没有提示我配置IP地址等信息.不过这不是问题,我们可以编辑/etc/network/interfaces文件来修改她. 
</p>
<p>
   LS1:~# nano /etc/network/interfaces 
</p>
<p>
   修改 
</p>
<p>
   iface eth0 inet dhcp 
</p>
<p>
   为 
</p>
<p>
   iface eth0 inet static<br />
       address 192.168.100.11<br />
       netmask 255.255.255.0<br />
       gateway 192.168.100.2 
</p>
<p>
   这样基系统就基本完成了,剩下的就是修改sources list了.不过,在服务器上一个字母一个字母的录入不是我的风格.现在回到自己的位置上去,用PuTTY登陆Server. 
</p>
<p>
   LS1:~# nano /etc/apt/sources.list 
</p>
<p>
   你会发现里面有一条 
</p>
<p>
   deb cdrom:[Debian GNU/Linux 3.1 r0 _Sarge_ - Official i386 Binary-1 (20050605)$ 
</p>
<p>
   这个表示现在的源是你的光盘.下面就是显示PuTTY+nano可爱之处了.首先,在复制以下的设置文本(我用的是<a href="http://debian.cn99.com/sources.list.cn99">cn99.com</a>的更新镜像,同时,镜像处的设置还是3.0<woody>的,所以我稍微的修改了一下.) 
</p>
<p>
   deb <a href="http://debian.cn99.com/debian">http://debian.cn99.com/debian</a> stable
   main non-free contrib<br />
   deb <a href="http://debian.cn99.com/debian">http://debian.cn99.com/debian</a> proposed-updates
   main contrib non-free<br />
   deb <a href="http://debian.cn99.com/debian-security">http://debian.cn99.com/debian-security</a> sarge/updates
   main contrib non-free 
   <br />
   deb-src <a href="http://debian.cn99.com/debian">http://debian.cn99.com/debian</a> stable
   main non-free contrib<br />
   deb-src <a href="http://debian.cn99.com/debian">http://debian.cn99.com/debian</a> proposed-updates
   main contrib non-free 
</p>
<p>
   然后切换到PuTTY,在PuTTY中点击鼠标右键.你会发现PuTTY会将以上信息自动填入正在编辑的文件中.让我们Ctrl+X, Y, 回车存盘推出编辑器. 
</p>
<p>
   更新 
</p>
<p>
   LS1:~#aptitude update 
</p>
<p>
   升级 
</p>
<p>
   LS1:~#aptitude upgrade 
</p>
<p>
   最后,再把webmin也装上,不过我除了修改一下Cron以为实在用的很少.
</p>
<p>
   LS1:~#aptitude install webmin
</p>
<p>
   webmin默认是只能在本机上访问的,不过为了方便远程维护.修改其配置实现指定的IP地址可访问
</p>
<p>
   ~# nano /etc/webmin/miniserv.conf
</p>
<p>
   修改
</p>
<p>
   allow=127.0.0.1
</p>
<p>
   为
</p>
<p>
   allow=192.168.100.100
</p>
<p>
   这里的IP地址192.168.100.100为你平常维护服务器常用的工作站的IP地址.

最后,重启一下webmin服务
~# /etc/init.d/webmin restart</p>
