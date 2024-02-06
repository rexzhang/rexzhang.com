搞定"文章分类"区块,感谢GUNlife的帮助
####################################

:author: Rex Zhang
:date: 2005-08-08T21:47:58+08:00
:modified: 2005-08-08T21:47:58+08:00
:status: published
:category: 运维
:tags: Drupal

搞定"文章分类"区块,感谢\ `GNUlife <http://www.gnulife.cn/>`__\ 的帮助.代码如下:

.. code-block:: php

    if (user_access('access content')) {
        $result = db_query("SELECT d.tid, d.name, MAX(n.created) AS updated,COUNT(*) AS count FROM {term_data} d INNER JOIN {term_node} USING (tid) INNER JOIN {node} n USING (nid) WHERE n.status = 1 GROUP BY d.tid,d.name ORDER BY updated DESC, d.name");
        //读取分类关键词，最新文章创建的时间，降序排列
        $items = array();
        while ($category = db_fetch_object($result)) {
            $items[] = l($category->name .' ('. $category->count .')','taxonomy/term/'. $category->tid);
            //按照以前的格式显示分类区块，包括最后一片帖子的发布时间。
            //.'
            '. t('%time ago', array('%time' => format_interval(time() - $category->updated))));
        }
        return theme('item_list', $items);
    }

下一步就是整理分类了...这是个头痛的问题
