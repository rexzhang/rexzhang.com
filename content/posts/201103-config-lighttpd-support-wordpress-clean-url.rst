让 lighttpd 支持 wordpress clean url
##################################################################


:author: Rex Zhang
:date: 2011-03-17T05:54:46+08:00
:modified: 2011-03-17T05:54:46+08:00
:status: published
:category: Linux
:tags: WordPress, lighttpd


首先，修改 ``/etc/lighttpd/lighttpd.conf 激活 mod_rewrite`` 模块。格式如下：

.. code-block:: text

    server.modules = (
            "mod_access",
            "mod_alias",
            "mod_compress",
            "mod_redirect",
            "mod_rewrite",
    )

然后在 ``/etc/lighttpd/conf-enabled/10-simple-vhost.conf`` 内添修改如下：

.. code-block:: text

    $HTTP["host"] == "rex.zhang.name" {
        server.document-root = "/www/"
        accesslog.filename = "/var/log/lighttpd/rex.zhang.name.access.log"
        ...
        ...
        url.rewrite = (
            "/wp-admin/$" => "/wp-admin/index.php",
            "^/(.*)\.(.+)$" => "$0",
            "^/(.+)/?$" => "/index.php/$1"
        )
    }

确保网站根目录下的 .htaccess 文件存在，并且在文件权限上可以被执行 lighttpd 的用户可写。最后在 /wp-admin/options-permalink.php 设计自己喜欢的目录格式即可。成功后的 .htaccess 文件内容如下

.. code-block:: text

    <IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteBase /

    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteCond %{REQUEST_FILENAME} !-d
    RewriteRule . / [L]
    </IfModule>

最后重启 web 服务器即可。

另外还有一个超级简单的办法；只需要修改 lighttpd 的配置文件 /etc/lighttpd/conf-enabled/10-simple-vhost.conf ，不用开启 rewrite 都可以工作

.. code-block:: text

    $HTTP["host"] == "rex.zhang.name" {
        ...
        ...

        server.error-handler-404 = "/index.php"
    }

参考链接：

-  http://codex.wordpress.org/Using_Permalinks
-  http://www.guyrutenberg.com/2008/05/24/clean-urls-permalinks-for-wordpress-on-lighttpd/
-  http://redmine.lighttpd.net/wiki/lighttpd/Tutorials
-  http://www.lpfrx.com/archives/445/
-  http://www.nicolaskuttler.com/post/wpmu-lighttpd-rewrite-rules/
-  http://wordpress.org/support/topic/lighttpd-support

Update:

-  20110729:添加对 .htaccess 的设置
-  20110818:添加使用404的一种最精简使用方案
-  20120207:添加解决访问 /wp-admin/ 不显示后台，反而显示前台页面的问题
