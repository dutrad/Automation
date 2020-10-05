import subprocess
import datetime
import sys, os

sys.path.append(os.path.join(sys.path[0], "..", "SendEmail"))
from mail import sendMail

IP_NETWORK = '192.168.1.'

def checkIp(ip):
    ip = IP_NETWORK + str(ip)
    out = subprocess.call(['ping', '-c', '3', ip], stdout=subprocess.DEVNULL)

    return out == 0


def getnames():
    d = {}
    l = []
    file = os.path.join(os.path.dirname(__file__), 'ips.txt')
    with open(file) as f:
        for line in f:
            if not line.strip():
                break
            (key, val) = line.split()
            d[int(key)] = val
        
        next(f)
        for line in f:
            l.append(int(line.strip()))

    return [d,l]


[names, ignore] = getnames()
fileName = os.path.join(os.path.join(sys.path[0], 'out.txt'))

ips = {}
for i in range(64, 90):
    if i not in ignore:
        ips[i] = checkIp(i)

while True:
    for ip, conn in ips.items():
        resp = checkIp(ip)

        if resp != conn:
            conn = resp
            name = names.get(i)
            msg = ""
            now = datetime.datetime.now()
            if not name:
                name = i
            if resp:
                msg = now.strftime("%c") + " " + str(name) + " online\n"
                sendMail(str(name) + " is online", msg)
            else:
                msg = now.strftime("%d/%m/%Y %H:%M:%S") + " " + str(name) + " offline\n"

            with open(fileName, 'a+') as outFile:
                outFile.write(msg)
