# coding:utf-8

'''
Docker 基本操作
'''

'''
Docker基本介绍和操作
Docker基本介绍
什么是Docker
Docker 最初是 dotCloud 公司创始人 Solomon Hykes 在法国期间发起的一个公司内部项目，它是基于 dotCloud 公司多年云服务技术的一次革新，并于 2013 年 3 月以 Apache 2.0 授权协议开源，主要项目代码在 GitHub 上进行维护。
Docker 使用 Google 公司推出的 Go 语言 进行开发实现，基于 Linux 内核的 cgroup，namespace，以及 AUFS 类的 Union FS 等技术，对进程进行封装隔离，属于 操作系统层面的虚拟化技术。由于隔离的进程独立于宿主和其它的隔离的进程，因此也称其为容器。最初实现是基于 LXC，从 0.7 版本以后开始去除 LXC，转而使用自行开发的 libcontainer，从 1.11 开始，则进一步演进为使用 runC 和 containerd。
Docker 在容器的基础上，进行了进一步的封装，从文件系统、网络互联到进程隔离等等，极大的简化了容器的创建和维护。使得 Docker 技术比虚拟机技术更为轻便、快捷。

Docker与传统虚拟化的不同
传统虚拟机技术是虚拟出一套硬件后，在其上运行一个完整操作系统，在该系统上再运行所需应用进程；而容器内的应用进程直接运行于宿主的内核，容器内没有自己的内核，而且也没有进行硬件虚拟。因此容器要比传统虚拟机更为轻便。

为什么使用Docker
更高效的利用系统资源
更快速的启动时间
一致的运行环境
持续交付和部署
更轻松的迁移
更轻松的维护和扩展
对比传统虚拟机总结，如下表：

特性	容器	虚拟机
启动	秒级	分钟级
硬盘使用	一般为 MB	一般为 GB
性能	接近原生	弱于
系统支持量	单机支持上千个容器	一般几十个


Docker基本概念
Docker 包括三个基本概念

镜像（Image）
容器（Container）
仓库（Repository）


Docker基本操作

Docker版本介绍
docker-ce-17.09.0.ce
系统环境是linux7.x
Docker服务相关命令

启动docker服务
systemctl start docker

查看docker服务状态
systemctl status docker

关闭docker服务
systemctl stop docker

docker开机自启动
systemctl enable docker
查看Docker信息
查看docker版本
docker version
查看docker系统信息
docker info
查看docker日志信息
docker logs
Docker镜像
镜像拉取
例如以 centos 为关键词进行搜索：
docker search centos
使用公司内部镜像库
docker login dockerhub.xxxxx.com
输入账号+密码
docker pull [选项] [Docker Registry 地址[:端口号]/]仓库名[:标签]
实战：如从公司内部镜像库下载CentOS镜像
docker pull dockerhub.xxxxx.com/global/centos:7.2.1511
使用第三方镜像仓库，如Docker
实战：如从Docker镜像库下载busybox
docker pull busybox
列出镜像
要想列出已经下载下来的镜像，可以使用 docker image 命令。

REPOSITORY                             TAG                 IMAGE ID            CREATED             SIZE
busybox                                latest              e1ddd7948a1c        5 days ago          1.16MB
说明：
列表包含了 仓库名、标签、镜像 ID、创建时间 以及 所占用的空间。
镜像推送
推送至公司内部镜像库
登录公司镜像库
docker login dockerhub.xxxx.com
输入账号+密码
如我们需要将 busybox:latest 推送至global项目下，具体操作步骤如下：
docker tag e1ddd7948a1c dockerhub.xxxx.com/global/busybox:v100
其中，e1ddd7948a1c 是镜像ID，可以通过docker images来查看。
操作Docker容器
运行镜像
实战：运行busybox，容器名字是datagrand，启动sh并且将其放到后台运行。

语法：docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
docker run -itd --name=datagrand busybox /bin/sh
其中：
-itd这三个参数分别表示：
-i：交互式操作
-t：终端
-d：后台运行
查看容器运行状态
正在运行的容器
docker ps
查找某个正在运行的容器，如上例中的datagrand
docker ps | grep datagrand
查看所有容器状态（包括运行和停止的）
docker ps -a
进入容器内部
语法：docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
docker exec -it b7df818849aa /bin/sh
其中b7df818849aa为容器ID，可通过docker ps来查看。
停止、重启和删除容器
docker stop b7df818849aa 
docker restart b7df818849aa
docker rm b7df818849aa
其中b7df818849aa为容器ID，可通过docker ps来查看。
删除本地镜像
语法：docker rmi [OPTIONS] IMAGE [IMAGE...]
docker rmi e1ddd7948a1c feac5e0dfdb2
其中e1ddd7948a1c和feac5e0dfdb2是镜像ID，可以通过docker images来查看。
请注意：在删除镜像之前，请将使用该镜像的容器停止和删除，否则会有如下报错：

Error response from daemon: conflict: unable to delete e1ddd7948a1c (cannot be forced) - image is being used by running container b7df818849aa
Error response from daemon: conflict: unable to delete e1ddd7948a1c (must be forced) - image is being used by stopped container b7df818849aa
镜像导出和导入

镜像导出
docker save e1ddd7948a1c |gzip > docker_file.tgz
其中，e1ddd7948a1c是镜像ID，可以通过docker images来查看。
镜像导入
docker load < docker_file.tgz 
#load
gunzip -c mycontainer.tgz | docker load

说明：
也可以使用Export和Import对容器进行导出和导入。
两者区别，这里简单说一下：
使用导出后再导入(exported-imported)的镜像会丢失所有的历史，而保存后再加载（saveed-loaded）的镜像没有丢失历史和层(layer)。这意味着使用导出后再导入的方式，你将无法回滚到之前的层(layer)，同时，使用保存后再加载的方式持久化整个镜像，就可以做到层回滚（可以执行docker tag <LAYER ID> <IMAGE NAME>来回滚之前的层）。



Docker 数据管理
为什么需要数据卷
当该容器不再运行时，数据将不会持久存在，并且如果另一个进程需要，则可能很难从容器中获取数据。
容器的可写层紧密耦合到运行容器的主机。无法轻松地将数据移动到其他位置。
写入容器的可写层需要 存储驱动程序来管理文件系统。存储驱动程序使用Linux内核提供联合文件系统。与使用直接写入主机文件系统的数据卷相比，这种额外的抽象降低了性能 。
Docker将数据从Docker主机安装到容器中三种方式：
数据卷（Volumes）
挂载主机目录 (Bind mounts)
tmpfs卷
容器中管理数据三种方式区别：
Volumes 存储在由Docker（/var/lib/docker/volumes/在Linux上）管理的主机文件系统的一部分中。非Docker进程不应修改文件系统的这一部分。卷是在Docker中保留数据的最佳方式。
Bind mounts 可以存储在主机系统的任何位置。它们甚至可能是重要的系统文件或目录。Docker主机或Docker容器上的非Docker进程可以随时修改它们。
tmpfs 挂载仅存储在主机系统的内存中，永远不会写入主机系统的文件系统。
什么是数据卷
数据卷 是一个可供一个或多个容器使用的特殊目录，它绕过 UFS，可以提供很多有用的特性：

可以在容器之间共享和重用
对数据卷的修改会立马生效
对数据卷的更新，不会影响镜像
数据卷默认会一直存在，即使容器被删除
注意：
数据卷的使用，类似于 Linux 下对目录或文件进行 mount，镜像中的被指定为挂载点的目录中的文件会隐藏掉，能显示看的是挂载的 数据卷。

创建和管理卷
创建一个卷
docker volume create my-vol
查看创建的卷
docker volume ls
查看卷详细信息
docker volume inspect my-vol
删除卷
docker volume rm my-vol
启动具有卷的容器
如果启动具有尚不存在的卷的容器，Docker会自动创建卷。
docker run -d \
  -it \
  --name datatest \
  --mount source=myvol2,target=/app \
  busybox
使用docker inspect devtest验证创建卷并安装正确。寻找Mounts部分：
"Mounts": [
            {
                "Type": "volume",
                "Name": "myvol2",
                "Source": "/data/sys/var/docker/volumes/myvol2/_data",
                "Destination": "/app",
                "Driver": "local",
                "Mode": "z",
                "RW": true,
                "Propagation": ""
            }
        ],
说明：mount是一个卷，它显示正确的源和目标，并且mount是可读写的。
停止容器并移除卷:
docker stop datatest
docker rm datatest
docker volume rm myvol2
使用只读卷
docker run -d \
  -it \
  --name=nginxtest \
  --mount source=nginx-vol,destination=/usr/share/nginx/html,readonly \
  nginx:latest
使用绑定挂载(Bind mounts)
与卷相比，绑定装载具有有限的功能。使用绑定装入时，主机上的文件或目录将装入容器中。文件或目录由其在主机上的完整路径或相对路径引用。相反，当你使用卷时，会在主机上的Docker存储目录中创建一个新目录，Docker会管理该目录的内容。
该文件或目录不需要已存在于Docker主机上。如果它尚不存在，则按需创建。绑定挂载非常高效，但它们依赖于具有特定目录结构的主机文件系统。

创建source路径文件target
mkdir /tmp/target
docker run -d \
  -it \
  --name devtest \
  --mount type=bind,source=/tmp/target,target=/app \
  busybox
使用docker inspect devtest验证绑定安装正确创建。寻找Mounts部分：

"Mounts": [
            {
                "Type": "bind",
                "Source": "/tmp/target",
                "Destination": "/app",
                "Mode": "",
                "RW": true,
                "Propagation": "rprivate"
            }
        ],
说明：
这表明mount是一个bindmount，它显示了正确的源和目标，它表明mount是读写的，并且传播设置为rprivate。
停止容器：

docker stop devtest
docker rm devtest
注意：
如果将bind-mount绑定到容器上的非空目录中，则绑定装置将隐藏目录的现有内容。

使用只读绑定挂载
docker run -d \
  -it \
  --name devtest \
  --mount type=bind,source="$(pwd)"/target,target=/app,readonly \
  nginx:latest
Docker容器网络
默认网络
安装Docker时，它会自动创建三个网络。可以使用以下docker network ls命令列出这些网络：

docker network ls

NETWORK ID          NAME                DRIVER
7fca4eb8c647        bridge              bridge
9f904ee27bf5        none                null
cf03ee007fb4        host                host
说明：

这三个网络内置于Docker中。运行容器时，可以使用该--network标志指定容器应连接到的网络。
bridge所有Docker主机上都存在默认网络。如果未指定其他网络，则新容器将自动连接到默认bridge网络。
创建网络
创建了桥接网络
docker network create --driver bridge datagrand
docker network create datatest
查看创建的网络
docker network ls
NETWORK ID          NAME                   DRIVER              SCOPE
3bf08b12e820        datagrand              bridge              local
0e155373e305        datatest               bridge              local
说明：
默认创建的是bridge网络
删除网络
docker network rm datatest datagrand
网络端口映射
-P（大写）
创建容器时，使用 -P 标志用于自动将其中的任何网络端口映射到Docker主机上临时端口范围内的随机高端口。
实战：运行一个ngin容器，将容器中的端口80 和 443 绑定到主机上的随机高端口。

docker run -itd --name nginxtest -P nginx:1.7.9 /bin/bash
查看nginx容器运行情况：
docker ps
CONTAINER ID        IMAGE                                      COMMAND                  CREATED             STATUS              PORTS                                           NAMES
09cc5e292f7d        nginx:1.7.9                                "/bin/bash"              4 seconds ago       Up 2 seconds        0.0.0.0:32770->80/tcp, 0.0.0.0:32769->443/tcp   nginxtest
-p（小写）
说明：-p 可以多次使用该标志来配置多个端口。

创建容器时，使用该-p标志将容器的端口绑定到特定端口。
实战：运行一个ngin容器，将主机的端口8080映射到容器的端口80.

docker run -itd --name nginxtest -p 8080:80  nginx:1.7.9 /bin/bash
查看nginx容器运行情况：
docker ps
CONTAINER ID        IMAGE                                      COMMAND                  CREATED             STATUS              PORTS                           NAMES
89469d564c89        nginx:1.7.9                                "/bin/bash"              3 seconds ago       Up 3 seconds        443/tcp, 0.0.0.0:8080->80/tcp   nginxtest
创建容器时，使用该-p标志将容器的端口绑定到一定范围内随机端口。
实战：运行一个ngin容器，将容器中的端口80绑定到主机上8000到9000之间的随机可用端口。

docker run -itd --name nginxtest -p 8000-9000:80  nginx:1.7.9 /bin/bash
查看nginx容器运行情况：
docker ps
CONTAINER ID        IMAGE                                      COMMAND                  CREATED             STATUS              PORTS                           NAMES
dbaeeba59908        nginx:1.7.9                                "/bin/bash"              3 seconds ago       Up 3 seconds        443/tcp, 0.0.0.0:8000->80/tcp   nginxtest
默认情况下，该-p标志将指定的端口绑定到主机上的所有接口。但您也可以指定绑定到特定接口，例如仅指定localhost。
实战：运行一个ngin容器，将容器中的端口80绑定到主机127.0.0.1:8080上

docker run -itd --name nginxtest -p 127.0.0.1:8080:80  nginx:1.7.9 /bin/bash
查看nginx容器运行情况：
docker ps
CONTAINER ID        IMAGE                                      COMMAND                  CREATED             STATUS              PORTS                             NAMES
205dd2ed1640        nginx:1.7.9                                "/bin/bash"              3 seconds ago       Up 3 seconds        443/tcp, 127.0.0.1:8080->80/tcp   nginxtest
或者，要将容器的端口80绑定到动态端口，但只能在其上 localhost。

docker run -itd --name nginxtest -p 127.0.0.1::80  nginx:1.7.9 /bin/bash
查看nginx容器运行情况：
docker ps
CONTAINER ID        IMAGE                                      COMMAND                  CREATED             STATUS              PORTS                              NAMES
ba506a445ccc        nginx:1.7.9                                "/bin/bash"              2 seconds ago       Up 2 seconds        443/tcp, 127.0.0.1:32769->80/tcp   nginxtest
可以通过添加尾部来绑定UDP端口/udp
docker run -d -p 127.0.0.1:80:5000/udp training/webapp python app.py

'''

'''
镜像的构成与定制
'''

'''
Docker镜像构成和定制
利用 commit 理解镜像构成
docker commit 命令应用场合
docker commit 命令除了学习之外，还有一些特殊的应用场合，比如被***后保存现场等。但是，不要使用 docker commit 定制镜像，定制镜像应该使用 Dockerfile 来完成。

慎用 docker commit
使用 docker commit 意味着所有对镜像的操作都是黑箱操作，生成的镜像也被称为黑箱镜像，换句话说，就是除了制作镜像的人知道执行过什么命令、怎么生成的镜像，别人根本无从得知。而且，即使是这个制作镜像的人，过一段时间后也无法记清具体在操作的。虽然 docker diff 或许可以告诉得到一些线索，但是远远不到可以确保生成一致镜像的地步。这种黑箱镜像的维护工作是非常痛苦的。

使用 Dockerfile 定制镜像
Dockerfile 是一个文本文件，其内包含了一条条的指令(Instruction)，每一条指令构建一层，因此每一条指令的内容，就是描述该层应当如何构建。

Dockerfile 指令介绍
COPY 复制文件
格式：
* COPY <源路径>... <目标路径>
* COPY ["<源路径1>",... "<目标路径>"]
比如：
COPY package.json /usr/src/app/
说明：
<源路径> 可以是多个，甚至可以是通配符，其通配符规则要满足 Go 的 filepath.Match 规则，如：
COPY hom* /mydir/
COPY hom?.txt /mydir/
<目标路径> 可以是容器内的绝对路径，也可以是相对于工作目录的相对路径（工作目录可以用 WORKDIR 指令来指定）。目标路径不需要事先创建，如果目录不存在会在复制文件前先行创建缺失目录。
注意：
使用 COPY 指令，源文件的各种元数据都会保留。比如读、写、执行权限、文件变更时间等。这个特性对于镜像定制很有用。特别是构建相关文件都在使用 Git 进行管理的时候。
ADD 更高级的复制文件
ADD 指令和 COPY 的格式和性质基本一致。但是在 COPY 基础上增加了一些功能。
如果 <源路径> 为一个 tar 压缩文件的话，压缩格式为 gzip, bzip2 以及 xz 的情况下，ADD 指令将会自动解压缩这个压缩文件到 <目标路径> 去。
最适合使用 ADD 的场合，就是当我们需要自动解压缩的场合。如官方镜像 ubuntu 中：

FROM scratch ##空白镜像
ADD ubuntu-xenial-core-cloudimg-amd64-root.tar.gz /
...
由于ADD 则包含了更复杂的功能，其行为也不一定很清晰。它不像COPY 的语义很明确，就是复制文件而已。所以，我们还是尽可能使用COPY吧。

CMD 容器启动命令
CMD 指令就是用于指定默认的容器主进程的启动命令的。

CMD 指令的格式和 RUN 相似，也是两种格式：
* shell 格式：CMD <命令>
* exec 格式：CMD ["可执行文件", "参数1", "参数2"...]
* 参数列表格式：CMD ["参数1", "参数2"...]。在指定了 ENTRYPOINT 指令后，用 CMD 指定具体的参数。
在运行时可以指定新的命令来替代镜像设置中的这个默认命令，比如，nginx：1.7.9 镜像默认的 CMD 是 /bin/bash ，如果我们直接使用 docker run -it nginx：1.7.9 的话，会直接进入 bash 。
我们也可以在运行时指定运行别的命令，如 docker run -it nginx:1.7.9 cat /etc/os-release。这就是用 cat /etc/os-release 命令替换了默认的 /bin/bash 命令了，输出了系统版本信息。
在指令格式上，一般推荐使用 exec 格式，这类格式在解析时会被解析为 JSON 数组，因此一定要使用双引号 "，而不要使用单引号。

shell格式：
CMD echo $HOME
exec格式：
CMD [ "sh", "-c", "echo $HOME" ]
这就是为什么我们可以使用环境变量的原因，因为这些环境变量会被 shell 进行解析处理。
容器中应用在前台执行和后台执行的问题
Docker 不是虚拟机，容器中的应用都应该以前台执行，而不是像虚拟机、物理机里面那样，用 upstart/systemd 去启动后台服务，容器内没有后台服务的概念。

比如，关于nginx的启动，我们错误的写成：

CMD service nginx start
或
CMD systemctl start nginx
然后发现容器执行后就立即退出了。对于容器而言，其启动程序就是容器应用进程，容器就是为了主进程而存在的，主进程退出，容器就失去了存在的意义，从而退出，其它辅助进程不是它需要关心的东西。
而使用 service nginx start 命令，则是希望 upstart 来以后台守护进程形式启动 nginx 服务。通过上面内容我们了解到 CMD service nginx start 会被理解为 CMD [ "sh", "-c", "service nginx start"]，因此主进程实际上是 sh。那么当 service nginx start 命令结束后，sh 也就结束了，sh 作为主进程退出了，自然就会令容器退出。
正确的做法是直接执行 nginx 可执行文件，并且以前台形式运行，如：

CMD ["nginx", "-g", "daemon off;"]
ENTRYPOINT 入口点
ENTRYPOINT 的格式和 RUN 指令格式一样，分为 exec 格式和 shell 格式。
ENTRYPOINT 的目的和 CMD 一样，都是在指定容器启动程序及参数。ENTRYPOINT 在运行时也可以替代，不过比 CMD 要略显繁琐，需要通过 docker run 的参数 --entrypoint 来指定。
当指定了 ENTRYPOINT 后，CMD 的含义就发生了改变，不再是直接的运行其命令，而是将 CMD 的内容作为参数传给 ENTRYPOINT 指令，换句话说实际执行时，将变为：

<ENTRYPOINT> "<CMD>"
那么有了 CMD 后，为什么还要有 ENTRYPOINT 呢？这种 <ENTRYPOINT> "<CMD>" 有什么好处么？让我们来看两个场景。

场景一：让镜像变成像命令一样使用
假设我们需要一个得知自己当前公网 IP 的镜像，那么可以先用 CMD 来实现：

FROM ubuntu:16.04
RUN apt-get update \
    && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*
CMD [ "curl", "-s", "http://ip.cn" ]
假如我们使用 docker build -t myip . 来构建镜像的话，如果我们需要查询当前公网 IP，只需要执行：

$ docker run myip
当前 IP：61.148.226.66 来自：北京市 联通
从上面的 CMD 中可以看到实质的命令是 curl，那么如果我们希望显示 HTTP 头信息，就需要加上 -i 参数。那么我们可以直接加 -i 参数给 docker run myip 么？

docker run myip -i
docker: Error response from daemon: invalid header field value "oci runtime error: container_linux.go:247: starting container process caused \"exec: \\\"-i\\\": executable file not found in $PATH\"\n".
执行报错，executable file not found。之前我们说过，跟在镜像名后面的是 command，运行时会替换 CMD 的默认值。因此这里的 -i 替换了原来的 CMD，而不是添加在原来的 curl -s http://ip.cn 后面。而 -i 根本不是命令，所以自然找不到。
那么如果我们希望加入 -i 这参数，我们就必须重新完整的输入这个命令：

docker run myip curl -s http://ip.cn -i
这显然不是很好的解决方案，而使用 ENTRYPOINT 就可以解决这个问题。现在我们重新用 ENTRYPOINT 来实现这个镜像：

FROM ubuntu:16.04
RUN apt-get update \
    && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*
ENTRYPOINT [ "curl", "-s", "http://ip.cn" ]
这次我们再来尝试直接使用 docker run myip -i：

docker run myip
当前 IP：61.148.226.66 来自：北京市 联通

docker run myip -i
HTTP/1.1 200 OK
...
这次成功了。这是因为当存在 ENTRYPOINT 后，CMD 的内容将会作为参数传给 ENTRYPOINT，而这里 -i 就是新的 CMD，因此会作为参数传给 curl，从而达到了我们预期的效果。

场景二：应用运行前的准备工作
启动容器就是启动主进程，但有些时候，启动主进程前，需要一些准备工作。
比如 mysql 类的数据库，可能需要一些数据库配置、初始化的工作，这些工作要在最终的 mysql 服务器运行之前解决。
此外，可能希望避免使用 root 用户去启动服务，从而提高安全性，而在启动服务前还需要以 root 身份执行一些必要的准备工作，最后切换到服务用户身份启动服务。或者除了服务外，其它命令依旧可以使用 root 身份执行，方便调试等。
这些准备工作是和容器 CMD 无关的，无论 CMD 为什么，都需要事先进行一个预处理的工作。这种情况下，可以写一个脚本，然后放入 ENTRYPOINT 中去执行，而这个脚本会将接到的参数（也就是 <CMD>）作为命令，在脚本最后执行。比如官方镜像 redis 中就是这么做的：

FROM alpine:3.4
...
RUN addgroup -S redis && adduser -S -G redis redis
...
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 6379
CMD [ "redis-server" ]
可以看到其中为了 redis 服务创建了 redis 用户，并在最后指定了 ENTRYPOINT 为 docker-entrypoint.sh 脚本。

#!/bin/sh
...
# allow the container to be started with `--user`
if [ "$1" = 'redis-server' -a "$(id -u)" = '0' ]; then
    chown -R redis .
    exec su-exec redis "$0" "$@"
fi

exec "$@"
该脚本的内容就是根据 CMD 的内容来判断，如果是 redis-server 的话，则切换到 redis 用户身份启动服务器，否则依旧使用 root 身份执行。比如：

docker run -it redis id
uid=0(root) gid=0(root) groups=0(root)
ENV 设置环境变量
这个指令很简单，就是设置环境变量.

格式有两种：

* ENV  <key> <value>
* ENV  <key1>=<value1> <key2>=<value2>...
实例如下：

ENV MYSQL_ROOT_PASSWORD="123456" \
    MYSQL_DATABASE="edusoho" \ 
    MYSQL_USER="edusoho" \
    MYSQL_PASSWORD="edusoho"
这个例子中演示了如何换行，以及对含有空格的值用双引号括起来的办法，这和 Shell 下的行为是一致的。
定义了环境变量，那么在后续的指令中，就可以使用这个环境变量。比如在官方 node 镜像 Dockerfile 中，就有类似这样的代码：

ENV NODE_VERSION 7.2.0

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.xz" \
  && curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
  && gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \
  && grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum -c - \
  && tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local --strip-components=1 \
  && rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt \
  && ln -s /usr/local/bin/node /usr/local/bin/nodejs
在这里先定义了环境变量 NODE_VERSION，其后的 RUN 这层里，多次使用 $NODE_VERSION 来进行操作定制。可以看到，将来升级镜像构建版本的时候，只需要更新 7.2.0 即可，Dockerfile 构建维护变得更轻松了。
下列指令可以支持环境变量展开：

ADD、COPY、ENV、EXPOSE、LABEL、USER、WORKDIR、VOLUME、STOPSIGNAL、ONBUILD
可以从这个指令列表里感觉到，环境变量可以使用的地方很多，很强大。通过环境变量，我们可以让一份 Dockerfile 制作更多的镜像，只需使用不同的环境变量即可。

ARG 构建参数
格式：

ARG <参数名>[=<默认值>]
构建参数和 ENV 的效果一样，都是设置环境变量。所不同的是，ARG 所设置的构建环境的环境变量，在将来容器运行时是不会存在这些环境变量的。但是不要因此就使用 ARG 保存密码之类的信息，因为 docker history 还是可以看到所有值的。
Dockerfile 中的 ARG 指令是定义参数名称，以及定义其默认值。该默认值可以在构建命令 docker build 中用 --build-arg <参数名>=<值> 来覆盖。
在 1.13 之前的版本，要求 --build-arg 中的参数名，必须在 Dockerfile 中用 ARG 定义过了，换句话说，就是 --build-arg 指定的参数，必须在 Dockerfile 中使用了。如果对应参数没有被使用，则会报错退出构建。
从 1.13 开始，这种严格的限制被放开，不再报错退出，而是显示警告信息，并继续构建。报错信息如下例所示：

[Warning] One or more build-args [foo] were not consumed.
VOLUME 定义匿名卷
格式为：

VOLUME ["<路径1>", "<路径2>"...]
VOLUME <路径>
容器运行时应该尽量保持容器存储层不发生写操作，对于数据库类需要保存动态数据的应用，其数据库文件应该保存于卷(volume)中，关于Docker 卷的概念和使用，可参考本库文章
“Docker基本介绍和操作.md”。
为了防止运行时用户忘记将动态文件所保存目录挂载为卷，在 Dockerfile 中，我们可以事先指定某些目录挂载为匿名卷，这样在运行时如果用户不指定挂载，其应用也可以正常运行，不会向容器存储层写入大量数据。
比如：

VOLUME /data
这里的 /data 目录就会在运行时自动挂载为匿名卷，任何向 /data 中写入的信息都不会记录进容器存储层，从而保证了容器存储层的无状态化。
如果我们想把这个匿名卷中的内容挂载到主机上呢？

docker run -itd --name busytest --mount type=bind,source=/teng,target=/data busytest:v1
或
docker run -itd --name busytest -v /teng:/data busytest:v1
EXPOSE 声明端口
EXPOSE <port> [<port>/<protocol>...]
该EXPOSE指令通知Docker容器在运行时侦听指定的网络端口。可以指定端口是侦听TCP还是UDP，如果未指定协议，则默认为TCP。
EXPOSE 指令是声明运行时容器提供服务端口，这只是一个声明，在运行时并不会因为这个声明应用就会开启这个端口的服务。在 Dockerfile 中写入这样的声明有两个好处，一个是帮助镜像使用者理解这个镜像服务的守护端口，以方便配置映射；另一个用处则是在运行时使用随机端口映射时，也就是 docker run -P 时，会自动随机映射 EXPOSE 的端口。

比如，我这里编写一个Dockerfile文件：

FROM busybox
VOLUME /data
EXPOSE 80

docker build -t busytest:v2 .

docker run -itd --name busytest -P busytest:v2

docker ps
CONTAINER ID        IMAGE                                      COMMAND                  CREATED             STATUS              PORTS                         NAMES
30614a66bff0        busytest:v2                                "sh"                     3 seconds ago       Up 2 seconds        0.0.0.0:32771->80/tcp         busytest
无论EXPOSE设置如何，您都可以使用-p标志在运行时覆盖它们。例如

 docker run -itd --name busytest -p 8080:80  busytest:v2
 docker ps
CONTAINER ID        IMAGE                                      COMMAND                  CREATED             STATUS              PORTS                         NAMES
b07c5575afa1        busytest:v2                                "sh"                     3 seconds ago       Up 2 seconds        0.0.0.0:8080->80/tcp          busytest
WORKDIR 指定工作目录
格式为 WORKDIR <工作目录路径>。
使用 WORKDIR 指令可以来指定工作目录（或者称为当前目录），以后各层的当前目录就被改为指定的目录，如该目录不存在，WORKDIR 会帮你建立目录。
在Dockerfile中可以多次使用WORKDIR指令。如果提供了相对路径，则它将相对于前一条WORKDIR指令的路径 。例如：

WORKDIR /a
WORKDIR b
WORKDIR c
RUN pwd

最终pwd命令的输出Dockerfile将是 /a/b/c。
该WORKDIR指令可以解析先前使用的环境变量 ENV。您只能使用显式设置的环境变量Dockerfile。例如：

ENV DIRPATH /path
WORKDIR $DIRPATH/$DIRNAME
RUN pwd

最终pwd命令的输出Dockerfile将是 /path/$DIRNAME
USER 指定当前用户
格式：
USER <user>[:<group>] or
USER <UID>[:<GID>]

USER 指令和 WORKDIR 相似，都是改变环境状态并影响以后的层。WORKDIR 是改变工作目录，USER 则是改变之后层的执行 RUN, CMD 以及 ENTRYPOINT 这类命令的身份。
当然，和 WORKDIR 一样，USER 只是帮助你切换到指定用户而已，这个用户必须是事先建立好的，否则无法切换。
如：

RUN groupadd -r redis && useradd -r -g redis redis
USER redis
RUN [ "redis-server" ]
如果以 root 执行的脚本，在执行期间希望改变身份，比如希望以某个已经建立好的用户来运行某个服务进程，不要使用 su 或者 sudo，这些都需要比较麻烦的配置，而且在 TTY 缺失的环境下经常出错。建议使用 gosu。

# 建立 redis 用户，并使用 gosu 换另一个用户执行命令
RUN groupadd -r redis && useradd -r -g redis redis
# 下载 gosu
RUN wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/1.7/gosu-amd64" \
    && chmod +x /usr/local/bin/gosu \
    && gosu nobody true
# 设置 CMD，并以另外的用户执行
CMD [ "exec", "gosu", "redis", "redis-server" ]

'''

'''
Docker 三剑客之Compose
'''

'''
Docker三剑客之Compose
Docker Compose 是 Docker 官方编排（Orchestration）项目之一，负责快速的部署分布式应用。

Compose 基本介绍
Compose 简介
Compose代码
Compose 项目是 Docker 官方的开源项目，负责实现对 Docker 容器集群的快速编排。从功能上看，跟 OpenStack 中的 Heat 十分类似。
Compose 定位是 「定义和运行多个 Docker 容器的应用（Defining and running multi-container Docker applications）」，其前身是开源项目 Fig。

为什么使用Compose
在Docker镜像构成和定制介绍中，我们可以使用Dockerfile文件很方便定义一个单独的应用容器。
然而，在日常工作中，经常会碰到需要多个容器相互配合来完成某项任务的情况。例如要实现一个 Web 项目，除了 Web 服务容器本身，往往还需要再加上后端的数据库服务容器，甚至还包括负载均衡容器等。
Compose 恰好满足了这样的需求。它允许用户通过一个单独的 docker-compose.yml 模板文件（YAML 格式）来定义一组相关联的应用容器为一个项目（project）。

docker-compose.yml看起来像这样：
version: '3'
services:
  web:
    build: .
    ports:
    - "5000:5000"
    volumes:
    - .:/code
    - logvolume01:/var/log
    links:
    - redis
  redis:
    image: redis
volumes:
  logvolume01: {}
Compose 中两个重要的概念
服务 (service)：一个应用的容器，实际上可以包括若干运行相同镜像的容器实例。
项目 (project)：由一组关联的应用容器组成的一个完整业务单元，在 docker-compose.yml 文件中定义。
说明：

Compose 的默认管理对象是项目，通过子命令对项目中的一组容器进行便捷地生命周期管理。
Compose 项目由 Python 编写，实现上调用了 Docker 服务提供的 API 来对容器进行管理。因此，只要所操作的平台支持 Docker API，就可以在其上利用 Compose 来进行编排管理。
Compose 安装与卸载
Docker 版本
docker-ce-17.09.0.ce
系统环境是linux7.x
PIP 安装
pip install docker-compose
Compose 版本
docker-compose --version
docker-compose version 1.21.2, build a133471
卸载
如果是通过 pip 安装的，则执行如下命令即可删除。

pip uninstall docker-compose
实战--使用docker-compose部署Edusoho平台
项目目录结构
# pwd
/root/docker-lnmp
# tree -L 3
.
├── docker-compose.yml
├── mysql
│   ├── data
│   └── my.cnf
├── nginx
│   ├── conf.d
│   │   └── default.conf
│   ├── Dockerfile
│   ├── edusoho
│   │   ├── api
│   │   ├── app
│   │   ├── bootstrap
│   │   ├── plugins
│   │   ├── src
│   │   ├── vendor
│   │   ├── vendor_user
│   │   └── web
│   ├── edusoho-8.2.38.tar.gz
│   ├── log
│   │   └── error.log
│   ├── nginx.conf
│   ├── ssl
│   │   ├── nginx.key
│   │   └── nginx.pem
│   └── www
│       ├── db.php
│       ├── index.html
│       ├── index.php
├── php
│   ├── Dockerfile
│   ├── log
│   │   └── php-fpm.log
│   ├── php-fpm.conf
│   ├── php.ini
│   └── www.conf
项目docker-compose.yml文件
version: '3'
# 定义三个服务nginx，php，mysql
services:
  nginx:
    # 依赖php服务，意味着在启动nginx之前先启动php
    depends_on:
      - php
      # nginx镜像的路径
    build: ./nginx
        # 这样使nginx容器把网站文件和目录存放到主机目录中，持久化和方便管理
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
      - ./nginx/log/error.log:/var/log/nginx/error.log
      - ./nginx/edusoho:/usr/share/nginx/html
        # nginx意外退出时自动重启
    restart: always

        # 映射80端口
    ports:
      - "80:80"
     # - "443:443"
    networks:
      - frontend

        # 容器名称
    container_name: nginx

  php:
    depends_on:
      - mysql
    build: ./php
    ports:
      - "9000"
    networks:
      - frontend
      - backend      
    volumes:
      - ./php/php-fpm.conf:/usr/local/php/etc/php-fpm.conf
      - ./php/www.conf:/usr/local/php/etc/php-fpm.d/www.conf
      - ./php/php.ini:/usr/local/php/etc/php.ini
      - ./php/log/php-fpm.log:/usr/local/php/var/log/php-fpm.log
      - ./nginx/edusoho:/usr/share/nginx/html
    restart: always
    container_name: php

  # MySQL
  mysql:
    image: "dockerhub.datagrand.com/global/mysql:5.6"
    ports:
      - "3306:3306"
    volumes:
      - ./mysql/data:/var/lib/mysql
      - ./mysql/my.cnf:/etc/my.cnf
    environment:
      MYSQL_ROOT_PASSWORD: 123456
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
    command: ['mysqld', '--character-set-server=utf8']
    networks:
      - backend
    restart: always
    container_name: mysql
  #Network    
networks:
  frontend:
  backend:
后台启动并运行所有容器
docker-compose up -d

-d 在后台运行服务容器
docker-compose.yml 文件内容说明
默认的模板文件名称为 docker-compose.yml，格式为 YAML 格式。

version
Compose文件版本，详见Compose file versions and upgrading | Docker Documentation

depends_on
使用depends_on选项控制服务启动的顺序。详见Control startup order in Compose

services:
  nginx:
    # 依赖php服务，意味着在启动nginx之前先启动php
    depends_on:
      - php
说明：
nginx服务不会等待php完全启动之后才启动！
build
指定 Dockerfile 所在文件夹的路径（可以是绝对路径，或者相对 docker-compose.yml 文件的路径）。 Compose 将会利用它自动构建这个镜像，然后使用这个镜像。
详见build

# nginx镜像的路径
    build: ./nginx
你也可以使用 context 指令指定 Dockerfile 所在文件夹的路径。
使用 dockerfile 指令指定 Dockerfile 文件名。
使用 arg 指令指定构建镜像时的变量。

version: '3'
services:

  webapp:
    build:
      context: ./dir
      dockerfile: Dockerfile-alternate
      args:
        buildno: 1
volumes
数据卷所挂载路径设置。可以设置宿主机路径 (HOST:CONTAINER) 或加上访问模式 (HOST:CONTAINER:ro）。
该指令中路径支持相对路径。详见volumes

 volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
      - ./nginx/log/error.log:/var/log/nginx/error.log
      - ./nginx/edusoho:/usr/share/nginx/html
restart
no是默认的重新启动策略，它不会在任何情况下重新启动容器。当always指定时，容器总是重新启动。
该命令对保持服务始终运行十分有效，在生产环境中推荐配置为 always 或者 unless-stopped。
详见restart

restart: "no"
restart: always
restart: on-failure
restart: unless-stopped

注意：使用（版本3）Compose文件在群集模式下部署堆栈时，将忽略此选项 。请改用restart_policy。
ports
暴露端口信息。
使用宿主端口：容器端口 (HOST:CONTAINER) 格式，或者仅仅指定容器的端口（宿主将会随机选择端口）。
详见ports

ports:
 - "3000"
 - "3000-3005"
 - "8000:8000"
 - "9090-9091:8080-8081"
 - "49100:22"
 - "127.0.0.1:8001:8001"
 - "127.0.0.1:5000-5010:5000-5010"
 - "6060:6060/udp"
注意：以HOST:CONTAINER格式映射端口时，使用低于60的容器端口时可能会遇到错误的结果，因为YAML会将格式xx:yy中的数字解析为base-60值。因此，我们建议始终将端口映射明确指定为字符串。

networks
配置容器连接的网络。详见网络配置

创建frontend网络
docker network create frontend
查看网络
docker network ls
删除网络
docker network rm frontend
container_name
指定容器名称。默认将会使用 项目名称_服务名称_序号 这样的格式。
注意： 使用（版本3）Compose文件在群集模式下部署堆栈时，将忽略此选项。
详见container_name

 # 容器名称
    container_name: nginx
environment
详见environment

设置环境变量。你可以使用数组或字典两种格式。
environment:
      MYSQL_ROOT_PASSWORD: 123456
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: wordpress
或
environment:
      - MYSQL_ROOT_PASSWORD=123456
      - MYSQL_DATABASE=wordpress
      - MYSQL_USER=wordpress
      - MYSQL_PASSWORD=wordpress
如果变量名称或者值中用到 true|false，yes|no 等表达 布尔 含义的词汇，最好放到引号里，避免 YAML 自动解析某些内容为对应的布尔语义。
这些特定词汇，包括:
y|Y|yes|Yes|YES|n|N|no|No|NO|true|True|TRUE|false|False|FALSE|on|On|ON|off|Off|OFF
environment:
  RACK_ENV: development
  SHOW: 'true'
或
environment:
  - RACK_ENV=development
  - SHOW=true
只给定名称的变量会自动获取运行 Compose 主机上对应变量的值，可以用来防止泄露不必要的数据。
environment:
  RACK_ENV: development
  SESSION_SECRET:

environment:
  - RACK_ENV=development
  - SESSION_SECRET
command
覆盖容器启动后默认执行的命令。详见command


command: bundle exec thin -p 3000
该命令也可以是一个列表，方式类似于 dockerfile：
command: ["bundle", "exec", "thin", "-p", "3000"]

'''