import socket 
import sys
import threading
import string
import json
import os
import cherrypy


#Exo 1 : connect to ecam with port 80

""" Examples """
print ( socket . getfqdn ("www.google.be"))         # Fully Qualified Domain Name
print ( socket . gethostname ())                    # Nom d’hôte de la machine
print ( socket . gethostbyname ("www.google.be"))   # Hôte à partir du nom

""" connecting """
s = socket.socket()     #socket.AF_INET6, socket.SOCK_DGRAM
s.connect(('www.google.be',80))
print(s.getsockname())

""" working :"""
data = "GET / HTTP/1.0\n\n".encode()
data = b'GET / HTTP/1.0\n\n'        #other way
sent = s.send(data)
receipt = s.recv(512).decode()
print("receipt",len(receipt), "bytes :")
print(data)

""" not working :"""
s.send(b'GET / HTTP/1.0\n\n' )   #b for encoded in bytes
chunks = []
finnished = False
while not finnished:
    data = s.recv(512)
    chunks.append(data)
    finnished = data == b''
print(b''.join(chunks).decode())        #something not working here

""" closing :"""
s.close()


#Exo 2: create a chat       
""" 
Le serveur permet de mémoriser la liste des clients disponibles pour chatter. Il retient pour
chaque client son pseudo et son adresse IP.

— Au demarrage, Le client va se présenter au serveur, ce qui fait qu’il sera disponible pour chatter.
Il peut interroger le serveur pour obtenir la liste des clients disponibles.

— Ayant l’adresse IP d’une autre machine, une machine peut lancer un chat avec une autre en mode
peer-to-peer, tout cela indépendamment du serveur.
"""

# __running un bbooleen pour indiquer si ca tourne 
# __address pour avoir l'addresse du destinataire
# __s : le socket

class Chat:
    def __init__(self, host="0.0.0.0", port=5000):
        s = socket.socket(type=socket.SOCK_DGRAM)
        s.settimeout(0.5)
        s.bind((host, port))
        self.__s = s
        print('Écoute sur {}:{}'.format(host, port))
        
    def run(self):
        handlers = {
            '/exit': self._exit,
            '/quit': self._quit,
            '/join': self._join,
            '/send': self._send
        }
        self.__running = True
        self.__address = None
        threading.Thread(target=self._receive).start()
        while self.__running:
            line = sys.stdin.readline().rstrip() + ' '
            # Extract the command and the param
            command = line[:line.index(' ')]
            param = line[line.index(' ')+1:].rstrip()
            # Call the command handler
            if command in handlers:
                try:
                    handlers[command]() if param == '' else handlers[command](param)
                except:
                    print("Erreur lors de l'exécution de la commande.")
            else:
                print('Command inconnue:', command)
    
    def _exit(self):
        self.__running = False
        self.__address = None
        self.__s.close()
    
    def _quit(self):
        self.__address = None
    
    def _join(self, param):
        tokens = param.split(' ')
        if len(tokens) == 2:
            try:
                self.__address = (tokens[0], int(tokens[1]))
                print('Connecté à {}:{}'.format(*self.__address))
            except OSError:
                print("Erreur lors de l'envoi du message.")
    
    def _send(self, param):
        if self.__address is not None:
            try:
                message = param.encode()
                totalsent = 0
                while totalsent < len(message):
                    sent = self.__s.sendto(message[totalsent:], self.__address)
                    totalsent += sent
            except OSError:
                print('Erreur lors de la réception du message.')
    
    def _receive(self):
        while self.__running:
            try:
                data, address = self.__s.recvfrom(1024)
                print("[{}] {}".format(address, data.decode()))
            except socket.timeout:
                pass
            except OSError:
                return

if __name__ == '__main__':
    if len(sys.argv) == 3:
        Chat(sys.argv[1], int(sys.argv[2])).run()
    elif len(sys.argv) == 2:
        Chat(port=int(sys.argv[1])).run()
    else:
        Chat().run()

#Exo 3 : cherrypy
import webbrowser


print(socket.gethostbyname(socket.gethostname()))
class WebApp():
    @cherrypy.expose
    def index(self):
        return '<b>YYOOOOOOOOOOOOOOOOOOOOOO<b>!'

site = "http://localhost:8080"
webbrowser.open(site)
print('browser started !')


cherrypy.server.socket_host = "0.0.0.0"
cherrypy.quickstart(WebApp())


""" Pour se connecter depuis un autre pc : ipadress:8080"""