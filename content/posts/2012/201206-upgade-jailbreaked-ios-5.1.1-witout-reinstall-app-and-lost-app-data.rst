iOS 5.1.1 不重装程序、不丢失设置及数据的升级越狱办法
##############################################################


:author: Rex Zhang
:date: 2012-06-08T06:25:27+08:00
:modified: 2012-06-08T06:25:27+08:00
:status: published
:category: 数字生存
:tags: iOS, jailbreak


一般来说越狱一个 iOS 设备的标准做法：将设备恢复到出厂状态，然后越狱，最后重新安装自己需要的软件。但这样做的最大困境是：每次 iOS 升级并再次重新越狱后，无数的软件需要重装，所有软件都需要再度手工设置一遍，本地游戏进度直接丢失

恩。。。废话了这么多，反正现在找到办法了（虽然过程是血泪的，但是结果是美好的）。简单的说就是：利用iTunes 的恢复备份功能、并在恢复备份的中途插入越狱这么一个操作

另，iPad2(WCDMA) 和 iPhone4(GSM) 均已成功 我的大致流程如下

#. 将设备升级到最新可越狱的 iOS 版本，这里的范例是 5.1.1
#. 使用 iTunes 同步并在电脑上做备份
#. 使用恢复到指定 iOS 版本的方法恢复设备
#. 在完成 iOS 系统恢复后，设备设置数据恢复前；中断恢复
#. 使用越狱软件越狱，这里的范例是 absinthe-win-2.0.2
#. 越狱完成后，继续使用 iTunes 恢复设备备份的数据
#. 等待 iTunes 将需要恢复的程序同步回设备

这里需要先说明一下 iTunes 恢复 iOS 设备的大致步骤（有大量删减）

#. 确认 iOS 固件文件后，到 Apple
   的授权服务器授权（小雨伞干的就是在本地模拟和替代这个授权服务器的事情）
#. 将 iOS 设备设置到恢复模式状态，并且将 iOS 固件扔给设备
#. iOS 设备接收固件，并自引导进行系统覆盖
#. iOS 设备刷新完固件后将自己设置为出厂状态（待激活）
#. iTunes 将 iOS 备份中的设置信息同步到 iOS 设备
#. iTunes 将 iOS 设备为激活状态
#. iTunes 将 iOS 备份信息中存在的程序同步到 iOS 设备
#. 完成

范例的环境：

-  Windows7 64位
-  iTunes 10.6.1.7
-  absinthe-win-2.0.2
-  iPad2(WCDMA) 32G

详细步骤如下：

首先，将 iPad 连接到 PC 上，打开 iTunes。 然后，将 iOS 升级到 5.1.1（升级到指定版本可以按住键盘『SHIFT』的同时点『更新』按钮）

|jbWithLosslessData-1|

选择正确的固件文件进行升级操作

|jbWithLosslessData-2|

整个升级过程不用人工干预，等待其更新了固件并且完成了数据恢复后。使用 iTunes 的同步功能做一个最新的同步备份

|jbWithLosslessData-3|

备份完成后即可进入我们的主题：不丢失数据的越狱 将 iPad 恢复到刚刚做的 5.1.1 的备份（恢复到指定版本可以：按住键盘『SHIFT』按键的同时点『恢复』按钮）

|jbWithLosslessData-4|

直到出现如下画面

|jbWithLosslessData-5|

iPad屏幕上的画面如下（『未激活』状态）

|jbWithLosslessData-5-2|

关闭 iTunes，打开越狱软件 absinthe-win-2.0.2；重新插拔一下 iPad 到 PC 的连线。开始越狱

|jbWithLosslessData-6|

越狱的过程中，你将看到 iPad 上会出现如下画面（这说明其实越狱也就是一次特别的恢复操作）

|jbWithLosslessData-6-2|

越狱成功后可以看到

|jbWithLosslessData-7|

同时 iPad 的画面依然会停留在『未激活』状态 这个时候关闭越狱软件，拔下 iPad,再度打开 iTunes ，插上 iPad 。继续之前 iTunes 未完的事业（从备份中恢复）

|jbWithLosslessData-5|

这个时候恢复的是设置相关的数据。大概要花费几分钟时间。 完成后 iPad 重新回到已激活状态；并且 iTunes 会进入恢复程序的状态

|jbWithLosslessData-8|

iPad 的画面如下（Cydia 已经安装，其他苹果软件商店的程序会一个一个的同步回来）

|jbWithLosslessData-8-2|

我16G左右的数据量大概花了一个小时多一点点的时间完成程序同步过程

最后！！！请在所有恢复操作完成后，再进入 Cydia 完成 Cydia的初始化操作！！！

祝顺利，完

.. |jbWithLosslessData-1| image:: http://farm8.staticflickr.com/7222/7163121899_4da7a2a82e.jpg
   :width: 500px
   :height: 188px
   :target: http://www.flickr.com/photos/rexzhang/7163121899/
.. |jbWithLosslessData-2| image:: http://farm9.staticflickr.com/8145/7348344270_20d1f95de8.jpg
   :width: 500px
   :height: 384px
   :target: http://www.flickr.com/photos/rexzhang/7348344270/
.. |jbWithLosslessData-3| image:: http://farm8.staticflickr.com/7074/7163133751_28aeed8cef.jpg
   :width: 500px
   :height: 457px
   :target: http://www.flickr.com/photos/rexzhang/7163133751/
.. |jbWithLosslessData-4| image:: http://farm9.staticflickr.com/8142/7348343808_178dc07876.jpg
   :width: 500px
   :height: 306px
   :target: http://www.flickr.com/photos/rexzhang/7348343808/
.. |jbWithLosslessData-5| image:: http://farm8.staticflickr.com/7100/7348343708_e6561c3235.jpg
   :width: 500px
   :height: 209px
   :target: http://www.flickr.com/photos/rexzhang/7348343708/
.. |jbWithLosslessData-5-2| image:: http://farm8.staticflickr.com/7226/7348380278_244e41c0a9.jpg
   :width: 374px
   :height: 500px
   :target: http://www.flickr.com/photos/rexzhang/7348380278/
.. |jbWithLosslessData-6| image:: http://farm8.staticflickr.com/7071/7163167587_7d4d20f824.jpg
   :width: 480px
   :height: 350px
   :target: http://www.flickr.com/photos/rexzhang/7163167587/
.. |jbWithLosslessData-6-2| image:: http://farm8.staticflickr.com/7079/7348377922_7f4dc27a91.jpg
   :width: 374px
   :height: 500px
   :target: http://www.flickr.com/photos/rexzhang/7348377922/
.. |jbWithLosslessData-7| image:: http://farm8.staticflickr.com/7074/7348375888_71fd2a0120.jpg
   :width: 480px
   :height: 350px
   :target: http://www.flickr.com/photos/rexzhang/7348375888/
.. |jbWithLosslessData-8| image:: http://farm8.staticflickr.com/7105/7348375718_8abdd0ac90.jpg
   :width: 500px
   :height: 305px
   :target: http://www.flickr.com/photos/rexzhang/7348375718/
.. |jbWithLosslessData-8-2| image:: http://farm8.staticflickr.com/7089/7348375550_2a69f729da.jpg
   :width: 374px
   :height: 500px
   :target: http://www.flickr.com/photos/rexzhang/7348375550/
