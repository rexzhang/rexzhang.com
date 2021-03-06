Django 使用 Cache 机制提升性能
############################################


:author: Rex Zhang
:date: 2012-04-21T00:19:51+08:00
:modified: 2012-04-21T00:19:51+08:00
:status: published
:category: Coding
:tags: Django


Django 的缓存机制支持多种缓存介质和缓存范围的组合。以 v1.4 版为例；

缓存介质（backends）支持 ：

-  Memcached
-  数据库（支持多库模式）
-  文件系统
-  本地内存

缓存范围 ：

-  全网站范围
-  单个视图
-  URL规则与单个视图的组合

使用缓存机制分两个部分 ：

#. 配置要使用的缓存介质
#. 对需要缓存的范围做配置

配置要使用的缓存介质，以使用数据库为例 ：


在数据库内创建缓存专用表，其中 ``cache_eve_map_online`` 是自定义的表名

.. code-block:: shell

    python eveMapOnline/manage.py createcachetable cache_eve_map_online --settings=eveMapOnline.settingsSgfansOrg

如果使用了自定义的 settings 文件要追加参数，不然可能会出现异常（比如没有正确的数据库接口设置）

修改 ``settings.py`` 文件，添加 ``CACHE`` 配置

.. code-block:: python

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'cache_eve_map_online',
        }
    }

设置缓存作用范围，以全站范围为例：

修改 ``settings.py`` 的中间件设置部分

.. code-block:: python

    MIDDLEWARE_CLASSES = (
        'django.middleware.cache.UpdateCacheMiddleware', #必须在中间件清单的第一条
        'django.middleware.common.CommonMiddleware',
        ...
        'django.middleware.cache.FetchFromCacheMiddleware', #必须在中间件清单的最后一条
    )

需要注意的是添加后启用的中间件之间的顺序

建议的配置方式

值得注意的是：即便只在中间件部分启用了缓存，而未设置 Cache 的具体参数时，缓存机制依然是会自动生效的！解决这个问题的办法是为发布环境专门设计一个配置文件镶嵌调用的方式来处理。发布 settingsRelease.py 内的写法如下：

.. code-block:: python

    from settings import *

    #
    # 缓存机制设置
    #

    # 中间件设置
    MIDDLEWARE_CLASSES = ('django.middleware.cache.UpdateCacheMiddleware',) + MIDDLEWARE_CLASSES  #必须在第一个
    MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('django.middleware.cache.FetchFromCacheMiddleware',) #必须在最后一个

    # 缓存模式支持设置
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'cache_eve_map_online',
        }
    }

.. Tip::

    总的来说, 即便使用的是最简单的设置对显示信息相对固定的网站的性能提升还是非常大的

参考链接：

- https://docs.djangoproject.com/en/1.4/topics/cache/

Update：

- 20120421 增加 settingsRelease.py 范例
