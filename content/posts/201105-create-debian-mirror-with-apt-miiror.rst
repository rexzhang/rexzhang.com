使用 apt-mirror 生成本地 Debian 源镜像
##########################################################


:author: Rex Zhang
:date: 2011-05-04T20:26:48+08:00
:modified: 2011-05-04T20:26:48+08:00
:status: published
:category: Linux
:tags: Debian, mirror


apt-mirror 是个不错的本地源镜像工具。它可以指定要下载的：发布版本、架构（源代码也视为一种架构类型）、包类型（授权种类、更新种类）。很适合做内部源解决流量、速度和可访问性问题（基本上每次debian做大的升级时，公共源都或多或少的会出些同步问题

安装

.. code-block:: shell

    sudo aptitude install apt-mirror

修改配置文件

安装完成后，会创建一个叫 apt-mirror 的不可登录帐号，以及一个配置文件 ``/etc/apt/mirror.list``

.. code-block:: shell

    sudo nano /etc/apt/mirror.list

修改内容如下：

.. code-block:: text

    #镜像文件已经一些同步日志类的过程文件都会分子目录放在 /YourDebianMirrorPath 下面
    set base_path /YourDebianMirrorPath

    #我选择的镜像源为 ftp.us.debian.org ；发布版本 stable ；架构 amd64。需要其他的部分可以自行添加。如下选择消耗了约 93GB 的磁盘空间
    deb-amd64 http://ftp.us.debian.org/debian wheezy main contrib non-free
    deb-src   http://ftp.us.debian.org/debian wheezy main contrib non-free
    deb-amd64 http://ftp.us.debian.org/debian wheezy-updates main contrib non-free
    deb-src   http://ftp.us.debian.org/debian wheezy-updates main contrib non-free
    deb-amd64 http://ftp.us.debian.org/debian wheezy-proposed-updates main contrib non-free
    deb-src   http://ftp.us.debian.org/debian wheezy-proposed-updates main contrib non-free
    deb-amd64 http://ftp.us.debian.org/debian wheezy-backports main contrib non-free
    deb-src   http://ftp.us.debian.org/debian wheezy-backports main contrib non-free

    deb-amd64 http://ftp.us.debian.org/debian stable main contrib non-free
    deb-src   http://ftp.us.debian.org/debian stable main contrib non-free
    deb-amd64 http://ftp.us.debian.org/debian stable-updates main contrib non-free
    deb-src   http://ftp.us.debian.org/debian stable-updates main contrib non-free
    deb-amd64 http://ftp.us.debian.org/debian stable-proposed-updates main contrib non-free
    deb-src   http://ftp.us.debian.org/debian stable-proposed-updates main contrib non-free
    deb-amd64 http://ftp.us.debian.org/debian stable-backports main contrib non-free
    deb-src   http://ftp.us.debian.org/debian stable-backports main contrib non-free

    clean http://ftp.us.debian.org/debian

如果安装程序没有自动生成 apt-mirror 用户的话，可以手工添加

.. code-block:: shell

    adduser --system apt-mirror

初次同步

下载(老版本40GB容量)在我的 2Mbps 小水管下用了3天2夜。执行方法如下：

.. code-block:: shell

    sudo su - apt-mirror
    apt-mirror

每日自动增量更新的方法

修改 ``/etc/cron.d/apt-mirror`` 取消掉被注释了的命令即可。这样系统会在指定的时间（默认是本地凌晨4点）自动开始同步

配置 apache ，以最终实现在本地提供 http 的镜像源服务

可以创建一个专门的镜像配置文件 ``/etc/apache2/sites-available/mirror`` 。内容如下：

.. code-block:: text

    <virtualhost *:80>
            ServerAdmin webmaster@localhost
            ServerName mirror.SAMPLE.COM

            DocumentRoot /home/mirror/wwwroot

            Alias /debian /YourDebianMirrorPath/mirror/ftp.us.debian.org/debian
            Alias /docs /home/mirror/docs

            <directory />
                    Options FollowSymLinks
                    AllowOverride None
            </directory>

            <directory /home/mirror/wwwroot/>
                    Options Indexes FollowSymLinks MultiViews
                    AllowOverride None
                    Order allow,deny
                    allow from all
                    # This directive allows us to have apache2's default start page
                    # in /apache2-default/, but still have / go to the right place
                    # RedirectMatch ^/$ /apache2-default/
            </directory>

            <directory /YourDebianMirrorPath/mirror/ftp.us.debian.org/debian/>
                    Options Indexes FollowSymLinks MultiViews
                    AllowOverride None
                    Order allow,deny
                    allow from all
                    # This directive allows us to have apache2's default start page
                    # in /apache2-default/, but still have / go to the right place
                    # RedirectMatch ^/$ /apache2-default/
            </directory>

            <directory /home/mirror/docs/>
                    Options Indexes FollowSymLinks MultiViews
                    AllowOverride ALL
                    Order allow,deny
                    allow from all
                    # This directive allows us to have apache2's default start page
                    # in /apache2-default/, but still have / go to the right place
                    # RedirectMatch ^/$ /apache2-default/
            </directory>

            ErrorLog /var/log/apache2/error.log

            # Possible values include: debug, info, notice, warn, error, crit,
            # alert, emerg.
            LogLevel warn

            CustomLog /var/log/apache2/vhost_mirror_access.log combined
            ServerSignature On

    </virtualhost>

使用

重启 apache 应该就可以访问 http://mirror.SAMPLE.COM/debian 查看效果, 修改需要使用本地镜像源的 /etc/apt/sources.list 内容，添加内容类似如下

.. code-block:: text

    deb http://mirror.SAMPLE.com/debian/ stable main contrib non-free
    deb http://mirror.SAMPLE.com/debian/ stable-updates main contrib non-free
    deb http://mirror.SAMPLE.com/debian/ stable-proposed-updates main contrib non-free
    deb http://mirror.SAMPLE.com/debian/ stable-backports main contrib non-free

    #deb http://security.debian.org/ stable/updates main contrib

一些可能的问题

工作目录（/YourDebianMirrorPath）下的文件权限可能因为使用不同 unix 用户执行同步程序而会导致权限的不正常。apache 使用的 www-data 用户可能会没有相应目录的目录执行权限，而出现提示没有权限的错误

修正 apt-mirror 当前发布包中无法正确下载 i18n 文件的方法

如果在 apt update 的时候出现类似如下内容

.. code-block:: text

    Err http://mirror.rex.zhang.name wheezy-proposed-updates/contrib Translation-en 404  Not Found
    Err http://mirror.rex.zhang.name wheezy-proposed-updates/main Translation-en 404  Not Found

编辑文件 ``/var/spool/apt-mirror/var/postmirror.sh`` 添加如下内容

.. code-block:: shell

    for part in wheezy wheezy-updates wheezy-proposed-updates wheezy-backports; do
        cd /var/spool/apt-mirror/mirror/ftp.us.debian.org/debian/dists/$part

        for directory in contrib main non-free; do
            cd $directory
            mkdir i18n 2>/dev/null
            cd i18n
            rm Translation-en*
            wget http://ftp.us.debian.org/debian/dists/$part/$directory/i18n/Translation-en.bz2
            cd ../../

参考

#. http://apt-mirror.sourceforge.net/
#. http://www.linuxeden.com/html/sysadmin/20090518/65717.html

update

-  20140903 添加对 backports 的支持
-  20140912 添加不能 i18n 文件下载问题
