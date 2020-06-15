
import threading as th
import time

#Exo multiprocessing

def warn (t, msg ):
    def sleeping(t,msg):
        time.sleep(t)
        print(msg)
    t = th.Thread(target=sleeping, args = (t,msg,))
    t.start()

# OR !!! 

def warn1 (t, msg ):
    def sleeping():
        time.sleep(t)
        print(msg)
    th.Thread(target=sleeping).start()
    # t = th.Thread(target=sleeping)    #this gives an error
    # t.start()
    
    
    


warn (2, "Kono giorno Giovanna yume ga arimasu")
warn1 (2, "Kono Dio da !")

for i in range (5) :
    print (i)
    time.sleep (1)