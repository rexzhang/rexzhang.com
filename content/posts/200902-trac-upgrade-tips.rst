Trac 安装笔记
##################


:author: Rex Zhang
:date: 2009-02-26T23:33:46+08:00
:modified: 2009-02-26T23:33:46+08:00
:status: published
:category: Coding
:tags: trac


我们开发用的项目管理系统是Trac。很好用，其安装也几乎可以用傻瓜来形容。因为升级Debian，重装了下，顺便笔记如下

先装支持和依赖库

.. code-block:: shell

    aptitude install python-pysqlite2 python-subversion python-support libapache2-mod-python
    aptitude install python-dev python-tz

安装 easy_install 。easy_install 是 py 的安装工具，安装时会自动到互联网上寻找最新的稳定版并下载安装之（太适合我这种懒人了！）

.. code-block:: shell

    aptitude install python-pip

安装 Trac 需要是依赖包（python库）

.. code-block:: shell

    root@pip install pytz #国际时区支持
    root@pip install babel==0.9.6 #国际化支持
    root@pip install Genshi
    root@aptitude install python-clearsilver #pip/easy_install 安装这个包会出现问题

如果直接安装最近版本的 babel (v1.2)包,会得如下错误

.. code-block:: text

    AttributeError: NullTranslationsBabel instance has no attribute 'isactive'

解决方法是安装 trac v1.0.1 对应的 babel v0.9.6

安装Trac

.. code-block:: shell

    pip install Trac

初始化一个新的Trac项目

.. code-block:: shell

    mkdir /yourTracProjPath
    trac-admin /yourTracProjPath initenv

创建一个密码本，保存访问用户的帐号和密码

我用的是apache集成的认证系统

创建一个svn项目（如果你还没有的话）

.. code-block:: shell

    svnadmin create /yourSvnPath

添加一个虚拟主机

.. code-block:: text

    <virtualhost *:80>
        DocumentRoot /yourTracProjPath
        ServerName YourProjUrl.com
        <location />
            SetHandler mod_python
            PythonInterpreter main_interpreter
            PythonHandler trac.web.modpython_frontend
            PythonOption TracEnv /yourTracProjPath
            PythonOption TracUriRoot /
        </location>
        <location /login>
            AuthType Basic
            AuthName "MyCompany Trac Server"
            AuthUserFile /YourPassSavePath/trac.htpasswd
            Require valid-user
        </location>
    </virtualhost>

修改Trac配置

.. code-block:: shell

    cd /yourTracProjPath/conf
    nano tarc.ini

让apache能访问你的trac项目目录（很重要，权限不正确就完全不能工作）

.. code-block:: shell

    chown -R www-data:www-data /yourTracProjPath

重启apache即可

.. code-block:: shell

    /etc/init.d/apache2 restart

设置 Trac 管理帐号

.. code-block:: shell

    trac-admin /yourTracProjPath permission add YourAddUserName TRAC_ADMIN

UPDATE

- 20120614 重新排版
- 20140624 更新 clearsilver babel 安装方法
