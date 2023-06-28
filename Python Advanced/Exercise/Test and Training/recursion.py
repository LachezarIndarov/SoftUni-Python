import time

def f1():
    print(time.time())
    time.sleep(1)
    f1()

f1()