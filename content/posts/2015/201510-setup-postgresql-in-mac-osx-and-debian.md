title: Mac/Debian 环境配置 PostgreSQL/PostGIS/GeoDjango
author: Rex Zhang
date: 2015-10-23T08:49:54+08:00
modified: 2015-10-23T08:49:54+08:00
status: published
category: 运维
tags: PostgreSQL

## PostgreSQL Debian 安装

postgres 有官方提供的源 <https://www.postgresql.org/download/linux/debian/>。以 Debian 7 为例，在 /etc/apt/source.list 文件中添加

```text
deb http://apt.postgresql.org/pub/repos/apt/ wheezy-pgdg main
```

安装

```bash
aptitude install postgresql

aptitude install python-dev
aptitude install libpq-dev
```

修改配置允许非 localhost 访问
postgresql.conf

```text
listen_addresses = 'localhost, 10.10.167.94'
```

pg_hba.conf

```text
host     all     postgres     10.10.0.1/16     md5
```

## PostgreSQL Mac 安装

推荐使用 HomeBrew 和 postgresapp(整合了 PostGIS)

可以由 postgresapp 替代的部分

```shell
brew install postgresql
brew install postgis
```

或者直接安装 postgresapp

```shell
brew cask install postgres
```

PostGIS Debian 安装

```shell
aptitude install postgis
aptitude install binutils libproj-dev gdal-bin
```

PostGIS Mac 安装

```shell
brew install gdal
brew install libgeoip
```

验证 PostGIS 安装，执行

```sql
select * from pg_available_extensions where name like 'postgis%';
```

将看到三条返回，包含名称、版本、描述

```text
postgis
postgis_tiger_geocoder
postgis_topology
```

创建 postgres 用户

切换到 postgres 用户

```text
root@rex-jp1:~# su postgres
```

然后创建一个新用户

```text
postgres@rex-jp1:~$ createuser --interactive
```

修改/添加用户密码

修改当前用户的密码的方法很简单，只需要 su 到对应账号下，然后执行 psql，然后使用如下命令即可

```text
\password
```

或者在 postgres 用户下的 psql 内

```text
postgres-# \password username
```

创建账号同时设置密码，详见 <a>http://www.postgresql.org/docs/current/static/sql-createrole.html</a>

```sql
CREATE ROLE username WITH LOGIN CREATEDB PASSWORD 'password';
```

安装 psycopg2
Mac 下需要添加设置到 ~/.bash_porfile 以解决本地编译时无法找到相关头文件问题

```shell
export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/lastest/bin
```

因为 pip 本地缓存的原因，如果升级 PostgreSQL 可能因为 包内 lib/python2.7/site-packages/psycopg2/_psycopg.so 文件没有更新导致的 import 错误，可以通过强制不使用本地缓冲的方式重新生成

```shell
pip uninstall psycopg2
pip install -U psycopg2 --no-cache-dir
```

未完待续。。。
