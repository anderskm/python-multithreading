from random import random
import sys
import threading
import time

def ox():
    print(max([random() for x in range(20000000)]))

def go():
    r = threading.Thread(target=ox)
    r.start()
    ox()


print("Python version:")
print(sys.version)

print("Single thread - sequential execution:")
start_time_single_thread = time.time()
ox()
ox()

print("--- %s seconds ---" % (time.time() - start_time_single_thread))


print("Two threads - 'parallel' execution:")
start_time_multi_thread = time.time()
go()

print("--- %s seconds ---" % (time.time() - start_time_multi_thread))
