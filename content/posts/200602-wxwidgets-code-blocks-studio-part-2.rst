wxWidgets & Code::Blocks Studio续
#######################################

:author: Rex Zhang
:date: 2006-02-01T22:33:42+08:00
:modified: 2006-02-01T22:33:42+08:00
:status: published
:category: Coding
:tags: wxWidgets, IDE

wxWidgets & Code::Blocks Studio续；在Code::Blocks
Studio中给wxWidgets项目打开Debug。

接\ `上篇 </node/109>`__\ 。

在创建了一个Using UNICODE wxWidgets DLL项目后；C::B默认创建的项目只有一个名为default(相当于release)的tagets，无法使用debug跟踪程序。

要使用Debug需要在编译设置中同时加上GCC和wxWidgets的Debug信息。设置地点都在"程序菜单"->"project"->"Bulid"->"Options"

#. "Compiler"中勾选上"Produce debugging symbols"
#. "Compiler"->"#defined"中添加"__WXDEBUG__"
#. "Linker"中将Link libraries中原有的"wxmsw26u"替换成"wxmsw26ud"
#. "Directories"中将"$(#WX.lib)\gcc_dll$(WX_CFG)\mswud"替换成"$(#WX.lib)\gcc_dll$(WX_CFG)\mswud"

以上配置适合C::B v1.0(Nightly builds) + C::B整合的MingW + wxWidgets
v2.6.2环境
