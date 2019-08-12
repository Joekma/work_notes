# coding:utf-8

'''
例一：列出/home/peidachang文件夹下的所有文件和目录的详细资料
命令：ls -l -R /home/peidachang

例二：列出当前目录中所有以“t”开头的目录的详细内容，可以使用如下命令：
命令：ls -l t*

例三：只列出文件下的子目录
命令：ls -F /opt/soft |grep /$
列出 /opt/soft 文件下面的子目录

例四：列出目前工作目录下所有名称是s 开头的档案，愈新的排愈后面，可以使用如下命令：
命令：ls -ltr s*

例五：列出目前工作目录下所有档案及目录;目录于名称后加"/", 可执行档于名称后加"*"
命令：ls -AF

例六：计算当前目录下的文件数和目录数
命令：
ls -l * |grep "^-"|wc -l ---文件个数
ls -l * |grep "^d"|wc -l    ---目录个数

例七: 在ls中列出文件的绝对路径
命令：ls | sed "s:^:`pwd`/:"

例九：列出当前目录下的所有文件（包括隐藏文件）的绝对路径， 对目录不做递归
命令：find $PWD -maxdepth 1 | xargs ls -ld

例十：递归列出当前目录下的所有文件（包括隐藏文件）的绝对路径
命令： find $PWD | xargs ls -ld


例十一：指定文件时间输出格式
命令：

ls -tl --time-style=full-iso
ls -ctl --time-style=long-iso

1. 显示彩色目录列表
    打开/etc/bashrc, 加入如下一行:

    alias ls="ls --color"

    下次启动bash时就可以像在Slackware里那样显示彩色的目录列表了, 其中颜色的含义如下:

    1. 蓝色-->目录

    2. 绿色-->可执行文件

    3. 红色-->压缩文件

    4. 浅蓝色-->链接文件

    5. 灰色-->其他文件

返回进入此目录之前所在的目录     cd -
把上个命令的参数作为cd的参数使用



实例三：目录连接链接时，pwd -P  显示出实际路径，而非使用连接（link）路径；pwd显示的是连接路径
命令：pwd -P


实例2：递归创建多个目录
命令：
mkdir -p test2/test22


实例3：创建权限为777的目录
命令：
mkdir -m 777 test3


实例五：一个命令创建项目的目录结构
参考：http://www.ibm.com/developerworks/cn/aix/library/au-badunixhabits.html
命令：
mkdir -vp scf/{lib/,bin/,doc/{info,product},logs/{info,product},service/deploy/{info,product}}


iterm相关

⌘ + d: 垂直分屏，
⌘ + shift + d: 水平分屏。
⌘ + ]和⌘ + [在最近使用的分屏直接切换.
⌘ + opt + 方向键切换到指定位置的分屏。
⌘ + 数字: 切换标签页。
⌘ + 方向键 按方向切换标签页。
shift + ⌘ + s: 保存当前窗口快照。
⌘ + opt + b: 快照回放。很有意思的功能，你可以对你的操作根据时间轴进行回放。可以拖动下方的时间轴，也可以按左右方向键


rm 自定义回收站功能

#但想直接在命令行定义一个函数的话，可以执行如下操作： $ function b() { a=2; }     注意：这里的 { } 前后需要有空格

myrm(){ D=/tmp/$(date +%Y%m%d%H%M%S); mkdir -p $D; mv "$@" $D && echo "moved to $D ok"; }

实例
[root@localhost test]# myrm(){ D=/tmp/$(date +%Y%m%d%H%M%S); mkdir -p $D; 	mv "$@" $D && echo "moved to $D ok"; }

[root@localhost test]# alias rm='myrm'

[root@localhost test]# touch 1.log 2.log 3.log

[root@localhost test]# ll

总计 16

-rw-r--r-- 1 root root    0 10-26 15:08 1.log

-rw-r--r-- 1 root root    0 10-26 15:08 2.log

-rw-r--r-- 1 root root    0 10-26 15:08 3.log

drwxr-xr-x 7 root root 4096 10-25 18:07 scf

drwxrwxrwx 2 root root 4096 10-25 17:46 test3

drwxr-xr-x 2 root root 4096 10-25 17:56 test4

drwxr-xr-x 3 root root 4096 10-25 17:56 test5

[root@localhost test]# rm [123].log

moved to /tmp/20121026150901 ok

[root@localhost test]# ll

总计 16drwxr-xr-x 7 root root 4096 10-25 18:07 scf

drwxrwxrwx 2 root root 4096 10-25 17:46 test3

drwxr-xr-x 2 root root 4096 10-25 17:56 test4

drwxr-xr-x 3 root root 4096 10-25 17:56 test5

[root@localhost test]# ls /tmp/20121026150901/

1.log  2.log  3.log


rmdir命令。rmdir是常用的命令，该命令的功能是删除空目录，一个目录被删除之前必须是空的。
注意，rm - r dir命令可代替rmdir，但是有很大危险性。删除某目录时也必须具有对父目录的写权限。

mv命令是move的缩写，可以用来移动文件或者将文件改名（move (rename) files）

-b ：若需覆盖文件，则覆盖前先行备份。

-f ：force 强制的意思，如果目标文件已经存在，不会询问而直接覆盖；

-i ：若目标文件 (destination) 已经存在时，就会询问是否覆盖！

-u ：若目标文件已经存在，且 source 比较新，才会更新(update)

-t  ： --target-directory=DIRECTORY move all SOURCE arguments into DIRECTORY，即指定mv的目标目录，该选项
适用于移动多个源文件到一个目录的情况，此时目标目录在前，源文件在后。

移动当前文件夹下的所有文件到上一级目录

命令：
mv * ../


文件被覆盖前做简单备份，前面加参数-b

命令：

mv log1.txt -b log2.txt

输出：

[root@localhost test5]# ll

-rw-r--r-- 1 root root   25 10-28 07:02 log1.txt

-rw-r--r-- 1 root root   13 10-28 06:16 log2.txt

-rw-r--r-- 1 root root   29 10-28 06:05 test1.txt

drwxr-xr-x 2 root root 4096 10-25 17:56 test5-1

[root@localhost test5]# mv log1.txt -b log2.txt

mv：是否覆盖“log2.txt”? y

[root@localhost test5]# ll

-rw-r--r-- 1 root root   25 10-28 07:02 log2.txt

-rw-r--r-- 1 root root   13 10-28 06:16 log2.txt~

-rw-r--r-- 1 root root   29 10-28 06:05 test1.txt

drwxr-xr-x 2 root root 4096 10-25 17:56 test5-1

[root@localhost test5]#

说明：

-b 不接受参数，mv会去读取环境变量VERSION_CONTROL来作为备份策略。
--backup该选项指定如果目标文件存在时的动作，共有四种备份策略：

1.CONTROL=none或off : 不备份。
2.CONTROL=numbered或t：数字编号的备份
3.CONTROL=existing或nil：如果存在以数字编号的备份，则继续编号备份m+1...n：
执行mv操作前已存在以数字编号的文件log2.txt.~1~，那么再次执行将产生log2.txt~2~，以次类推。如果之前没有以数字编号的文件，则使用下面讲到的简单备份。
4.CONTROL=simple或never：使用简单备份：在被覆盖前进行了简单备份，简单备份只能有一份，再次被覆盖时，简单备份也会被覆盖。



nl命令在linux系统中用来计算文件中行号。nl 可以将输出的文件内容自动的加上行号！其默认的结果与 cat -n 有点不太一样，
 nl 可以将行号做比较多的显示设计，包括位数与是否自动补齐 0 等等的功能。


# more

显示文件中从第3行起的内容
命令：more +3 log2012.log


从文件中查找第一个出现"day3"字符串的行，并从该处前两行开始显示输出
命令：more +/day3 log2012.log


设定每屏显示行数
命令：more -5 log2012.log


列一个目录下的文件，由于内容太多，我们应该学会用more来分页显示。这得和管道 | 结合起来
命令：ls -l  | more -5


less 工具也是对文件或其它输出进行分页显示的工具，应该说是linux正统查看文件内容的工具，功能极其强大。
less 的用法比起 more 更加的有弹性。在 more 的时候，我们并没有办法向前面翻， 只能往后面看，但若使用了 less 时，
就可以使用 [pageup] [pagedown] 等按键的功能来往前往后翻看文件，更容易用来查看一个文件的内容！除此之外，在 less 里头可以拥有更多的搜索功能，
不止可以向下搜，也可以向上搜。

ps查看进程信息并通过less分页显示

命令：ps -ef |less


查看命令历史使用记录并通过less分页显示
命令：history | less


浏览多个文件

命令：Less log2013.log log2014.log

 说明：

输入 ：n后，切换到 log2014.log
输入 ：p 后，切换到log2013.log

5．附加备注

1.全屏导航

ctrl + F - 向前移动一屏

ctrl + B - 向后移动一屏

ctrl + D - 向前移动半屏

ctrl + U - 向后移动半屏



2.单行导航

j - 向前移动一行

k - 向后移动一行



3.其它导航

G - 移动到最后一行

g - 移动到第一行

q / ZZ - 退出 less 命令



4.其它有用的命令

v - 使用配置的编辑器编辑当前文件

h - 显示 less 的帮助文档

&pattern - 仅显示匹配模式的行，而不是整个文件



5.标记导航

当使用 less 查看大文件时，可以在任何一个位置作标记，可以通过命令导航到标有特定标记的文本位置：

ma - 使用 a 标记文本的当前位置

'a - 导航到标记 a 处


head 与 tail

显示文件的前n行
命令：head -n 5 log2014.log

显示文件前n个字节
命令：head -c 20 log2014.log

文件的除了最后n个字节以外的内容
命令：head -c -32 log2014.log

输出文件除了最后n行的全部内容
命令：head -n -6 log2014.log

tail 命令从指定点开始将文件写到标准输出.使用tail命令的-f选项可以方便的查阅正在改变的日志文件,tail -f filename会把filename里最尾部的
内容显示在屏幕上,并且不但刷新,使你看到最新的文件内容.

显示文件末尾内容
命令：tail -n 5 log2014.log

从第5行开始显示文件
命令：tail -n +5 log2014.log


查找文件

which  查看可执行文件的位置。
whereis 查看文件的位置。
locate   配合数据库查看文件位置。
find   实际搜寻硬盘查询文件名称。

which命令的作用是，在PATH变量指定的路径中，搜索某个系统命令的位置，并且返回第一个搜索结果。
也就是说，使用which命令，就可以看到某个系统命令是否存在，以及执行的到底是哪一个位置的命令。


查找文件、显示命令路径

命令：which lsmod
输出：
[root@localhost ~]# which pwd
/bin/pwd
[root@localhost ~]#  which adduser
/usr/sbin/adduser
[root@localhost ~]#

说明：
which 是根据使用者所配置的 PATH 变量内的目录去搜寻可运行档的！所以，不同的 PATH 配置内容所找到的命令当然不一样的！

实例2：用 which 去找出 which
命令：which which
输出：
[root@localhost ~]# which which
alias which='alias | /usr/bin/which --tty-only --read-alias --show-dot 	--show-tilde'
     /usr/bin/which
[root@localhost ~]#

说明：

竟然会有两个 which ，其中一个是 alias 这就是所谓的『命令别名』，意思是输入 which 会等於后面接的那串命令！

实例3：找出 cd 这个命令

命令：which cd
说明：cd 这个常用的命令竟然找不到啊！为什么呢？这是因为 cd 是bash 内建的命令！ 但是 which 默认是找 PATH 内所规范的目录，所以当然一定找不到的！


将和**文件相关的文件都查找出来
命令：whereis svn

只将二进制文件 查找出来
命令：whereis -b svn

whereis -m svn 查出说明文档路径，whereis -s svn 找source源文件。


查找指定时间内修改过的文件
命令：find . -atime -2
说明：超找48小时内修改过的文件(有点猛，要过滤一下)


根据关键字查找
命令：find . -name "*.log"

按照目录或文件的权限来查找文件
命令：find /opt/soft/test/ -perm 777

按类型查找
命令：find . -type f -name "*.log"
说明：查找当目录，以.log结尾的普通文件

查找当前所有目录并排序
命令：find . -type d | sort

按大小查找文件
命令：find . -size +1000c -print
查找当前目录大于1K的文件

find exce

ls -l命令放在find命令的-exec选项中

命令：find . -type f -exec ls -l {} \;
说明:上面的例子中，find命令匹配到了当前目录下的所有普通文件，并在-exec选项中使用ls -l命令将它们列出


在目录中查找更改时间在n日以前的文件并删除它们

命令：find . -type f -mtime +14 -exec rm {} \;
在shell中用任何方式删除文件之前，应当先查看相应的文件，一定要小心！当使用诸如mv或rm命令时，可以使用-exec选项的安全模式。
它将在对每个匹配到的文件进行操作之前提示你。


在目录中查找更改时间在n日以前的文件并删除它们，在删除之前先给出提示

命令：find . -name "*.log" -mtime +5 -ok rm {} \;
在上面的例子中， find命令在当前目录中查找所有文件名以.log结尾、更改时间在5日以上的文件，并删除它们，只不过在删除之前先给出提示。
按y键删除文件，按n键不删除。

grep mv cp 等都可以在exec后面使用


使用xargs命令

在使用 find命令的-exec选项处理匹配到的文件时， find命令将所有匹配到的文件一起传递给exec执行。
但有些系统对能够传递给exec的命令长度有限制，这样在find命令运行几分钟之后，就会出现溢出错误。
错误信息通常是“参数列太长”或“参数列溢出”。这就是xargs命令的用处所在，特别是与find命令一起使用。
find命令把匹配到的文件传递给xargs命令，而xargs命令每次只获取一部分文件而不是全部，不像-exec选项那样。
这样它可以先处理最先获取的一部分文件，然后是下一批，并如此继续下去。
在有些系统中，使用-exec选项会为处理每一个匹配到的文件而发起一个相应的进程，并非将匹配到的文件全部作为参数一次执行；
这样在有些情况下就会出现进程过多，系统性能下降的问题，因而效率不高； 而使用xargs命令则只有一个进程。
另外，在使用xargs命令时，究竟是一次获取所有的参数，还是分批取得参数，以及每一次获取参数的数目都会根据该命令的选项及系统内核中相应的可调参数来确定。

查找系统中的每一个普通文件，然后使用xargs命令来测试它们分别属于哪类文件

命令：find . -type f -print | xargs file


在整个系统中查找内存信息转储文件(core dump) ，然后把结果保存到/tmp/core.log 文件中
命令：find / -name "core" -print | xargs echo "" >/tmp/core.log

在当前目录下查找所有用户具有读、写和执行权限的文件，并收回相应的写权限
命令：find . -perm -7 -print | xargs chmod o-w

用grep命令在所有的普通文件中搜索hostname这个词
命令：find . -type f -print | xargs grep "hostname"

用grep命令在当前目录下的所有普通文件中搜索hostnames这个词
命令：find . -name \* -type f -print | xargs grep "hostnames"


find后执行xargs提示xargs: argument line too long解决方法：
命令：
find . -type f -atime +0 -print0 | xargs -0 -l1 -t rm -f
输出：
[root@pd test4]#  find . -type f -atime +0 -print0 | xargs -0 -l1 -t rm -f
rm -f

说明：-l1是一次处理一个；-t是处理之前打印出命令


find命令参数详解

使用name选项：

文件名选项是find命令最常用的选项，要么单独使用该选项，要么和其他选项一起使用。
可以使用某种文件名模式来匹配文件，记住要用引号将文件名模式引起来。
不管当前路径是什么，如果想要在自己的根目录$HOME中查找文件名符合*.log的文件，使用~作为 'pathname'参数，波浪号~代表了你的$HOME目录


用perm选项：

按照文件权限模式用-perm选项,按文件权限模式来查找文件的话。最好使用八进制的权限表示法。
如在当前目录下查找文件权限位为755的文件，即文件属主可以读、写、执行，其他用户可以读、执行的文件，可以用：
[root@localhost test]# find . -perm 755 -print
还有一种表达方法：在八进制数字前面要加一个横杠-，表示都匹配，如-007就相当于777，-005相当于555

忽略某个目录：

如果在查找文件时希望忽略某个目录，因为你知道那个目录中没有你所要查找的文件，那么可以使用-prune选项来指出需要忽略的目录。
在使用-prune选项时要当心，因为如果你同时使用了-depth选项，那么-prune选项就会被find命令忽略。如果希望在test目录下查找文件，
但不希望在test/test3目录下查找，可以用：
命令：find test -path "test/test3" -prune -o -print


使用find查找文件的时候怎么避开某个文件目录：

实例1：在test 目录下查找不在test4子目录之内的所有文件
命令：find test -path "test/test4" -prune -o -print

说明：
find [-path ..] [expression]

在路径列表的后面的是表达式
-path "test" -prune -o -print 是 -path "test" -a -prune -o -print 的简写表达式按顺序求值, -a 和 -o 都是短路求值，与 shell 的 && 和 || 类似如果
-path "test" 为真，则求值 -prune , -prune 返回真，与逻辑表达式为真；否则不求值 -prune，与逻辑表达式为假。如果 -path "test" -a -prune 为假，则求值 -print ，-print返回真，或逻辑表达式为真；否则不求值 -print，或逻辑表达式为真。

这个表达式组合特例可以用伪码写为:

if -path "test" then
-prune
else
-print


避开多个文件夹:
命令：find test \( -path test/test4 -o -path test/test3 \) -prune -o -print
说明：圆括号表示表达式的结合。  \ 表示引用，即指示 shell 不对后面的字符作特殊解释，而留给 find 命令去解释其意义。
'''


'''
linux文件类型与扩展名

Linux文件类型常见的有：普通文件、目录文件、字符设备文件和块设备文件、符号链接文件等，现在我们进行一个简要的说明。

1. 普通文件 

我们用 ls -lh 来查看某个文件的属性，可以看到有类似-rwxrwxrwx，值得注意的是第一个符号是 - ，这样的文件在Linux中就是普通文件。
这些文件一般是用一些相关的应用程序创建，比如图像工具、文档工具、归档工具... .... 或 cp工具等。这类文件的删除方式是用rm 命令。 
另外，依照文件的内容，又大略可以分为：

1>. 纯文本档(ASCII)：

这是Linux系统中最多的一种文件类型，称为纯文本档是因为内容为我们人类可以直接读到的数据，例如数字、字母等等。
几乎只要我们可以用来做为设定的文件都属于这一种文件类型。 举例来说，你可以用命令： cat ~/.bashrc 来看到该文件的内容。 
(cat 是将一个文件内容读出来的指令).

2>. 二进制文件(binary)：

Linux系统其实仅认识且可以执行二进制文件(binary file)。Linux当中的可执行文件(scripts, 文字型批处理文件不算)就是这种格式的文件。
刚刚使用的命令cat就是一个binary file。

3>. 数据格式文件(data)： 

有些程序在运作的过程当中会读取某些特定格式的文件，那些特定格式的文件可以被称为数据文件 (data file)。举例来说，我们的Linux在使用者登录时
，都会将登录的数据记录在 /var/log/wtmp那个文件内，该文件是一个data file，他能够透过last这个指令读出来！ 但是使用cat时，
会读出乱码～因为他是属于一种特殊格式的文件？


2. 目录文件

当我们在某个目录下执行，看到有类似 drwxr-xr-x ，这样的文件就是目录，目录在Linux是一个比较特殊的文件。注意它的第一个字符是d。创建目录的命令可以用 mkdir 命令，或cp命令，cp可以把一个目录复制为另一个目录。删除用rm 或rmdir命令。 

3. 字符设备或块设备文件 

如时您进入/dev目录，列一下文件，会看到类似如下的:

[root@localhost ~]# ls -al /dev/tty

crw-rw-rw- 1 root tty 5, 0 11-03 15:11 /dev/tty

[root@localhost ~]# ls -la /dev/sda1

brw-r----- 1 root disk 8, 1 11-03 07:11 /dev/sda1

我们看到/dev/tty的属性是 crw-rw-rw- ，注意前面第一个字符是 c ，这表示字符设备文件。比如猫等串口设备。我们看到 /dev/sda1 的属性是 brw-r----- ，注意前面的第一个字符是b，这表示块设备，比如硬盘，光驱等设备。

这个种类的文件，是用mknode来创建，用rm来删除。目前在最新的Linux发行版本中，我们一般不用自己来创建设备文件。因为这些文件是和内核相关联的。

与系统周边及储存等相关的一些文件， 通常都集中在/dev这个目录之下！通常又分为两种：

区块(block)设备档 ：

就是一些储存数据， 以提供系统随机存取的接口设备，举例来说，硬盘与软盘等就是啦！ 你可以随机的在硬盘的不同区块读写，这种装置就是成组设备！你可以自行查一下/dev/sda看看， 会发现第一个属性为[ b ]！

字符(character)设备文件：

亦即是一些串行端口的接口设备， 例如键盘、鼠标等等！这些设备的特色就是一次性读取的，不能够截断输出。 举例来说，你不可能让鼠标跳到另一个画面，而是滑动到另一个地方！第一个属性为 [ c ]。

4. 数据接口文件(sockets)： 

数据接口文件（或者：套接口文件），这种类型的文件通常被用在网络上的数据承接了。我们可以启动一个程序来监听客户端的要求， 而客户端就可以透过这个socket来进行数据的沟通了。第一个属性为 [ s ]， 最常在/var/run这个目录中看到这种文件类型了。

例如：当我们启动MySQL服务器时，会产生一个mysql.sock的文件。

[root@localhost ~]# ls -lh /var/lib/mysql/mysql.sock 

srwxrwxrwx 1 mysql mysql 0 04-19 11:12 /var/lib/mysql/mysql.sock

注意这个文件的属性的第一个字符是 s

5. 符号链接文件： 

当我们查看文件属性时，会看到有类似 lrwxrwxrwx,注意第一个字符是l，这类文件是链接文件。是通过ln -s 源文件名 新文件名 。上面是一个例子，表示setup.log是install.log的软链接文件。怎么理解呢？这和Windows操作系统中的快捷方式有点相似。

符号链接文件的创建方法举例:

[root@localhost test]# ls -lh log2012.log

-rw-r--r-- 1 root root 296K 11-13 06:03 log2012.log

[root@localhost test]# ln -s log2012.log  linklog.log

[root@localhost test]# ls -lh *.log

lrwxrwxrwx 1 root root   11 11-22 06:58 linklog.log -> log2012.log

-rw-r--r-- 1 root root 296K 11-13 06:03 log2012.log

6. 数据输送文件（FIFO,pipe）:

FIFO也是一种特殊的文件类型，他主要的目的在解决多个程序同时存取一个文件所造成的错误问题。 FIFO是first-in-first-out的缩写。第一个属性为[p] 。

二. Linux文件扩展名

1. 扩展名类型

基本上，Linux的文件是没有所谓的扩展名的，一个Linux文件能不能被执行，与他的第一栏的十个属性有关， 与档名根本一点关系也没有。这个观念跟Windows的情况不相同喔！在Windows底下， 能被执行的文件扩展名通常是 .com .exe .bat等等，而在Linux底下，只要你的权限当中具有x的话，例如[ -rwx-r-xr-x ] 即代表这个文件可以被执行。

不过，可以被执行跟可以执行成功是不一样的～举例来说，在root家目录下的install.log 是一个纯文本档，如果经由修改权限成为 -rwxrwxrwx 后，这个文件能够真的执行成功吗？ 当然不行～因为他的内容根本就没有可以执行的数据。所以说，这个x代表这个文件具有可执行的能力， 但是能不能执行成功，当然就得要看该文件的内容.

虽然如此，不过我们仍然希望可以藉由扩展名来了解该文件是什么东西，所以，通常我们还是会以适当的扩展名来表示该文件是什么种类的。底下有数种常用的扩展名：

*.sh ： 脚本或批处理文件 (scripts)，因为批处理文件为使用shell写成的，所以扩展名就编成 .sh 

*Z, *.tar, *.tar.gz, *.zip, *.tgz： 经过打包的压缩文件。这是因为压缩软件分别为 gunzip, tar 等等的，由于不同的压缩软件，而取其相关的扩展名！

*.html, *.php：网页相关文件，分别代表 HTML 语法与 PHP 语法的网页文件。 .html 的文件可使用网页浏览器来直接开启，至于 .php 的文件， 则可以透过 client 端的浏览器来 server 端浏览，以得到运算后的网页结果。

基本上，Linux系统上的文件名真的只是让你了解该文件可能的用途而已，真正的执行与否仍然需要权限的规范才行。例如虽然有一个文件为可执行文件，如常见的/bin/ls这个显示文件属性的指令，不过，如果这个文件的权限被修改成无法执行时，那么ls就变成不能执行。

上述的这种问题最常发生在文件传送的过程中。例如你在网络上下载一个可执行文件，但是偏偏在你的 Linux系统中就是无法执行！呵呵！那么就是可能文件的属性被改变了。不要怀疑，从网络上传送到你的 Linux系统中，文件的属性与权限确实是会被改变的。

2. Linux文件名长度限制：

在Linux底下，使用预设的Ext2/Ext3文件系统时，针对文件名长度限制为：

单一文件或目录的最大容许文件名为 255 个字符

包含完整路径名称及目录 (/) 之完整档名为 4096 个字符

是相当长的档名！我们希望Linux的文件名可以一看就知道该文件在干嘛的， 所以档名通常是很长很长。

3. Linux文件名的字符的限制：

由于Linux在文字接口下的一些指令操作关系，一般来说，你在设定Linux底下的文件名时， 最好可以避免一些特殊字符比较好！例如底下这些：

* ? > < ; & ! [ ] | \ ' " ` ( ) { }

因为这些符号在文字接口下，是有特殊意义的。另外，文件名的开头为小数点“.”时， 代表这个文件为隐藏文件！同时，由于指令下达当中，常常会使用到 -option 之类的选项， 所以你最好也避免将文件档名的开头以 - 或 + 来命名。



增加文件所有用户组可执行权限

命令：chmod a+x log2012.log
同时修改不同用户权限

命令：chmod ug+w,o-x log2012.log
说明：即设定文件text的属性为：文件属主（u） 增加写权限;与文件属主同组用户（g） 增加写权限;其他用户（o） 删除执行权限


删除文件权限
命令：chmod a-x log2012.log
删除所有用户的可执行权限 


使用“=”设置权限 

命令：chmod u=x log2012.log

对一个目录及其子目录所有文件添加权限 
命令：chmod -R u+x test4
递归地给test4目录下所有文件和子目录的属主分配权限 
















'''

