LinkSYS RTP300 firmware升级
##################################################

:author: Rex Zhang
:date: 2007-06-19T22:01:08+08:00
:modified: 2007-06-19T22:01:08+08:00
:status: published
:category: 数字生存

到手一个LinkSYS的带SIP网关的小路由器RTP300。其软件是1.00.xx（\ `Vonage <http://www.vonage.com>`__\ ）的软件版本而非3.1.xx的\ `公版 <http://www.linksys.com>`__\ 。找不到设置SIP的页面，更找不到软件升级的地方；也无法使用LinkSYS官方网站上提供的firmware。后在\ `OpenWrt <http://openwrt.org>`__\ 发现一个\ `整理了的firmware清单 <http://wiki.openwrt.org/OpenWrtDocs/Hardware/Linksys/WRTP54G>`__

根据网上的提示使用 admin/admin （用户名/密码）登录 http://192.168.15.1 后。再用 user/tivonpw 登录 http://192.168.15.1/update.html 失败。

放狗搜索发现因为用的是1.00.xx系列的firmware，需要在升级firmware需要先解开管理密码。网上有叫\ `CYT Device Unlock的解锁工具 <http://www.bargainshare.com/index.php?showtopic=87504&st=0>`__\ 。我用的是cyt49Beta版（\ `cyt46_win32.zi <http://www.dslreports.com/r0/download/1098007%7E6f3e709c3920e98e7ad7277378f5d6a7/cyt46_win32.zip>`__\ `p <http://www.dslreports.com/r0/download/1098007%7E6f3e709c3920e98e7ad7277378f5d6a7/cyt46_win32.zip>`__\ ）。

-  先连接好RTP300
-  将RTP300的IP地址恢复为出厂默认的 192.168.15.1
-  PC的IP地址可以设置成自动获取（RTP300默认会分配给你。如果RTP300的DHCP被关掉了的话，可以手动设置成 192.168.15.100)
-  打开IE浏览器，访问 http://192.168.15.1 ；使用 admin/admin 登录
-  将cyt解包到硬盘
-  双击运行cyt
-  会出现一个DOS窗口，并提供了菜单化的界面
-  选择（ 1 ）,程序将会自动开始重置设备密码；并会需要你回车确定修改密码，回车；等待程序提示Configure
   is complete
-  在IE中访问 http://192.168.15.1/update.html 升级firmware；使用 Admin/Admin 登录（注意是大写的A）
-  在IE中访问 http://192.168.15.1/Voice_adminPage.html 配置语音部分；使用 Admin/Admin 登录（SIP）

RTP300的用户登录分为几个级别。普通的管理员是 admin/admin ；超级用户是 Admin/Admin 。登录超级用户前需要先用普通管理帐号登录所以当使用超级用户登录报错的时候；先使用普通帐号登录进去，再重新访问特别的隐藏页面。
