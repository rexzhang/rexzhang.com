flord.net迁移到新的硬件
################################

:author: Rex Zhang
:date: 2006-12-28T07:54:08+08:00
:modified: 2006-12-28T07:54:08+08:00
:status: published
:category: 运维
:tags: Drupal


找到一台快些的旧机器，所以决定给网站搬个家。

迁移开始前用tar+gzip命令将durpal系统下的整个目录打包。然后用\ `MySQL官方的MySQL Administrator </www.mysql.com/products/administrator/>`__\ 备份数据库到PC。

原系统是Ubuntu+Apache2+PHP4+Mysql4.1；新系统打算还是用回Debian。只是要注意的是:Debian默认安装的MySQL为4.0版,其不支持语言设置。所以安装Debian时要特别指定使用MYSQL4.1

.. code-block::

    aptitude install apache2-common apache2-mpm-prefork libapache2-mod-php4 mysql-server-4.1 php4-mysql php4-gd phpmyadmin

回灌很简单。用FTP把 .tar.gz的包解回原路径,然后到数据库灌会新的服务器.连设置都不用改动一下.就可以直接使用了

只是需要注意的是如果drupal有开Cache的话,需要需要清空一下cache这张表,另外,也可以把表sessions清空.以避免出现奇怪的问题
