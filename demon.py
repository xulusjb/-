#!/usr/bin/python
import psutil
import time
import os
while 1==1:
    pythonnum = 0

    pids = psutil.pids()
    for pid in pids:
        pname = psutil.Process(pid).name()
        if pname=="python":
            pythonnum += 1
    if pythonnum != 2:
        os.system('python /usr/local/shadowsocks/server.py -c /etc/shadowsocks.json -d start')


    time.sleep(10)
