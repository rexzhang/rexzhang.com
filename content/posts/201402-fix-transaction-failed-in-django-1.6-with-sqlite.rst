SQLite 环境 Django 1.6  使用老版本代码出现事务异常的临时解决办法
####################################################################################


:author: Rex Zhang
:date: 2014-02-19T23:48:41+08:00
:modified: 2014-02-19T23:48:41+08:00
:status: published
:category: Coding
:tags: Django, SQLite


SQLite对事务机制的支持是不完整的，Django 1.6 开始对事物的支持迁移到了有数据库直接支持。

手上正好有个项目是很久以前的，部分开发调整环境还行想继续使用 SQLite ；一旦遇到有事务处理的代码就提示

.. code-block::

    Your database backend doesn't behave properly when
    autocommit is off. Turn it on before using 'atomic'.

在数据库配置中添加设置均无效。最终还是用强行 hack 的方式暂时解决。希望 Django 团队能在新版本中提供配置允许 SQLite 环境忽略这个异常。方法如下：

修改文件 ``site-packages\django\db\transaction.py`` 242 行

.. code-block:: python

    if connection.features.autocommits_when_autocommit_is_off:
        pass
        #raise TransactionManagementError(
        #    "Your database backend doesn't behave properly when "
        #    "autocommit is off. Turn it on before using 'atomic'.")

参考链接

-  `Django 1.6 TransactionManagementError: database doesn't behave properly when autocommit is off <http://stackoverflow.com/questions/20039250/django-1-6-transactionmanagementerror-database-doesnt-behave-properly-when-aut>`__
-  `Django Database transactions <https://docs.djangoproject.com/en/1.6/topics/db/transactions/>`__
