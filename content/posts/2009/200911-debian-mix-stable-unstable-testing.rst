debian stable、unstable、testing混合系统安装方法
############################################################################


:author: Rex Zhang
:date: 2009-11-21T01:12:40+08:00
:modified: 2009-11-21T01:12:40+08:00
:status: published
:category: Linux
:tags: Debian


Debian的稳定版非常好用。不过偶尔也会需要非稳定版本下的软件或者软件版本。

比如：现在我就遇到这个问题了。当前Debian的stable版本是lenny，unstable版本是squeeze。稳定版本中的Ice是3.2.1
。这个版本的Ice有个bug。

python版本如果使用Ice的Interface（接口）传递unicode对象会导致致命性错误。这个错误在Ice3.0.0得到了纠正，但是只有debian的非稳定版本才有>=3.0.0的Ice。

这个时候就非常有必要在debian稳定版下单独安装squeeze下的Ice了。

当前环境是：debian的lenny版，已经安装Ice，并且有依赖Ice的软件包。混合步骤如下：

首先，在 ``/etc/apt/apt.conf`` 文件（正常情况没有这个文件，需要创建）中添加如下内容：

.. code-block:: text

    APT::Default-Release "stable";

然后编辑 ``/etc/apt/sources.list`` 文件，添加如下内容：

.. code-block:: text

    deb http://mirrors.163.com/debian squeeze main non-free contrib
    deb-src http://mirrors.163.com/debian squeeze main non-free contrib

更新软件包列表

.. code-block:: shell

    # aptitude update

安装 squeeze版本的 python-zeroc-ice

.. code-block:: shell

    # aptitude install -t squeeze python-zeroc-ice

aptitude会自动帮你将旧版的 python-zeroc-ice 升级到新版；并安装相应的依赖包。现在新的版本就已经搞定；不过还有一点点依赖问题。

执行 aptitude upgrade 就会发现系统要你更新一大堆 stable 不需要更新的包。解决办法如下：

首先，注释掉 ``/etc/apt/sources.list`` 新添加的源信息

然后再执行 aptitude update 即可

一些参考链接：

- http://zhuaxia.spaces.live.com/Blog/cns!71787D3A37FFC48A!461.entry?ppud=4&wa=wsignin1.0&sa=221919623
- http://www.debian.org/doc/manuals/apt-howto/ch-apt-get.zh-cn.html
- http://www.debian.org/doc/manuals/debian-reference/ch-package.zh-cn.html#s-mixedsys
- http://www.debian.org/doc/manuals/debian-reference/ch02.en.html#_packages_from_mixed_source_of_archives

注：

aptitude 在lenny下对 /etc/apt /preferences有一点点问题不建议使用
