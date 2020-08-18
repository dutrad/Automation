import subprocess
import datetime

IP_NETWORK = '192.168.1.'

def checkIp(ip):
  ip = IP_NETWORK + str(ip)
  resp = subprocess.call(['ping', '-c', '1', ip], stdout=subprocess.DEVNULL)

  return (resp == 0)

def getNames():
  d = {}
  with open("ips.txt") as f:
    for line in f:
      (key, val) = line.split()
      d[int(key)] = val
  return d

names = getNames()
connected = [False] * 100

while True:
  for i in range(64,100):
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

      with open('out.txt', 'a+') as file:
          file.write(msg)








