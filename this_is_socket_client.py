import socket

"""

这是一个socket客户端 就是用户使用的一端 用来向服务器发起连接并接收或者发送信息的

"""


client = socket.socket()

client.connect(("127.0.0.1", 7777))

mes = client.recv(1024)

client.close()

print(mes.decode("utf-8"))
