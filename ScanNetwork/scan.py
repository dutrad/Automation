import subprocess
import datetime
import sys

IP_NETWORK = '192.168.1.'


def checkIp(ip):
    ip = IP_NETWORK + str(ip)
    out = subprocess.call(['ping', '-c', '3', ip], stdout=subprocess.DEVNULL)

    return out == 0


def getnames():
    d = {}
    file = sys.argv[1]
    with open(file) as f:
        for line in f:
            (key, val) = line.split()
            d[int(key)] = val
    return d


names = getnames()
connected = [False] * 90
fileName = sys.argv[2]

for i in range(64, 90):
    connected[i] = checkIp(i)

while True:
    for i in range(64, 90):
        resp = checkIp(i)

        if resp != connected[i]:
            connected[i] = resp
            name = names.get(i)
            msg = ""
            now = datetime.datetime.now()
            if not name:
                name = i
            if resp:
                msg = now.strftime("%c") + " " + str(name) + " online\n"
            else:
                msg = now.strftime("%d/%m/%Y %H:%M:%S") + " " + str(name) + " offline\n"

            with open(fileName, 'a+') as outFile:
                outFile.write(msg)
