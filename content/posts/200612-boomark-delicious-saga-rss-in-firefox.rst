本地书签、del.icio.us、Saga/RSS混战Firefox插件系统
############################################################################

:author: Rex Zhang
:date: 2006-12-02T01:18:26+08:00
:modified: 2006-12-02T01:18:26+08:00
:status: published
:category: 数字生存
:tags: Firefox, 书签


从前。。。我喜欢在Firefox（后统一称FF）中创建不同的目录来将常用的链接和RSS分别放在不同的子目录下。然后将常用链接的目录设置为“书签工具条|Bookmark toolbar”。相安无事了许久。

某日，再也忍受不了在多个机器间同步书签的麻烦。虽然有FTP空间帮忙同步的中转，但终归是要人力介入。而且纯树型分类也不太适合一个网站有多个属性的特点。当然与人交流就更不方便了。遂打算用一网上的、有Tag特性的、带一定社交性质的书签网站替代之

在FF的插件网站转了一圈，发现del.icio.us是符合我的要求的咚咚。而且我也用它的基础版本一段时间了

OK，装上\ `del.icio.us完整版插件 <https://addons.mozilla.org/firefox/3615/>`__\ ，导入本地的书签到del.icio.us。感觉不错，本地书签就是del.icio.us上的书签，每次修改都实时的自动的更新到del.icio.us网站。顿时觉得轻松了不少。

且慢，发现问题！

#. 导入的书签需要添加Tag整理，这个不算问题了
#. 书签的RSS部分导入后基本都是乱码，而且Saga没法使用。晕倒，还好作这个操作前有用Saga备份了OPML文件。万幸。看来要为这个解决方案付出点代价了。还好试用了 `Google Reader <https://www.google.com/reader>`__\ 后，决定以后的RSS部分就交给Reader来处理。两者差不多，都依赖浏览器，阅读信息都必须处于在线状态，这个对使用习惯几无改变。而且新版的FF支持直接把RSS收录到几个知名的RSS阅读器中（当然包括Reader）很是方便
#. del.icio.us的书签是完全基于Tag和搜索的，要做树型分类还没招。每次要访问常用链接还要再搜索一下。del.icio.us的书签工具条替换掉了FF自身的那个。虽然其工具条有Most
   Visited 选项，但是能显示的太少。暂时无解

又折腾了些时日。想到的一个勉强的办法。装一个提供Google所有服务按钮的插件，先简化到几个常用的Google服务的操作。进入眼帘的有2个。试了一下，两个感觉都差别不大。

`GButts! <https://addons.mozilla.org/firefox/3576/>`__

可以控制具体的某个服务按钮的显示与否；可以控制是以下拉菜单模式显示，还是全部并排显示。不过在下拉菜单模式下有Bug，显示不完整。另外要注意的是，需要手动定制一下工具栏。把它拖动到指定的位置才能显示

`GUtil! <https://addons.mozilla.org/firefox/3755/>`__

只有下拉菜单模式；提供的按钮是固定的，不可以自定义。不过有预先分类，界面要清晰一些

都不是很满意，况且两者不冲突。就都装着慢慢比对了
