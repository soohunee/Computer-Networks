#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 15:34:39 2021

@author: soohun
"""

from socket import *
serverIP = '192.168.35.148'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))

msg = input('Input lowercase sentence : ')
clientSocket.send(msg.encode())

newMsg = clientSocket.recv(1024)
print('From Server : ', newMsg.decode())
clientSocket.close()