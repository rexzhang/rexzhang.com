wxWidgets & Code::Blocks Studio
###################################

:author: Rex Zhang
:date: 2006-01-21T23:01:00+08:00
:modified: 2006-01-21T23:01:00+08:00
:status: published
:category: Coding
:tags: wxWidgets, IDE

近来无事想写一个小程序，又不想花太多时间在UI上；就想起了一直关注的wxWidgets(以前叫wxWindows，据说是因为微软施压才改的名)。选用他的理由有三：

#. 只会C。。。
#. 不想因为界面设计而花太多时间
#. wxWidgets已经有了像\ `wxGlade <http://wxglade.sourceforge.net/>`__\ 这样的东东，画个简单的界面什么的足够了
#. 我的服务器已经都转换到了Linux；而桌面电脑随着时间的推移已经逐步的将常用的程序切换成了跨Windows/Linux的版本。所以学习一个跨平台的UI比较能够做到知识的保值
#. wxWidgets中的wxString类提供了统一的一个字符串操作界面。一些常用的文本处理函数不用再创建了；这个我喜欢
#. 开源、免费！

下一步就是选择IDE
-----------------

主要焦点在\ `MinGW Developer Studio <http://www.parinyasoft.com/mingwstudio.html>`__\ 和\ `Code::Blocks Studio <http://www.codeblocks.org/>`__\ 这两个跨平台(都使用的是wxWidgetsUI库)的免费软件之间：

#. MinGW Developer Studio使用感觉还不错。有预编译的wxWidgets库；入门方便(编译wxWidgets库遇到的问题多多，后面慢慢讲)
#. Code::Blocks Studio提供插件接口而且最重要的是更新快。这方面MinGW Developer Studio就差多了，活跃的开发团队是开源项目发展的关键！

当然差别还有很多。我是菜菜鸟看得到的就这些。。。

安装Code::Blocks Studio
-----------------------

Code::Blocks Studio现在发布的是RC2(还没有正式版)。但RC2问题多多(我发现的就有对Unicode编译的支持问题)；不过有Nightly Builds可以解决。我的解决步骤是：

#. 先下载并安装\ `RC2整合MingW的版本 <http://prdownloads.sourceforge.net/codeblocks/codeblocks-1.0rc2_mingw.exe?download>`__\ ，这样也就不用再去下载MingW(MingW下载包太多了，安装头痛)
#. 下载\ `Nightly Builds <http://forums.codeblocks.org/index.php?board=20.0>`__ (现在登陆C::B这个论坛要注册，前几天都还可以匿名的)中的 `Unicode wxWidget动态支持库 <http://download.berlios.de/codeblocks/wxmsw26u_gcc_cb.7z>`__\ (新版的C::B已经使用Unicodede发布)
#. 将两个包中文文件解压覆盖到 C:\Program Files\CodeBlocks

安装wxWdigets
-------------

#. 我在\ `wxWidgets官方下载页面 <http://www.wxwidgets.org/downld2.htm>`__\ 上下载的\ `wxMSW v2.6.2 的ZIP版 <http://prdownloads.sourceforge.net/wxwindows/wxMSW-2.6.2.zip>`__
#. 解到\ *D:\\*\ (安装完成后的路径为：\ *D:\wxWidgets-2.6.2*\ ，之后的设置都用的是这个路径)

编译wxWdigets(支持ODBC)
-----------------------

#. 首先编辑\ *D:\wxWidgets-2.6.2\include\wx\msw\setup.h*\ 以便编译后的动/静态库文件支持ODBC(为了让编译出来的库支持ODBC，我至少编译了4次才找到原来还要在这儿修改。虽然wxWidgets的手册上写要修改setup.h不过没有具体说是那个目录下的。。。吐血)。修改内容如下：
#. 将文件中的\ ``#define wxUSE_ODBC 0``\ 修改为\ ``#define wxUSE_ODBC 1``
#. 然后我在\ *D:\wxWidgets-2.6.2\build\msw*\ 下创建了一个\ **envset.bat**\ 文件来设置编译需要的环境参数。内容如下

.. code-block::

    set PATH=%PATH%;C:\Program Files\CodeBlocks\bin;C:\Program Files\CodeBlocks\mingw32\bin;set LIBRARY_PATH=C:\Program Files\CodeBlocks\libset C_INCLUDE_PATH=C:\Program Files\CodeBlocks\includeset CPLUS_INCLUDE_PATH=C:\Program Files\CodeBlocks\include;D:\wxWidgets-2.6.2\include;D:\wxWidgets-2.6.2\contrib\include;

..

   其中\ *C:\Program Files\CodeBlocks*\ 是我的C::B的安装路径

#. 同时修改\ *D:\wxWidgets-2.6.2\build\msw\config.gcc*

    将\ ``USE_ODBC = 0``\ 修改为\ ``USE_ODBC = 1``

#. 进入DOS命令行
#. 切换工作路径至 D:\wxWidgets-2.6.2\build\msw
#. 运行\ envset.net
#. 执行清理命令

.. code-block::

    mingw32-make -f makefile.gcc USE_XRC=1 SHARED=1 MONOLITHIC=1 BUILD=debug UNICODE=1 clean

其中
    #. SHARED=1表示生成的动态链接库DLL，0就是静态链接库
    #. MONOLITHIC=1表示生成单一的库文件，0表示生成多个按模块分割的库文件
    #. BUILD=debug表示生成带Debug信息的版本方便调试，release是发布版
    #. UNICODE=1表示使用unicode编码

#. 执行编译命令

.. code-block::

      mingw32-make -f makefile.gcc USE_XRC=1 SHARED=1 MONOLITHIC=1 BUILD=debug UNICODE=1 VENDOR=cb

#. 看看电视，泡壶茶。编译的时间可不短;-)

整合C::B和wxWidgets
-------------------

#. 运行C::B。程序会提示你填写wxWidgets的安装目录
#. |codeblock-wx-global-var-set.png|
#. 然后使用新建向导创建一个\ **Using UNICODE wxWidgets DLL**\ 的wxWidgets Appliction就可以开始了
#. |codeblock-wx-create-project.png|

有点晚了，关于C::B中的wxWidgets项目配置方面的改天再写。。。

.. |codeblock-wx-global-var-set.png| image:: http://www.flord.net/files/113785018509_tn_1.jpg :name: 113785018509.png :target: http://www.flord.net/files/113785018509_1.png
.. |codeblock-wx-create-project.png| image:: http://www.flord.net/files/113785466329_tn_1.jpg :name: 113785466329.png :target: http://www.flord.net/files/113785466329_1.png
