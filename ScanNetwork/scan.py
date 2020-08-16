import subprocess

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
  for i in range(64,101):
    resp = checkIp(i)

    if resp != connected[i]:
      connected[i] = resp
      name = names.get(i)
      if resp:
          print("ping to " + str(name) + " OK")
      else:
          print("ping to " + str(name) + "failed!")




