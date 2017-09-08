import time
from random import randint
from filemutex import mutexP
from filemutex import mutexV
import threading
import os

class Sensores:

    muestreolock = threading.Lock()
    muestreo = 1 #by default
    filename = "data" #by default
    s_thread = None
    s_stop_flag = None

    #por alguna razon hay que pasarle self como argumento a los metodos de las clases
    def start(self, filenamearg, muestreoarg):
        self.filename = filenamearg
        self.muestreo = muestreoarg
        #delete previous file
        if os.path.isfile(self.filename):
            os.remove(self.filename)
        if os.path.isfile(self.filename+".lock"):
            os.remove(self.filename+".lock")
        self.s_stop_flag = threading.Event()
        self.s_thread = threading.Thread(target = self.run)
        self.s_thread.daemon = True  
        self.s_thread.start()
        return

    def change_sampling(self, muestreoarg):
        self.muestreolock.acquire()
        self.muestreo = muestreoarg
        self.muestreolock.release()
        return

    def run(self):
        while (not self.s_stop_flag.is_set()):
            temp = randint(0, 90)
            humedad = randint(0, 90)
            presion = randint(0, 90)
            v_viento = randint (0, 90)
            mutexP(self.filename)
            f = open(self.filename, "a")
            f.write("{}|{}|{}|{}\n".format(temp,humedad,presion,v_viento))
            f.close()
            mutexV(self.filename)            
            self.muestreolock.acquire()
            aux = self.muestreo
            self.muestreolock.release()
            #  es igual a un sleep pero es despertado para que termine
            #  si se le indica que pare con .set()
            self.s_stop_flag.wait(float(aux))            
        return

    def stop(self):
        # thread safe
        self.s_stop_flag.set()
        return