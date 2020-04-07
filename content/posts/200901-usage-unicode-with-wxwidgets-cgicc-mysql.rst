wxWidgets CGI MySQL 混合使用UNICODE心得
##################################################################


:author: Rex Zhang
:date: 2009-01-12T07:19:04+08:00
:modified: 2009-01-12T07:19:04+08:00
:status: published
:category: Coding
:tags: wxWidgets, CGI, MySQL, unicode


在写一个程序用到了wxWidgets、CGI、MySQL为使用UNICODE头疼了数天。得下心得如下：

考虑到以后的迁移和多语种兼容，在MySQL中全部表和列包括整个数据库均使用UNICODE。MySQL++做数据库操作。wxWidgets用的UNICODE的编译版本。CGI用的cgicc3.2.7。用户段用的cURL库做提交和获取CGI相应工具

先是数据库
----------

my.ini已经有了

.. code-block::

    [mysql]
    default-character-set=utf8
    [mysqld]
    default-character-set=utf8 (数据库缺省以utf8存储)

使用

.. code-block:: cpp

    wxString qStr(wxT("UPDATE table SET chinese_text = '中文' WHERE uid = 2"));
    mysqlpp::Query query1 = m_pConnection->query(qStr.utf8_str());
    query1.store();

保存到数据库后依然是乱码！很奇怪。最后发现只要在执行query()前再加一条 ``query("SET NAMES UTF8");`` 问题立刻解决。很诡异。

其次是CGI
---------

不管使用何种格式直接提交 ``http://www.mysite.com/cgicc_test.exe?name=中文`` 。cgicc获取到的name字段信息均为乱码。只能将中文信息做urlencode再上传才行

最终的方案为：
--------------

cilent（wxWidgets）

- 将需要提交的中文内容先转换为UTF-8然后再转换为%DD的格式，然后以ANSI编码的方式用cURL提交
- CGI（cgicc）收到即为UTF-8编码格式。传给一个封装后的sql类
- sql类中进行sql语句拼装
- 最后扔给MySQL++执行

成功
