解决Drupal跨站登陆的问题
###########################

:author: Rex Zhang
:date: 2006-09-14T05:59:45+08:00
:modified: 2006-09-14T05:59:45+08:00
:status: published
:category: 运维
:tags: Drupal

以前一直无法用我在这个网站的帐号直接登陆DrupalChina.org.今天认真研究了一下Drupal的跨站登陆问题. 找到问题的症结所在：

是我的drupal模块的设置有问题。主要是没有打开发送本站帐号信息的选项。设置在“主页 » 管理 » 设置 » Drupal”.

#. 先启用“Post data to another site“下的”Register with a Drupal server”
#. 然后启用“Receive data from other sites”下的“Allow other Drupal sites to register”即可

注1：Drupal跨站登陆是指：当你有某一个基于Drupal系统（A）的网站的帐号时，不必在其他的Drupal系统（B）网站上重新注册。可以使用"YourID@DrupalSiteA.ext"格式的用户名以及在这个网站上的密码直接在其他Drupal系统（B）网站上登陆

注2：要达到注1所说效果需要：（A）打开允许“Allow other Drupal sites to register”；同时（B）打开“Authentication service:”
