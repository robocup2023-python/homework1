import threading
import socket
import requests
import random
import hashlib
def translate_text(text):
    src='zh'
    obj='en'
    appid='20231018001851631'
    secretkey='vlyThpNAJGiGtKjikSuJ'
    myurl='http://api.fanyi.baidu.com/api/trans/vip/translate'
    salt=random.randint(31256,66253)
    sign=appid+text+str(salt)+secretkey
    m1=hashlib.md5()
    m1.update(sign.encode("utf-8"))#?
    sign=m1.hexdigest()#?
    myurl1=myurl+"?q="+text+"&from="+src+"&to="+obj+'&appid='+appid+"&salt="+str(salt)+'&sign='+m1.hexdigest()#?

    english_data=requests.get(myurl1)
    js_data=english_data.json()
    data=js_data['trans_result'][0]['dst']
    return(data)
class Server:
    def __init__(self,host='127.0.0.1',port=51110):
        self.host=host
        self.port=port
        self.server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind((self.host,self.port))
        self.server.listen()
        self.client=[]
    def broadcast(self,msg):
        for client in self.client:
            client.send(str(msg).encode("utf-8"))
    def receive(self):
        while True:
            client,address=self.server.accept()
            print(f"connected with {str(address)}")
            self.client.append(client)
            thread=threading.Thread(target=self.handle,args=(client,))
            thread.start()
    def handle(self,client):
        while True:
            try:
                message=client.recv(1024).decode("gbk")
                print(message)
                translated_text=translate_text(message)
                self.broadcast(translated_text)
                print(self.client)
            except:
                break
server=Server()
server.receive()

        
    