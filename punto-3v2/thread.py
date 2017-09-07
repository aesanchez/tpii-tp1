import sys
import threading
import time
import os.path
from random import randint
from filemutex import mutexP
from filemutex import mutexV

def worker(count, t_muestreo, filename):
    cant_muestras = 1
    p_temp = 0
    p_humedad = 0
    p_presion = 0
    p_viento = 0
    """La a es para que se escriba al final del archivo"""
    while cant_muestras < 4:
        temp = randint(0, 90)
        humedad = randint(0, 90)
        presion = randint(0, 90)
        v_viento = randint (0, 90)
        p_temp = (p_temp + temp)/cant_muestras
        p_humedad = (p_humedad + humedad)/cant_muestras
        p_presion = (p_presion + presion)/cant_muestras
        p_viento = (p_viento + v_viento)/cant_muestras
        time.sleep(t_muestreo)
        cant_muestras = cant_muestras + 1
        mutexP(filename)
        file = open(filename+".txt", "a")
        time.sleep(2)
        print "me duermo (t={}) {} seg .. promedio temp = {}".format(count, t_muestreo, p_temp)
        file.write("{}-{}|{}|{}|{}\n".format(count, temp,humedad,presion,v_viento))
        file.close()
        mutexV(filename)
    return

threads = list()

for i in range(3):
    print sys.argv[1]
    t = threading.Thread(target=worker, args=(i, 0.001, sys.argv[1],))
    threads.append(t)
    t.start()