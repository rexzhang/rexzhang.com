VMware vSphere Hypervisor ESXi 5.5 支持 realtek 网卡
################################################################################################


:author: Rex Zhang
:date: 2014-02-20T00:15:59+08:00
:modified: 2014-02-20T00:15:59+08:00
:status: published
:category: 运维
:tags: VMware


ESXi 5.1 以及以前是内置支持 realtek 网卡的，不知为何到了 5.5 就不内建支持了。不过也好，正好学习了下如何生成自定义 ESXi 光盘镜像的制作

1.要安装 `vSphere PowerCLI <https://developercenter.vmware.com/web/dp/sdk/55/vsphere-powercli>`__

2.运行 vSphere PowerCLI

3.解除安全限制

.. code-block:: shell

    PS C:\>Set-ExecutionPolicy -Scope CurrentUser Unrestricted

4.创建 PowerShell 脚本 bulid-customized-iso.ps1

.. code-block:: text

    # Add VMware Online depot
    Add-EsxSoftwareDepot https://hostupdate.vmware.com/software/VUM/PRODUCTION/main/vmw-depot-index.xml
 
    # Clone the ESXi 5.5 GA profile into a custom profile
    $CloneIP = Get-EsxImageProfile ESXi-5.5.0-1331820-standard
    $MyProfile = New-EsxImageProfile -CloneProfile $CloneIP -Vendor $CloneIP.Vendor -Name (($CloneIP.Name) + "-customized") -Description $CloneIP.Description
 
    # Add latest versions of missing driver packages to the custom profile
    Add-EsxSoftwarePackage -SoftwarePackage net-r8168 -ImageProfile $MyProfile
    Add-EsxSoftwarePackage -SoftwarePackage net-r8169 -ImageProfile $MyProfile
    Add-EsxSoftwarePackage -SoftwarePackage net-sky2 -ImageProfile $MyProfile

    # Export the custom profile into ISO file
    Export-EsxImageProfile -ImageProfile $MyProfile -ExportToISO -FilePath c:\temp\ESXi-5.5.0-1331820-standard-customized-realtek.iso

5.继续在 vSphere PowerCLI 中执行脚本

.. code-block:: shell

    PS C:\>./bulid-customized-iso.ps1

因为需要在线下载源光盘镜像，所以耗时比较长

6.待生成 .ISO 文件成功后用新的 .ISO 文件刻盘重新安装 ESXi 即可

参考链接

-  `Installing and upgrading to ESXi 5.5 – Best practices and tips <http://www.vladan.fr/installing-upgrading-esxi-5-5-best-practices-tips/>`__
-  `Realtek 8169 NIC in ESXi 5.5 not detected by default – install a VIB <http://www.vladan.fr/realtek-8169-nics-not-detected-under-esxi-5-5/>`__
-  `Enable Realtek NIC on VMware ESXi 5.5 <http://nolabnoparty.com/en/enable-realtek-nic-vmware-esxi/>`__
