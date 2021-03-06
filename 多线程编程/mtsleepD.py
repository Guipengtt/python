#创建Tread实例，传给它一个可调用的类实例

import threading
from time import sleep, ctime

loops = [4, 2]

class TreadFunc(object):
    def __init__(self, func, args, name =''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)


def loop(nloop, nsec):
    print("Start loop", nloop, "at:", ctime())
    sleep(nsec)
    print("loop", nloop, "done at:", ctime())

def main():
    print("Start at:", ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target= TreadFunc(loop, (i, loops[i])))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print("All Done at:", ctime())

if __name__ == '__main__':
    main()
