创建、合并 Hg 分支
######################


:author: Rex Zhang
:date: 2012-05-04T08:27:48+08:00
:modified: 2012-05-04T08:27:48+08:00
:status: published
:category: Coding
:tags: Hg


创建分支
---------

Hg 的分支相对于 Git 没那么随意，如果要实现偏 Git 风格分支可以使用 bookmark 也就是书签功能 创建需要两步：

#. 设置新的分支名称
#. commit

命令行方式如下（其中的 release 为将要创建的新分支名称）：

.. code-block::

    hg branch release
    hg commit

hg branch release hg commit [/code]

如果使用 TortoiseHg 来实现的话：直接点击提交界面的『分支按钮』创建新的分支名称，然后『commit』即可

如要将本地新建的分支推送到远端的代码托管服务器上可以使用命令（使用 TortoiseHg Push 时其会自动代劳）：

.. code-block::

    hg push --new-branch

合并分支
--------

根据 Hg 的设计特征， Hg 似乎是不推崇创建大量分支来作为开发手段，其中一个很重要的特性就是没有删除分支这一功能！所有分支只能关闭，或者任由其存在。 如果实在要合并某一个以后不再使用的开发分支，有一个变通的方式。简单的说就是：

#. update 到需要关闭的分支 needCloseBranch
#. 关闭 needCloseBranch 分支
#. update 到需要合并后保留的分支 default
#. 合并 needCloseBranch 到 default

最终 needCloseBranch 这个分支并不会真正消失，不过在默认情况（不显示已关闭分支）下是看不到的

以下是命令行的范例（支持 hg 2.x 版本）

.. code-block::

    hg update needCloseBranch
    hg commit --close-branch #关闭功能在 TortoiseHg 是没有的，只能在命令行操作
    hg update default
    hg merge needCloseBranch

查看当前分支
------------

.. code-block::

    hg branch

列出所有分支
------------

.. code-block::

    hg branches
