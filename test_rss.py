#!/usr/bin/python

import socket,json

def send(var,txt):
        HOST = '127.0.0.1'
        PORT = 5679
#        try:
	if True:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((HOST, PORT))
                data = {'text':str(txt),'var':str(var)}
                d = json.dumps(data)
		print(d)
                s.sendall(d)
                data = s.recv(1024)
                s.close()
                return data
#        except:
                return False

send('rss','BLA')

