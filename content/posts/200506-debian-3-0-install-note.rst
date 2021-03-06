Debian 3.0 安装笔记
###################

:author: Rex Zhang
:date: 2005-06-08T23:55:35+08:00
:modified: 2005-06-08T23:55:35+08:00
:status: published
:category: Linux
:tags: Debian

Debian都出3.1r0了,以前一直放在桌面没来得及整理的笔记多数已经没有用了.放在这儿做个纪念好了

.. code-block:: text

    #
    # Replace /etc/apt/sources.list with this file will change apt source to Debian Mirror on CN99
    #
    deb http://debian.cn99.com/debian stable main non-free contrib
    deb http://debian.cn99.com/debian-non-US stable/non-US main contrib non-free
    deb http://debian.cn99.com/debian proposed-updates main contrib non-free
    deb http://debian.cn99.com/debian-non-US proposed-updates/non-US main contrib non-free
    deb http://debian.cn99.com/debian-security woody/updates main contrib non-free
    deb-src http://debian.cn99.com/debian stable main non-free contrib
    deb-src http://debian.cn99.com/debian-non-US stable/non-US main contrib non-free
    deb-src http://debian.cn99.com/debian proposed-updates main contrib non-free
    deb-src http://debian.cn99.com/debian-non-US proposed-updates/non-US main contrib non-free
    ---------------
    ESS
    http://sidlo.penguin.cz/ES2838/index.html
    http://www.linuxfans.org/nuke/modules.php?name=News&file=print&sid=2355

    http://www.pchome.net/dl/drvmodem.htm
    -------------------
    apt-get install ssh mc

    apt-get install samba

    ----Modem
    apt-get install kernel-headers-2.4.18-bf2.4
    apt-get install gcc make


    ln -s /usr/src/kernel-headers-2.4.18-bf2.4/ /lib/modules/2.4.18-bf2.4/build

    ----------------Intel 536EP---------------------
    解压Intel536-460.tgz包至
    make clean
    make 536ep
    make install

    ------------------HCF---0.99------------------
    tar -xzf hcfpcimodem-{version}.tar.gz
    cd hcfpcimodem-{version}
    make install
    hcfpciconfig
        /dev/ttySHCF0 or /dev/cuaHCF0 (call-out device)
    hcfpciconfig --help

    ------------------HCF---1.03full.deb------------------
     dpkg -i hcfpcimodem_1.03full_i386.deb

    ----------------------------------
    检查Modem是否已工作
    apt-get install minicom
    minicom -s
        Serial port setup
            /dev/ttyS3 -> /dev/modem
        save setup as dfl
        Exit
    Ctrl+A ,Q

    minicom

    -----------------------------
    HylaFax

    apt-get install hylafax-server

    /usr/share/doc/hylafax-server/README.debian.gz

    Default allow users: localhost

    hylafax can't use AdaptiveAnswer without these links:
            /etc/hylafax/getty-link -> /sbin/mgetty
            /etc/hylafax/vgetty-link -> /usr/sbin/vgetty
            /etc/hylafax/egetty-link -> /sbin/mgetty

    apt-get install mgetty
    ln -s /sbin/mgetty /etc/hylafax/getty-link
    ln -s /sbin/mgetty /etc/hylafax/egetty-link

    apt-get install mgetty-voice
    ln -s /usr/sbin/vgetty /etc/hylafax/vgetty-link

    ##ln -s /usr/bin/gs /usr/local/bin/

    faxsetup -server

    ~~~~faxsetup~~~
    mkdir /usr/local/lib/ghostscript
    ln -s /usr/share/gs/6.53 /usr/local/lib/ghostscript/6.53
    ln -s /usr/bin/ /usr/local/lib/ghostscript/common

    ~~~~
    faxaddmodem ttySHCF0
    ~~~~
    Next the following lines are added to /var/spool/fax/etc/host:

      localhost
      192.168.1

    All machines from domain 192.168.1.0 are allowed to use the fax!
    !!!!!!!!
    192.168.100.99:21::


    /etc/init.d/hylafax start


    ~~~~gs~~~~~~
     apt-get install gs gs-common gsfonts


    ~~~~
    Hylafax does not launch the daemon faxgetty by default. This has to be done by hand:

    1 - Edit file /etc/inittab and insert the following line at the end of the file:

    mo:2345:respawn:/usr/sbin/faxgetty -D ttyS0

    the command kill -HUP 1 is necessary to restart faxgetty

    Or

    if you want to use the rc.local file:
    2 - Add to /etc/rc.d/rc.local the following line:

    /usr/sbin/faxgetty -D /dev/ttyS0

    and launch the command:

    faxgetty -D /dev/ttyS0

    Note : The command faxaddmodem allows you to add one or more modems afterwards.
    ~~~
    fileserver:/etc# nano inittab
        F0:23:respawn:/usr/sbin/faxgetty ttySHCF0

    fileserver:/etc# nano syslog.conf
        local5.*                -/var/log/hylafax/hylafax.log
    /etc/init.d/sysklogd reload

    init q

    /etc/init.d/hylafax restart

    ps -e #check faxgetty install

    ===============================================
    Samba CUPS

    apt-get install lynx
    apt-get install lynx-ssl

    apt-get install cupsys cupsys-bsd cupsys-client
    apt-get install cupsomatic-ppd foomatic-bin foomatic-db hp-ppd
    apt-get install gs !!!
    apt-get install gs-cjk-resource

    apt-get install samba
    apt-get install swat
        /etc/services
            swat 901/tcp
        /etc/inetd.conf
            swat stream tcp nowait.400 root /usr/sbin/swat swat
    /etc/init.d/inetd restart
    http://localhost:901/

    HP6L
    在CUPS中用Raw格式创建打印机-可直接使用Windows打印程序


    ===========================================
    Webmin
    apt-get install webmin
    apt-get install webmin-ppp pptpd

    SSL 得端口号 443
    ###################################################3
    pptp VPN

    /etc/ppp/pptpd-options

    ## change 'servername' to whatever you specify as your server name in chap-secr$
    ##name servername
    name fileserver
    ## change the domainname to your local domain
    ##domain mydomain.net
    domain domain.com

    ## these are reasonable defaults for WinXXXX clients
    ## for the security related settings
    #auth
    require-chap
    #require-chapms
    #require-chapms-v2

    /etc/ppp/chap-secrets
    # Secrets for authentication using CHAP
    # client        server  secret                  IP addresses
    username  fileserver      password  "*"

    /etc/pptpd.conf
    localip 192.168.100.50
    remoteip 192.168.100.51-60

    ========================================================
    download from linuxsir.org

    METHOD C: TAR PACKAGE (*.tar.gz)

    If you have obtained the driver package in tar format:

    1. extract the package with "tar -xzf hcfpcimodem-{version}.tar.gz"
    ("tar -xzf hcfusbmodem-{version}.tar.gz" for the USB version)

    2. change to the package directory with "cd hcfpcimodem-{version}"
    ("cd hcfusbmodem-{version}" for the USB version)

    3. run "make install" from the top of the package directory.
    (Debian users might need to change the KERNELSRC definition in
    modules/common.mak first)

    4. run "hcfpciconfig" ("hcfusbconfig" for the USB version) to complete
    the installation and configure your modem.

    (Alternatively to this whole procedure you may generate RPMS from the tar
    package using rpm -ta hcf{pci|usb}modem-{version}.tar.gz")

    ============================
    Hard Disk

    cfdisk (menu Fdisk)###分区操作,创建了一个 /dev/hdc1 分区
    mkdir /home/wd15g
    mkfs.ext3 /dev/hdc1 格式化为ext3格式

    mkdir /home/wd15g/documents
    chown ..... /home/wd15g/documents
