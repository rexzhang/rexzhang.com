网站从Drupal转换到WordPress系统
##############################################


:author: Rex Zhang
:date: 2011-02-23T20:40:07+08:00
:modified: 2011-02-23T20:40:07+08:00
:status: published
:category: 运维
:tags: Drupal, WordPress

起因很简单，drupal是个内容管理系统，wordpress是一个内容发布系统。就个人应用而言，发布的需求远远大于管理的需求；至少我这么多年来就没多少文章需要管理。

转换的过程很简单。步骤如下：
----------------------------

1.安装wordpress 2.7版 因为我找到的转换脚本是支持 drupal6.x > wordpress2.7 的。安装过程就不累述了，需要注意的是

-  wordpress 安装后会自动生成一个 admin 用户以及一个密码，需要记下来。不然后面麻烦
-  数据库前缀保留默认的 wp\_
-  这个数据库我们称为 dbWordpress27

2.混合数据库 将 drupal6.x 的数据库内容导入到 dbWordpress27

-  我用的是 phpmyadmin
-  用“操作”中的“复制数据库”
-  不要选中 (CREATE DATABASE)

3.转换数据库内容 按照 http://socialcmsbuzz.com/convert-import-a-drupal-6-based-website-to-wordpress-v27-20052009/ 的步骤，一步一步吧 SQL 语句复制到 phpmyadmin 执行即可

-  参考链接：\ http://codex.wordpress.org/Importing_Content#Drupal

转换完毕后删除所有非 wp\_ 开头的表 4.升级 wordpress 至最新版本

遗留的问题和遗憾：
------------------

- 这个脚本不能转换 drupal 的 clean url 。丢失好多
- 所以 drupal 来的文章都会归到 wordpress.users id 为0的用户名下
- drupal 下注册用户的评论都变成了匿名的了
