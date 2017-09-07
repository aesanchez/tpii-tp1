import time
import os.path

def mutexP(filename):
    while os.path.isfile(filename+".lock"):
        while os.path.isfile(filename+".lock"):
            time.sleep(0.001)
    f_lock = open(filename+".lock","w")
    f_lock.close()
    return

def mutexV(filename):
    os.remove(filename+".lock")
    return