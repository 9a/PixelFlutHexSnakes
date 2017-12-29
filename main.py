# 171229 joo
# github.com/a9
# thingiverse.com/joo
#
# hexsnakes for pixelflut
# 34C3
#
# code base from standard python example for pixelflut
# python 2.7.11

import socket
import time
import random

HOST = '151.217.47.77'
PORT = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
send = sock.send

def pixel(x, y, r, g, b, a=255):
    global sock
    try:
        if a == 255:
            send('PX %d %d %02x%02x%02x\n' % (x, y, r, g, b))
            #print('PX %d %d %02x%02x%02x\n' % (x, y, r, g, b))
        else:
            send('PX %d %d %02x%02x%02x%02x\n' % (x, y, r, g, b, a))
            #print('PX %d %d %02x%02x%02x%02x\n' % (x, y, r, g, b, a))
    except:
        # Serverrestart doesn't work right now
        print("new socket")
        sock.shutdown(1)
        sock.close()
        time.sleep(1)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))

def rect(x,y,w,h,r,g,b):
  for i in xrange(x,x+w):
    for j in xrange(y,y+h):
      pixel(i,j,r,g,b)

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

class Hexsnake():
    def __init__(self):
        self.x = 400
        self.y = 200
        self.direction = 0
        self.dist = 18
        self.width = 12
        self.red = random.random()*255
        self.green  = random.random()*255
        self.blue  = random.random()*255

    def run(self):
        offsx = [0, 2,  2, 0, -2, -2]
        offsy = [3, 1, -1, -3, -1, 1]

        self.direction = (self.direction + random.randint(-1, 1)) % len(offsx)

        for i in range(self.dist):
            self.x += offsx[self.direction]
            self.y += offsy[self.direction]

            self.x = clamp(self.x, 20, 750)
            self.y = clamp(self.y, 20, 550)

            rect(self.x, self.y, self.width, self.width/2, self.red, self.green, self.blue)
            rect(self.x, self.y+self.width/2, self.width, self.width/2, self.red/2, self.green/2, self.blue/2)

hexsnake = Hexsnake()

def loopit():
    while True:
        hexsnake.run()

loopit()
