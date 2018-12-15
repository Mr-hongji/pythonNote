# -*- coding:utf-8 -*-
''''''


'''

聊天室

'''

import socket,time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
userSock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sendAddress = ('127.0.0.1',8080)
recAddress = ('',8899)

userSock1.bind(recAddress)

while True:

    sendMsg = raw_input('Input Msg：')

    userSock1.sendto(sendMsg.encode('utf-8'), sendAddress)

    user1RecMsg = userSock1.recvfrom(1024)

    print('%s : %s' % (time.ctime(), user1RecMsg))


userSock1.close()