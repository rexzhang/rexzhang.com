小内存环境下配置 php mysql lighttpd
######################################################


:author: Rex Zhang
:date: 2011-04-21T05:10:09+08:00
:modified: 2011-04-21T05:10:09+08:00
:status: published
:category: Linux
:tags: MySQL, lighttpd


lighttpd 修改 /etc/lighttpd/conf-enabled/15-fastcgi-php.conf

.. code-block:: text

    fastcgi.server += ( ".php" =>
            ((
                    "bin-path" => "/usr/bin/php-cgi",
                    "socket" => "/tmp/php.socket",
                    "max-procs" => 1,
                    "bin-environment" => (
                            "PHP_FCGI_CHILDREN" => "2",
                            "PHP_FCGI_MAX_REQUESTS" => "1000"
                    ),
                    "bin-copy-environment" => (
                            "PATH", "SHELL", "USER"
                    ),
                    "broken-scriptfilename" => "enable"
            ))
    )

这里有一个 lighttpd 进程数量的计算公式。很适合在小内存环境用来控制 php 进程的数量，进而控制内存使用情况，以避免因大量的 swap 动作拖慢整个系统的性能。不过这样设置的代价是不能接受大量的并发请求，只适合小流量的个人网站

.. code-block:: text

    num-procs = max-procs * ( 1 + PHP_FCGI_CHILDREN )

num-procs 为最大允许的 php 进程数量。以 lighttpd 官方说明的每进程最大消耗 13MB 内存为依据。如上配置的 lighttpd 最多

会有： 1 * (1 + 2) = 3 个进程

消耗： 1 * (1 + 2) * 13MB = 39MB

mysql 修改 /etc/mysql/my.cnf

.. code-block:: text

    thread_cache_size       = 4 #减少mysqld 的进程数量
    skip-innodb #关闭对 innodb的支持

另外，也可以调小一些 buffer 类参数的设置

参考链接
- http://redmine.lighttpd.net/projects/lighttpd/wiki/Docs:PerformanceFastCGI
