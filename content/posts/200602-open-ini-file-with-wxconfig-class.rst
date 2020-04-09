wxWidgets wxConfig类
#########################

:author: Rex Zhang
:date: 2006-02-02T19:38:33+08:00
:modified: 2006-02-02T19:38:33+08:00
:status: published
:category: Coding
:tags: wxWidgets

wxWidgets提供一个存取配置信息的完整类。可以将配置存放到注册表（windows平台）、类似于windows .INI格式的配置文件（跨平台）等。可惜的是现在还不支持使用.XML存储格式。不过也够用了。

生成的.INI文件格式如下：

.. code-block:: text

    PodBasePath=D:\\Tools\\
    nodpodPodYear=2005[/text]

代码如下：

.. code-block:: cpp

    struct ngpodwcConfig
    {
        wxString PodBasePath;
        ......

            int PodYear;
        ......
    } ；

        //打开配置文件
        wxFileInputStream ConfigInStream(wxT("ngpodwc.ini"));
    if (!ConfigInStream.Ok()) //检查配置文件是否存在
    {
        wxString msgTitle("配置文件不存在！", *wxConvCurrent);
        return 1;
    }

    // 建立到配置文件的连接，同时指定转换为UTF8格式
    wxFileConfig *pFileConfig = new wxFileConfig(ConfigInStream, wxConvUTF8);

    ngpodwcConfig config;

    // 读取配置文件->内存

    //读取文本配置信息
    config.PodBasePath = pFileConfig->Read(wxT("PodBasePath"));

    //读取数值配置信息，这里需要注意是传变量的地址
    pFileConfig->Read(wxT("PodYear"), &(config.PodYear));

    //给数值配置信息赋值

    fileConfig->Write(wxT("PodYear"), 2004);

    //给文本配置信息赋值

    fileConfig->Write(wxT("DatabasePath"), wxT("d:\\"));

    // 打开需要保存的配置文件

    wxFileOutputStream ConfigOutStream(wxT("ngpodwc-out.ini"));

    //将配置信息写入文件

    fileConfig->Save(ConfigOutStream, wxConvUTF8);
