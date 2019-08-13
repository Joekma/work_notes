### windows FTP相关

#####登录
```angular2html
C:\>ftp
ftp> open 127.0.0.1 2000
Connected to 127.0.0.1.
220 Microsoft FTP Service
User (127.0.0.1:(none)): xxx
331 Password required for xxx.
Password:
230 User xxx logged in.
ftp>
```
#####上传

```angular2html
ftp> put D:\index.html （回车）
当屏幕提示你已经传输完毕，可以键入相关命令查看：
ftp> dir （回车）
```
#####下载

```angular2html

假设要把服务器\images目录中的所有.jpg文件下载至本机中，可以输入指令：
ftp> cd images（回车） [注：进入\images目录]
ftp> mget *.jpg
windows下ftp上传与下载工作完毕，键入bye中断连接。
ftp> bye（回车）
```
#####常用命令
```angular2html
1. open：与服务器相连接；
2. send(put)：上传文件；
3. get：下载文件；
4. mget：下载多个文件；
```


###linux FTP相关

##### 开启FTP服务
```angular2html
1. 首先服务器要安装ftp软件,查看是否已经安装ftp软件下：
#which vsftpd
如果看到有vsftpd的目录说明服务器已经安装了ftp软件

2. 查看ftp 服务器状态
#service vsftpd status

3. 启动ftp服务器
#service vsftpd start

4. 重启ftp服务器
#service vsftpd restart

5. 查看服务有没有启动
#netstat -an | grep 21
tcp 0 0 0.0.0.0:21 0.0.0.0:* LISTEN
如果看到以上信息，证明ftp服务已经开启。

6.如果需要开启root用户的ftp权限要修改以下两个文件
#vi /etc/vsftpd.ftpusers中注释掉root
#vi /etc/vsftpd.user_list中也注释掉root
然后重新启动ftp服务。

7. vsftpd 500 OOPS: cannot change directory
登陆报错:
C:\>ftp 192.168.0.101
Connected to 192.168.0.101.
220 (vsFTPd 2.0.5)
User (192.168.0.101:(none)): frank
331 Please specify the password.
Password:
500 OOPS: cannot change directory:/home/frank
Login failed.
ftp> ls
500 OOPS: child died
Connection closed by remote host.
解决方法:
setsebool ftpd_disable_trans 1
service vsftpd restart
就OK了！

这是SELinux的设置命令,在不熟悉SELnux前，把SELinux关掉也可以的。

8. 永久开启，即os重启后自动开启ftp服务
方法一：
cd /etc/xinetd.d ，编辑ftp服务的配置文件gssftp的设置：
vi /etc/xinetd.d/gssftp ，将 修改两项内容：

(a) server_args = -l –a 去掉-a 改为server_args = -l
(b) disable=yes改为disable=no
(c) 保存退出。

方法二：
(a) system-config-services , 进入图形界面的System services查看是否有 vsftpd项,如果没有转到2.,保存后退出

　 (b) 用redhat第三张盘 安装此服务（开始--删除/增加程序），200K左右

　 (c) #setup
　　 此时能看到vsftpd项，此时选中此services项,保存后退出.


```

#####以二进制形式传输
```
如果传输非文本，先输入bianry，然后再get就可以了
比如
ftp> get 5-4.tif 
227 Entering Passive Mode (192，168，0，118，83，73) 

150 Opening BINARY mode data connection for 5-4.tif (68334 bytes). 
WARNING! 397 bare linefeeds received in ASCII mode File may not have transferred correctly. 226 File send OK. 
68334 bytes received in 0.024 seconds (2.8e+03 Kbytes/s)

ftp> binary # 以二进制模式进行传输 
ftp> get 5-4.tif 
200 Switching to Binary mode.

ftp> bye 
```

#####常用命令
```angular2html

1.连接ftp服务器 
格式：ftp [hostname| ip-address] 
　　a)在linux命令行下输入：ftp 10.18.34.115 
　　b)服务器询问你用户名和口令，分别输入yint和相应密码，待认证通过即可。 
2. 下载文件     下载文件通常用get和mget这两条命令。 
　　a) get 
　　格式：get [remote-file] [local-file] 
　　将文件从远端主机中传送至本地主机中. 
　　如要获取服务器上E:\rose\1.bmp,则 
　　ftp> get /rose/1.bmp 1.bmp (回车) 
　　b) mget　　　　　　 
　　格式：mget [remote-files] 
　　从远端主机接收一批文件至本地主机. 
　　如要获取服务器上E:\rose\下的所有文件,则 
　　ftp> cd /rose 
　　ftp> mget *.* (回车) 
　　注意：文件都下载到了linux主机的当前目录下。比如，在　/root/yint下运行的ftp命令，则文件都下载到了/root/yint下。 
3.上传文件 
　　a) put 
　　格式：put local-file [remote-file] 
　　将本地一个文件传送至远端主机中. 
　　如要把本地的1.bmp传送到远端主机E:\rose,并改名为333.bmp 
　　ftp> put 1.bmp /rose/333.bmp (回车) 
　　b) mput 
　　格式：mput local-files 
　　将本地主机中一批文件传送至远端主机. 
　　如要把本地当前目录下所有bmp文件上传到服务器E:\rose 下 
　　ftp> cd /rose （回车） 
　　ftp> mput *.bmp　（回车） 
　　注意：上传文件都来自于主机的当前目录下。比如，在　/root/yint下运行的ftp命令，则只有在/root/yint下的文件linux才会上传到服务器E:\rose 下。 
4. 断开连接 
　　bye：中断与服务器的连接。 
　　ftp> bye (回车)

```

###Mac FTP相关

#####常用命令
```angular2html
登录
# 方式一
$ ftp server-ip

# 方式二
$ ftp
ftp> open server-ip

此时已经进入ftp命令行环境，此时如果进行本地目录或文件操作命令将发生一些变化，如下：

服务器操作                         本地目录操作
cd 目录名（进入服务器目录）          lcd 目录名（进入本机目录）
cd \（退到服务器根目录）             lcd \（退到本机根目录）
cd ..（退回到上一级目录）            lcd ..（退回到上一级目录）
pwd                               !pwd
ls                                !ls

上传文件

# server-filename 必须显式指明，否则报错：文件名无效
ftp> put /local/path/filename /remote/path/server-filename

注意：向ftp服务器上传文件有两种模式   字符模式（ASCII）和二进制模式（Binary）。默认是ASCII模式。一般上传非文本文件要用二进制模式。
登录ftp后，上传文件前，在ftp>状态下输入bin即可(切换为二进制模式)。
在ftp>状态下输入asc(切换为ASCII模式)

批量上传
使用通匹符批量上传文件至服务器，需要注意的一点，mput 不支持绝对路径，应该先进入要上传的本地文件夹及远程文件夹才可以操作。

ftp> cd /remote/path
ftp> lcd /local/path
ftp> mput file*
local: file.jar remote: file.jar
229 Entering Extended Passive Mode (|||62331|)

150 Opening data channel for file upload to server of "/local/path/file.jar"
100% |*|   519        1.80 MiB/s    --:-- ETA

226 Successfully transferred "/local/path/file.jar"
519 bytes sent in 00:00 (19.54 KiB/s)

注意：ftp不支持文件夹上传

文件下载
下载服务器中的文件至本地目录中，可选指定下载至本地目录后的文件名称，依然要求提前进入待下载文件的目录中。

ftp> get remote-filename local-filename

local-filename可省略，默认本地当前路径。
注意：关于下载文件夹， FTP 命令不支持文件夹下载操作。

删除文件
ftp> delete /remote/path/filename
在服务器中删除文件，可以指定绝对路径，相对其他命令显得比较灵活。
```





