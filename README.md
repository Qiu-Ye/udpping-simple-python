# UDPping-simple-python

## Client.py
### 简述
这是一个基于UDP协议的简单版ping程序。（标准的ping程序使用IMCP协议）

### 功能
+ 该客户发送一个简单的ping报文
+ 接收从服务器返回的对应pong报文
+ 并确定从该客户发送ping报文到接收到pong报文为止的往返时延（RTT）
+ 客户程序经UDP向目标服务器发送10个ping报文，对于每个报文，当对应的pong报文返回时，客户端确认并打印RTT
+ 由于UDP是不可靠的协议，由客户端发出的分组可能会丢失，因此设定等待服务器回答的时间至多为1s
+ 如果没有收到回答，则假定该分组丢失，打印提醒

## Server.py
### 简述
简单的UDP服务器程序。

## 使用说明
+ 在一主机上运行`Server.py`程序作为服务器
+ 修改`Client.py`中`serverName`为服务器的IP地址
+ 在另一台能和服务器通信的主机上运行`Client.py`
# udpping-simple-python
