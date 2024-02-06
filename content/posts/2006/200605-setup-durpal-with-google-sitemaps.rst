使用robotstxt和gsitemap模块简化Google Sitemaps提交
#######################################################

:author: Rex Zhang
:date: 2006-05-19T15:39:00+08:00
:modified: 2006-05-19T15:39:00+08:00
:status: published
:category: 运维
:tags: Drupal, Google

`robotstxt <http://drupal.org/project/robotstxt>`__\ 是一个辅助生成 http://YourDrupalRoot/robots.txt 文件的模块.而robots.txt是可以帮助站长告知网络蜘蛛(搜索引擎的机器人)那些目录不要被收录,而那些希望被收录的咚咚.详细可以见\ `robotstxt.org <http://www.robotstxt.org/wc/robots.html>`__

`gsitemap <http://drupal.org/project/gsitemap>`__\ 是一个辅助Drupal站长提交\ `Google Sitemaps <http://www.google.com/webmasters/sitemap>`__\ 的模块.其可以工作在两种不同的模式.

#. 配合Sitemaps账号的设置,提供Sitemap.xml文件
#. 没有Sitemaps账号的情况下主动提交Sitemap.xml文件(我不知道这样是否有效,只是在WatchDog中看到主动提交成功,因我有Sitemaps账号所以也没有深究)

在安装上以上2个模块后：

第一步、先配置robotstxt模块,其默认的配置如下
--------------------------------------------

.. code-block:: text

    User-agent: *  Disallow: /node/  Disallow: /database/  Disallow: /includes/  Disallow: /misc/  Disallow: /modules/  Disallow: /sites/  Disallow: /themes/  Disallow: /admin/

需要注意的是需要将 `Disallow: /node/` 这一行去掉, node 可是Drupal的基本页面单元。

可以使用浏览器访问地址 http://YourDrupalRoot/robots.txt 来检查。如果看到以上的配置文本即配置成功。

第二步、确认sitemap.xml地址
--------------------------------------------

gsitemap默认生成的地址是 http://YourDrupalRoot/gsitemap\ 。而Google Sitemaps对非.xml结尾的地址似乎有问题。总是提示找不到。

解决方法就是使用Drupal系统自带的path(url_alias/Url别名)模块设置一个gsitemap.xml到 gsitemap的别名。

第三步A、配置gsitemap模块主动提交
--------------------------------------------

方法很简单:只需要在模块配置中的 `Other Settings` 中勾选上有 `Submit sitemap to Google` 的两项即可。到底有效与否不知道 ;-P

第三步B、配置gsitemap模块适应Sitemaps账号
--------------------------------------------

#. 在Google Sitemaps的Sitemaps地址一栏填写：\ http://YourDrupalRoot/gsitemap.xml
#. 选 使用上传文件的方式 验证网站
#. 复制下给出的文件名，将这个文件名粘贴到模块设置 Other Settings 中的 Verification link

    剩下的就是等待迎接Google的蜘蛛人。;-)
