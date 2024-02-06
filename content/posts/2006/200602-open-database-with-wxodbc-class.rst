wxODBC(wxWidgets)中使用驱动程序方式打开数据库
###############################################

:author: Rex Zhang
:date: 2006-02-02T17:25:58+08:00
:modified: 2006-02-02T17:25:58+08:00
:status: published
:category: Coding
:tags: wxWidgets, ODBC

wxWidgets的文档中都是使用在控制面板/数据源中设定DSN来创建ODBC连接。但是实际上很多小型的应用，只是使用本机的一个Access数据库。而要求使用者学习ODBC的DSN配置明显的增加了软件的使用难度。因此，研究了一下wxforum.org中的帖子，试验成功！范例如下：

.. code-block:: cpp

    wxDbConnectInf *DbConnectInf = NULL; // 定义数据库连接信息指针DB connection information
    wxDb *PodDB = NULL;                  // 定义数据库连接指针Database connection
    wxDbTable *table = NULL;             // 定义数据表指针Data table to access

    DbConnectInf = new wxDbConnectInf(0, wxT(""), wxT(""), wxT("")); //这里定义的内容基本没用，但不定义会报错

    PodDB = new wxDb(DbConnectInf->GetHenv());

    bool DBfailOnDataTypeUnsupported = !true;                                                                             //
    if (!DB->Open(wxT("DRIVER=Microsoft Access Driver (*.mdb);DBQ=D:\\pod.mdb;UID=admin;"), DBfailOnDataTypeUnsupported)) //使用驱动程序的方式打开数据库
    {
        if (PodDB->IsOpen())
        {
            // Connection is open, but the initialization of
            // datatypes and parameter settings failed
            return 0;
        }
        else
        {
            // Error opening datasource
            //return HandleError(wxT("DB ENV ERROR: Cannot allocate ODBC env handle"));
            return 0;
        }
    }
    const wxString tableName = wxT("POD"); //定义要操作的表的名称
    const UWORD numTableColumns = 8;       //指出POD表中的列数（columns）
    //建立到表的连接
    table = new wxDbTable(PodDB, tableName, numTableColumns, wxT(""), wxDB_QUERY_ONLY, wxT(""));

    //将存放提取数据的变量清空
    wxStrcpy(pPodPictureInfo->Title, wxT(""));
    ......

        //定义列的数据格式，和取出的格式。
        //此处需要注意的是如果前面指明了numTableColumns为n的话，就一定要定义n条
        table->SetColDefs(0, wxT("Pod_Title"), DB_DATA_TYPE_VARCHAR, pPodPictureInfo->Title, SQL_C_WXCHAR, sizeof(pPodPictureInfo->Title), true, true);
    ......

        //打开表
        if (!table->Open())
    {
        //An error occurred opening (setting up) the table"));
    }

    //限定取出Pod_When列值为1982的行(row)
    table->SetWhereClause(wxT("Pod_When = '1982'"));

    //按照PodDate字段排序
    table->SetOrderByClause(wxT("Pod_Date"));

    //根据上面的限定信息执行查询操作
    if (!table->Query())
    {
        return HandleError(wxT("QUERY ERROR: "), table->GetDb());
        //return 0;
    }

    while (table->GetNext()) //提取查询到的行
    {
        wxString msg; // Used for display messages
        msg.Printf(wxT("Row #% lu --\nTitle : %s\nPodDate : %s\nWhere : %s\nWhen : %s\nWho : %s\nDisc : %s\nRelated : %s\nPhotoName :%s"),
                   table->GetRowNum(),
                   pPodPictureInfo->Title,
                   pPodPictureInfo->PodDate,
                   pPodPictureInfo->Where,
                   pPodPictureInfo->When,
                   pPodPictureInfo->Who,
                   pPodPictureInfo->Disc,
                   pPodPictureInfo->Related,
                   pPodPictureInfo->PhotoName);
        //检查表操作/现实获取的POD信息
        //wxSafeShowMessage(wxT("Pod_wxDbTable Test"),msg);
    }

补充一点
--------

在SetColDefs中关联的变量不能使用wxString，只能使用wxChar[n]等格式。

.. code-block:: cpp

    struct PodPictrueInfo
    {
        wxChar Title[100];
    #......
    }
