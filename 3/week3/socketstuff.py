#import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('www.py4inf.com', 80))
# mysock.send('GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n')
#
# while True:
#     data = mysock.recv(512)
#     if ( len(data) < 1 ) :
#         break
#     print data;
# 
# mysock.close()
import urllib
from bs4 import BeautifulSoup

url = 'http://www.py4inf.com/code/romeo.txt'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
x = soup('a')
print x
