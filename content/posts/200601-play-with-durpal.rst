去掉网站中的drupal路径，将整个www.flord.net全部整合到Drupal中
#############################################################

:author: Rex Zhang
:date: 2006-01-14T00:29:27+08:00
:modified: 2006-01-14T00:29:27+08:00
:status: published
:category: 运维
:tags: 域名, Drupal

使用Drupal已经快1年了。越用越觉得Drupal这样的CMS系统而非Blog系统适合我。可预见的未来也就不打算再更换系统。因此，今天将原有的www.flord.net/[STRIKEOUT:drupal]\ 中的\ *drupal*\ 去掉，配合原有的Clean URL让整个URL显得更加简洁。

由于Drupal使用的全部是相对路径。所以整个系统都跟主机域名、父目录无关。而决定域名和目录的设置只有一行。那就是 sites/xxxxxx/settings.php 中的

    $base_url = 'http://www.flord.net';

当然只修改这一处是不行的。还需要修改Apache中关于www.flord.net这个虚拟主机的根目录(DocumentRoot)设置。然后重起一下Apache即可。

不过又遇到一个问题：

    Drupal的.htaccess文件修改了目录的访问规则（比如Drupal把默认的首页。限定为index.php）而我有一些脱离于Drupal的静态页面要展示。它们的默认首页是index.htm或index.html

因此非常有必要在子目录下使用.htaccess重定义相应设置。以www.flord.net/mirror为例：

这里放置的是我做的RFC中文化的镜像文件。我需要他能在没有index文件的时候，能够使用Apache的自动列表功能将其下的目录和文件显示出来。同时，
支持index.htm和index.html作首页

具体的设置如下：

在 mirror 目录下创建一个 .htaccess 文件

在文件中添加允许自动索引的选项

    Options +Indexes

在文件中修改默认首页的文件名

    DirectoryIndex index.html index.html
