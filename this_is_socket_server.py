import socket

"""

这是一个socket服务端 就是放在服务器上面用来接收客户端发送的信息的

"""



host = "0.0.0.0"

port = 7777

server = socket.socket()

server.bind((host, port))  # 注意  参数是一个元组
server.listen(1)
while 1:
    print("等待连接")
    conn, addr = server.accept()  # 创建socke和客户端通信
    print(conn, addr)
    mes = "hello"
    conn.send(mes.encode("utf-8"))
    conn.close()
