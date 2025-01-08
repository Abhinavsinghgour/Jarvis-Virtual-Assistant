import multiprocessing
# To run Jarvis
def startJarvis():
        # Code for process 1 __GUI __
        print("Process 1 is running.")
        from main import start
        start()
# To run hotword
def listenHotword():
        # Code for process 2 __BACKEND __
        print("Process 2 is running.")
        from engine.features import hotword
        hotword()
    # Start both processes
if __name__ == '__main__':
        p1 = multiprocessing.Process(target=startJarvis)
        p2 = multiprocessing.Process(target=listenHotword)
        #p1 and p2 start simultaneously using multi-threading
        p1.start()
        p2.start()
        p1.join() #Stops process1
        if p2.is_alive():
            p2.terminate()
            p2.join() #Stops process2
        print("system stop")   