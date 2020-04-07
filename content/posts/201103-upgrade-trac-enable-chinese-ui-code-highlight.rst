升级 trac；激活中文界面、语法高亮
######################################


:author: Rex Zhang
:date: 2011-03-17T05:26:27+08:00
:modified: 2011-03-17T05:26:27+08:00
:status: published
:category: Coding
:tags: trac


首先要确定 Debian 系统中是否已经使用 apt 安装过 trac。如果已经安装，为了避免冲突；可以先用 apt 卸载。

然后确定是否有 easy_install 。没有的话可以：

.. code-block::

    aptitude install python-setuptools

安装本地化的模块 Babel。以支持国际化

.. code-block::

    easy_install babel

安装过程类似如下：

.. code-block::

    Searching for Babel
    Reading http://pypi.python.org/simple/Babel/
    Reading http://babel.edgewall.org/
    Reading http://babel.edgewall.org/wiki/Download
    Best match: Babel 0.9.5
    Downloading http://ftp.edgewall.com/pub/babel/Babel-0.9.5-py2.5.egg
    Processing Babel-0.9.5-py2.5.egg
    creating /usr/lib/python2.5/site-packages/Babel-0.9.5-py2.5.egg
    Extracting Babel-0.9.5-py2.5.egg to /usr/lib/python2.5/site-packages
    Adding Babel 0.9.5 to easy-install.pth file
    Installing pybabel script to /usr/bin

    Installed /usr/lib/python2.5/site-packages/Babel-0.9.5-py2.5.egg
    Processing dependencies for Babel
    Finished processing dependencies for Babel


强制升级 trac 到最新的稳定版本

.. code-block::

    easy_install -U trac

或者升级到指定版本

.. code-block::

    easy_install --upgrade Trac==0.12

升级项目文件

.. code-block::

    trac-admin /path/to/projenv upgrade

升级 trac 自带 wiki 的内容

.. code-block::

    trac-admin /path/to/projenv wiki upgrade

重启 web 服务器即可生效。

因为 trac 0.12 版本已经集成国际化信息，所以如果未显示中可以检查两个地方

#. trac.ini 文件内的编码设置(default_charset)是否为 utf-8
#. trac 内帐号登录后，每个账户可以自行选择显示语种

打开语法高亮

在 trac 系统网页 /admin/general/plugin 选中“EnscriptRenderer — Syntax highlighter using GNU Enscript”。并且按照相应模块即可

.. code-block::

    aptitude install enscript

参考链接

-  http://trac.edgewall.org/wiki/TracUpgrade
-  http://www.btsmth.com/show_snapshot.php?en_name=LinuxDev&gid=252192
-  http://jordy.easymorse.com/?p=395
