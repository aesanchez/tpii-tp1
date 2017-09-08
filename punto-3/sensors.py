import time
from random import randint
from filemutex import mutexP
from filemutex import mutexV

def run(t_muestreo, filename):
    while 1:
        temp = randint(0, 90)
        humedad = randint(0, 90)
        presion = randint(0, 90)
        v_viento = randint (0, 90)
        time.sleep(t_muestreo)
        mutexP(filename)
        f = open(filename, "a")
        f.write("{}|{}|{}|{}\n".format(temp,humedad,presion,v_viento))
        f.close()
        mutexV(filename)
    return