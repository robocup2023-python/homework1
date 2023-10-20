
import socket

class Client:
    def __init__(self,host="127.0.0.1",port=51111):
        self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect((host,port))

    def send(self,message):
        self.client.send(message.encode('gbk'))

    def receive(self):
        while True:
            try:
                message=self.client.recv(1024).decode("utf-8")
                print(message)
                self.client.close()
                break
            except:
                print("ERROR!!!")
                self.client.close()
                break
client=Client()
words=input("input your sentences: ")
client.send(words)
client.receive()

