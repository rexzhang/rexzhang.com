Debian 5 发布
######################


:author: Rex Zhang
:date: 2009-02-26T22:44:30+08:00
:modified: 2009-02-26T22:44:30+08:00
:status: published
:category: Linux
:tags: Debian

Debian的发布周期明显缩短。而且这次发布整个系统变化很大，很多基础的包都做了升级；所以升级时感觉错误提示不少，提示需要调整配置的包也相当的多。\ `官方出了个相当详细的升级参考 <http://debian.org/releases/stable/i386/release-notes/ch-upgrading.zh_CN.html>`__\ ；大部分情况参照之即可。

我的环境是：

-  debian 4(从3一直维护到现象，未重装）
-  apache在d4的时候已经手工升级到了V2
-  php也是如此。已经到了5
-  mysql为4，但是已经手工升级到4.1+（支持unicode）版本（后来一直跟随维护体系更新）
-  python用的系统默认的2.3
-  未安装X系统，只有命令行。使用ssh远程操作。（值得注意的是这次升级会在升级过程中reload X系统，所以使用图形界面升级的需要注意。估计只能使用命令行）
-  包维护系统在d3时期使用的apt-get。后来转换到的apti
-  内核在d4时期已经手工升级到2.6.x。
-  引导系统用的grub（按照升级参考的说法lilo可能会有问题。建议升级前换成grub）

以下是我的升级路线

-  备份资料
-  先在debian4下面做apti update 和apti upgrade。系统会升级内核到2.6.18版本
-  重启系统。保证新的内核生效。（因为新版本严重依赖新内核）
-  修正可能的依赖和安装问题

   -  根据参考，官方强烈建议使用apti作为未来的维护工具
   -  执行 apti
   -  进入文本界面后按‘g’，会提示有没有需要处理的包。
   -  我就有一个cacti，可能是以前用apt-get安装的。提示需要安装，实际上已经安装并已经正常工作了。选择安装，即可。

-  将deb源修改为d5的

.. code-block:: text

    deb http://mirrors.163.com/debian/ lenny main contrib
    deb-src http://mirrors.163.com/debian/ lenny main contrib
    deb http://mirrors.163.com/debian-security lenny/updates main contrib

-  获取新的升级资源信息 apti update。会有关于认证key不存在的告警。问题不大；并非163.com的源出现问题，而是对D5需要的key在D4中不存在。升级后就正常了

.. code-block:: text

    W: There is no public key available for the following key IDs: 4D270D06F42584E6
    W: You may want to run apt-get update to correct these problems

-  开始最小限度升级 apti safe-upgrade （相当于D4的 apti upgrade）
-  很多重要的模块都会升级到新的版本 libc -> 6, apache -> 2, php -> 5, mysql -> 5, python -> 2.5, 内核 -> 2.6.26
-  升级的过程中会重启几乎所有的重要的模块。特别是libc，这个升级几乎会带动所有的基础模块升级。很多不会有版本升级的模块也因为二进制兼容问题会更新到新的包
-  一起妥当后建议再次reboot；检查基本系统是否工作。
-  同时把所有有过自动升级操作的服务检查一遍。保证其继续在工作

   -  我的 phpmyadmin, trac, cacti, apache就都基本挂了。不过svn升级做得很好，完全没影响
   -  apache是因为修改了虚拟主机的参数只要将自定义的 修改为
      重启就即可解决
   -  phpmyadmin, cacti 则是其默认配置文件做了改动，检查修改一遍即可
   -  trac
      比较麻烦，依赖的python升级了。重新安装一遍即可（其配置与安装时剥离的，重新安装比检查配置来的快）

-  最后来一个完整升级就算完成工作了 apti full-upgrade （相当于D4的 apti dest-upgrade）

说一点点经验。其实更多的算教训

-  重要的服务在D4中已经可以升级到新D5默认版本的建议先手工升级之。可以少很多困扰。
-  官方的发布升级参考很有价值，且有中文版本。建议详细阅读再做升级操作
