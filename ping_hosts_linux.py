import socket
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
os.system('cls')

#should I promp to point to the file name?
print('Loading the contents of "hosts.txt" file...')

f = open ("hosts.txt")

for line in f:
    HOST = line.strip()
    rep = os.system('ping -c 4' + HOST)
    if rep == 0:
        print ("server is up" ,HOST)
    else:
        print ("server is down" ,HOST)
print("Ping of the hosts has completed")
