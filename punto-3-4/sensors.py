import time
from random import randint
from filemutex import mutexP
from filemutex import mutexV
from getlastlines import getlastlines
import threading
import os

class Sensores:

    muestreolock = threading.Lock()
    muestreo = 1 #by default
    filename = "data" #by default
    sensors_thread = None
    sensors_stop_flag = None
    cleaner_thread = None
    cleaner_stop_flag = None
    cleaner_run_flag = None
    max_size = 20
    size = 0

    # por alguna razon hay que pasarle self como argumento a los metodos de las clases
    def start(self, filenamearg, muestreoarg):
        self.size = 0
        self.filename = filenamearg
        self.muestreo = muestreoarg
        # delete previous file
        if os.path.isfile(self.filename):
            os.remove(self.filename)
        if os.path.isfile(self.filename+".lock"):
            os.remove(self.filename+".lock")
        # Iniciar thread sensores
        self.sensors_stop_flag = threading.Event()
        self.sensors_thread = threading.Thread(target = self.sensors_run)
        self.sensors_thread.daemon = True
        self.sensors_thread.start()
        # Iniciar thread cleaner
        self.cleaner_stop_flag = threading.Event()
        self.cleaner_run_flag = threading.Event()
        self.cleaner = threading.Thread(target = self.cleaner_run)
        self.cleaner.daemon = True
        self.cleaner.start()
        return

    def change_sampling(self, muestreoarg):
        self.muestreolock.acquire()
        self.muestreo = muestreoarg
        self.muestreolock.release()
        return

    def cleaner_run(self):
        while (not self.cleaner_stop_flag.is_set()):
            # Espera a que lo despierten
            self.cleaner_run_flag.wait()
            # Una vez despertado borra ese evento
            self.cleaner_run_flag.clear()
            # Leo los ultimos datos sensados
            lastcontent = getlastlines(self.filename, int(self.max_size/2))
            # Sobreescribimos el archivo original con los datos mas nuevos
            mutexP(self.filename)
            f = open(self.filename, "w")
            for s in lastcontent:
                f.write(s+"\n")
            f.close()
            # Actualizamos el espacio ocupado a lo que recupero getlastlines
            self.size = len(lastcontent)
            mutexV(self.filename)            
        return

    def sensors_run(self):
        while (not self.sensors_stop_flag.is_set()):
            temp = randint(0, 90)
            humedad = randint(0, 90)
            presion = randint(0, 90)
            v_viento = randint (0, 90)
            mutexP(self.filename)
            f = open(self.filename, "a")
            f.write("{}|{}|{}|{}\n".format(temp,humedad,presion,v_viento))
            f.close()
            # Aprovecho este mutex
            self.size = self.size+1
            if self.size == self.max_size:
                self.cleaner_run_flag.set() 
            mutexV(self.filename)                      
            self.muestreolock.acquire()
            aux = self.muestreo
            self.muestreolock.release()
            #  es igual a un sleep pero es despertado para que termine
            #  si se le indica que pare con .set()
            self.sensors_stop_flag.wait(float(aux))            
        return

    def stop(self):
        # thread safe
        self.sensors_stop_flag.set()
        self.cleaner_stop_flag.set()
        return