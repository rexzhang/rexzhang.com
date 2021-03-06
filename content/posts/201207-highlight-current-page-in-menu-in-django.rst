使用 Django 的 TEMPLATE_CONTEXT_PROCESSORS 在模板中优雅的高亮当前页面对应的菜单项
######################################################################################################################


:author: Rex Zhang
:date: 2012-07-19T01:33:40+08:00
:modified: 2012-07-19T01:33:40+08:00
:status: published
:category: Coding
:tags: Django, Bootstrap

整体思路是

#. 使用 TEMPLATE_CONTEXT_PROCESSORS 在模板中激活全局上下文
#. 使用 bootstrap 库实现 CSS 效果
#. 在模板文件中调用全局变量完成实现

在 settings.py 中添加相应设置激活全局上下文

.. code-block:: python

    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.core.context_processors.request",#添加此项后才能在模板上访问 request 相关的信息

        #'django.core.context_processors.auth',
        #"django.contrib.auth.context_processors.auth",
        #"django.core.context_processors.debug",
        #"django.core.context_processors.i18n",
        #"django.core.context_processors.media",
        "django.core.context_processors.static",#在全局变量中添加 {{ STATIC_URL }}
        #"django.core.context_processors.tz",
        #"django.contrib.messages.context_processors.messages",
    )


如果遗漏添加 django.core.context_processors.static ，可能会导致 static 目录异常。具体表现是：导致下面添加的 css、js 访问路径不正常

在模板中添加 bootstrap 支持

.. code-block:: html

    <link rel="stylesheet" href="{{ STATIC_URL }}css/bootstrap/bootstrap.min.css" type="text/css" media="all" />

    <script src="{{ STATIC_URL }}js/jquery-1.7.2.min.js" type="text/javascript"></script>
    <script src="{{ STATIC_URL }}js/bootstrap.min.js" type="text/javascript"></script>

在模板文件中（我的范例是 menu.html ）使用全局变量 request.path为当前页面设置高亮

.. code-block:: xml

    {% url eveJumpNavigator:pathLayout as url_pathLayout %}
    {% url eveJumpNavigator:oneJump as url_oneJump %}
    <ul class="nav nav-tabs">
        <li {% if request.path == url_pathLayout %}class="active"{% endif %}><a href="{% url eveJumpNavigator:pathLayout %}" >旗舰跳跃路线规划工具</a></li>
        <li {% if request.path == url_oneJump %}class="active"{% endif %}><a href="{% url eveJumpNavigator:oneJump %}" >旗舰一跳可达星系查询</a></li>
    </ul>

需要注意的一点是：``request.path == url_oneJump`` 中的 ``==`` 两边必须有空格，不然会导致模板解析失败，应该是 Django(1.3.1) 的 Bug
