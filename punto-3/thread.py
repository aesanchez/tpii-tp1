import sys
sys.path.insert(0, './util')
import threading
import time
import os.path
from random import randint
from filemutex import mutexP
from filemutex import mutexV

def worker(count, t_muestreo, filename):
    cant_muestras = 1
    while cant_muestras < 4:
        temp = randint(0, 90)
        humedad = randint(0, 90)
        presion = randint(0, 90)
        v_viento = randint (0, 90)
        time.sleep(t_muestreo)
        cant_muestras = cant_muestras + 1
        mutexP(filename)
        file = open(filename, "a")
        time.sleep(2)
        file.write("{}-{}|{}|{}|{}\n".format(count, temp,humedad,presion,v_viento))
        file.close()
        mutexV(filename)
    return

threads = list()

for i in range(1):
    t = threading.Thread(target=worker, args=(i, 0.001, sys.argv[1],))
    threads.append(t)
    t.start()