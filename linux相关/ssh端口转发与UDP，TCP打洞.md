###SSH端口转发，实例分析

```angular2html
小米有一个腾讯云的主机，每个月10块钱，配置很低的那种，但是优点是有个外网ip，想在哪使用就在哪使用。
小米还有个性能很叼的机器，可惜外网不能使用，小米可以利用这个腾讯云的ecs去转发请求来登录内网机器。

1.服务端设置
先在腾讯云的/etc/ssh/sshd_config添加以下四项:

AllowAgentForwarding yes
AllowTcpForwarding yes
GatewayPorts yes
X11Forwarding yes
2.客户端连接
然后在客户机连接：

ssh -CfNg -R 目标端口:127.0.0.1:本地端口 -o ServerAliveInterval=30 用户名@腾讯云ip 
该命令会搭建一条ssh连接，使腾讯云主机的目标端口转发至本地端口。例如：

ssh -CfNg -R 33:127.0.0.1:22 -o ServerAliveInterval=30 ubuntu@192.168.1.1 
一旦有数据发送给192.168.1.1的33端口，就会将数据转发至客户机的22端口，即你可以通过腾讯云的33端口来登录内网机器了，6不6。注意腾讯云要自己去开启33端口哦
```

####SSH隧道技术（端口转发 与 socket 代理）

参考：https://blog.csdn.net/left_la/article/details/41519843


###NAT穿透

NAT名字很准确，网络地址转换，就是替换IP报文头部的地址信息。NAT通常部署在一个组织的网络出口位置，通过将内部网络IP地址替换为出口的IP地址提供公网可达性和上层协议的连接能力

NAT相关知识 参考 https://www.cnblogs.com/imstudy/p/5458133.html

UDP穿透NAT 参考 https://www.cnblogs.com/GO-NO-1/p/7241556.html

TCP穿透NAT 参考 http://www.360doc.com/content/18/0728/18/44856983_774004450.shtml