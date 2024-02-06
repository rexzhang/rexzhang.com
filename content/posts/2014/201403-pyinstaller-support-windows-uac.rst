使用 PyInstaller 生成便于分发的单一可执行程序，并且添加 Windows UAC 权限支持
######################################################################################################


:author: Rex Zhang
:date: 2014-03-18T01:11:41+08:00
:modified: 2014-03-18T01:11:41+08:00
:status: published
:category: Coding
:tags: Python, UAC


很多时候用 Python 写的小工具需要打包成一个可执行文件交给使用者，比如：

-  使用者没有安装 Python 或者第三方库环境
-  为了便于维护，代码被分割成多个 .py 文件；打包传递的时候相当麻烦

因为这个问题自然也孕育出了多个实现的方案:

-  `py2exe <http://www.py2exe.org/>`__ 是早期很流行的一个打包工具，只能生成 Windows 下的可执行程序，2008年开始停止更新；项目网址:`py2exe@SF.net <http://sourceforge.net/projects/py2exe/>`__
-  `py2app <http://pythonhosted.org/py2app/>`__ 一个生成 Mac OS X 可执行程序的打包工具
-  `cx_Freeze <http://cx-freeze.sourceforge.net/>`__ 支持 Windows、Mac OS X、Linux; 支持 Py2 Py3； 特色是可以生成安装包，没用过；以后可以试试
-  `PyInstaller <http://www.pyinstaller.org/>`__ 今天的主角，跨平台、支持第三方库比较完善，文档丰富；缺点是官方只支持到 Py27

安装很简单，唯一要注意的是其在 Windows 下工作时依赖于 `pywin32 <http://sourceforge.net/projects/pywin32/files/>`__ 这个项目。同时，如果要支持 Windows UAC 权限暂时测试成功的只有添加 ``*.manifest`` 文件这个办法


首次使用是可以用使用命令行工具自动生成一个配置文件，其中 ``launcher2.py`` 是这个工程的入口程序

.. code-block:: shell

    pyinstaller --onefile --noconsole launcher2.py

随后 pyinstaller 会自动生成一个名为 ``launcher2.spec`` 的配置文件

工程目录结构

.. code-block:: text

    root-+-res-+-p1.png
         |     +-p2.png
         +-launcher2.py    #工程入口程序
         +-launcher2.spec  #pyinstaller配置文件
         +-launcher2.exe.manifest #UAC配置文件

手工配置 ``launcher2.spec`` 文件，内容如下

.. code-block:: python

    # -*- mode: python -*-
    a = Analysis(['launcher2.py'],
                 pathex=['.'],
                 hiddenimports=[],
                 hookspath=None,
                 runtime_hooks=None)
    pyz = PYZ(a.pure)
    exe = EXE(pyz,
              a.scripts,
              a.binaries,
              a.zipfiles,
              a.datas,
              name='launcher.exe', #指定可执行程序文件名，可以与工程相关名字不同
              debug=False,
              strip=None,
              upx=True, #对生产的可执行文件压缩，不压缩实在太大
              manifest='launcher2.exe.manifest',
              icon='../../res/icons/client48.ico', #指定可执行程序图标
              console=False )

    coll = COLLECT(
              exe,
              Tree('res', prefix='res'), #指定同时整合的资源性文件夹
              name='release',
              )

添加 launcher2.exe.manifest 文件，内容如下

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <assembly manifestVersion="1.0" xmlns="urn:schemas-microsoft-com:asm.v1">
      <assemblyIdentity name="launcher" processorArchitecture="x86" type="win32" version="1.0.0.0"/>
      <dependency>
        <dependentAssembly>
          <assemblyIdentity name="Microsoft.VC90.CRT" processorArchitecture="x86" publicKeyToken="1fc8b3b9a1e18e3b" type="win32" version="9.0.21022.8"/>
        </dependentAssembly>
      </dependency>
      <dependency>
        <dependentAssembly>
          <assemblyIdentity language="*" name="Microsoft.Windows.Common-Controls" processorArchitecture="x86" publicKeyToken="6595b64144ccf1df" type="win32" version="6.0.0.0"/>
        </dependentAssembly>
      </dependency>

        <!-- Identify the app security requirements. -->
        <trustInfo xmlns="urn:schemas-microsoft-com:asm.v2">
            <security>
                <requestedPrivileges>
                    <requestedExecutionLevel level="requireAdministrator" uiAccess="false"/>
                </requestedPrivileges>
            </security>
        </trustInfo>
    </assembly>

一切配置妥当后可以通过执行如下命令来自动生成可执行程序

.. code-block:: shell

    pyinstaller --noconfirm launcher2.spec

最后，生成的目标文件在 dist\release 目录；目录结构如下

.. code-block:: text

    root-+-res-+-p1.png
         |     +-p2.png
         +-launcher.exe
         +-launcher2.exe.manifest

说说这类打包工具的缺陷

-  当前版本的 pyinstaller UAC 不支持 Python AMD64 版本；只支持 win32 版本
-  体积偏大，在实现非常简单功能的时候体积与功能严重不匹配（好处是：自带工作环境，避免与系统不同版本协同工作时的不兼容性）
-  工作原理类似很多病毒，在运行前会脱壳，将执行代码解出，然后再执行。很多安全软件都会对此行为告警
-  真实的执行文件所在路径与打包的 .exe 文件不在同一个目录，如果程序有依赖相关路径判断可能会导致错误

参考链接

-  http://blogs.msdn.com/b/shawnfa/archive/2006/04/06/568563.aspx
-  http://msdn.microsoft.com/en-us/library/aa375632%28v=VS.85%29.aspx
-  http://en.wikipedia.org/wiki/User_Interface_Privilege_Isolation
-  http://bojan-komazec.blogspot.cz/2011/08/how-to-make-your-application-uac.html
-  http://stackoverflow.com/questions/13964909/setting-uac-to-requireadministrator-using-pyinstaller-onefile-option-and-manifes
