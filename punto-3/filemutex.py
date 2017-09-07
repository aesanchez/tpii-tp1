import time
import os.path

def mutexP(filename):
    print "Entre a P"
    while os.path.isfile(filename+".lock"):
        while os.path.isfile(filename+".lock"):
            time.sleep(0.001)
    f_lock = open(filename+".lock","w")
    print "- P"
    f_lock.close()
    return

def mutexV(filename):
    print "Entre a V"
    os.remove(filename+".lock")
    return