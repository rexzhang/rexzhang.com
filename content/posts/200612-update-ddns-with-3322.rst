希网/3322.org动态域名更新方法
######################################

:author: Rex Zhang
:date: 2006-12-30T03:35:11+08:00
:modified: 2006-12-30T03:35:11+08:00
:status: published
:category: 数字生存
:tags: 域名

用3322不少时间了。感觉其支持的协议也一直在细微的变化。经过筛算发现当前“希网/3322.org”支持的动态域名更新方法有两种：

#. 基于客户端更新方式
#. 基于命令行的方式。其网页上用lynx访问www.3322.org的方式似乎已经不奏效通过实验发现如下格式依然是有效的；并且支持本地服务器在NAT网关后的情况

.. code-block::

    wget “http://username:password@member.3322.org/dyndns/update?system=dyndns&hostname=yourdomian.3322.org&mx=aspmx.l.google.com”

20071022更新
-------------

member.3322.org域名已经不可用，不过吧member.3322.org直接替换为www.3322.org依然可以继续使用
