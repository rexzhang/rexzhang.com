使用 apache2 作为 svn 仓库的访问接口
####################################

:author: Rex Zhang
:date: 2014-06-25T07:34:07+08:00
:modified: 2014-06-25T07:34:07+08:00
:status: published
:category: Linux
:tags: apache, svn

安装 apache 的 svn 支持

.. code-block:: shell

    aptitude install libapache2-svn

svn.apache.conf 配置文件内容

.. code-block:: text

    <Location /svnroot>
      DAV svn
      SVNParentPath /home/rex/svnroot

      # Authentication: Basic
      AuthName "Subversion repository"
      AuthType Basic
      AuthBasicProvider file
      AuthUserFile /home/rex/trac.htpasswd

      # Authorization: Authenticated users only
      Require valid-user

      # Authorization: Path-based access control; authenticated users only
    #  AuthzSVNAccessFile /path/to/access/file
    </Location>

重启 apache 后即可通过 dev.sample.com/svnroot/repos1 访问 svn 仓库
