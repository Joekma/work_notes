mac本身安装了ssh服务，默认情况下不会开机自启

1.启动sshd服务：
sudo launchctl load -w /System/Library/LaunchDaemons/ssh.plist

2.停止sshd服务：
sudo launchctl unload -w /System/Library/LaunchDaemons/ssh.plist

3查看是否启动：
sudo launchctl list | grep ssh

如果看到下面的输出表示成功启动了：
－－－－－－－－－－－－－－
- 0 com.openssh.sshd


但是如果新的虚拟机设置了桥接方式，没有把/etc/systconfig/network-script/ent-
                                   里面最后一个参数要设置成yes，才可以自动获取到ip



windows centos  ssh服务

在虚拟机（Vmware Workstation）下，安装了CentOS7，现在想通过SSH工具连接虚拟机中的CentOS7

1、 首先，要确保CentOS7安装了  openssh-server，在终端中输入  yum list installed | grep openssh-server
此处显示已经安装了  openssh-server，如果又没任何输出显示表示没有安装  openssh-server，通过输入  yum install openssh-server
来进行安装openssh-server

2、 找到了  /etc/ssh/  目录下的sshd服务配置文件 sshd_config，用Vim编辑器打开
将文件中，关于监听端口、监听地址前的 # 号去除
然后开启允许远程登录
最后，开启使用用户名密码来作为连接验证
保存文件，退出

3、开启 sshd服务，输入 sudo service sshd start
检查  sshd  服务是否已经开启，输入ps -e | grep sshd
或者输入netstat -an | grep 22  检查  22号端口是否开启监听

https://blog.csdn.net/trackle400/article/details/52755571

'''
从Linux服务器下载文件夹到本地
1、使用scp命令
scp /home/work/source.txt work@192.168.0.10:/home/work/   #把本地的source.txt文件拷贝到192.168.0.10机器上的/home/work目录下
scp work@192.168.0.10:/home/work/source.txt /home/work/   #把192.168.0.10机器上的source.txt文件拷贝到本地的/home/work目录下
scp work@192.168.0.10:/home/work/source.txt work@192.168.0.11:/home/work/   #把192.168.0.10机器上的source.txt文件拷贝到192.168.0.11机器的/home/work目录下
scp -r /home/work/sourcedir work@192.168.0.10:/home/work/   #拷贝文件夹，加-r参数

2、使用xshell工具
使用xshell来操作服务非常方便，传文件也比较方便。
就是使用rz，sz
首先，服务器要安装了rz，sz
yum install lrzsz
当然你的本地windows主机也通过ssh连接了linux服务器
运行rz，会将windows的文件传到linux服务器
运行sz filename，会将文件下载到windows本地

3、常用方法
在本地上安装Xshell和Xftp软件，在xshell软件中有快捷方式（选择利用Xftp打开当前目录）
'''


windows 打开 ssh服务

