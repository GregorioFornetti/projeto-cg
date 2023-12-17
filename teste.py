from multiprocessing import Process, Queue
from time import sleep

def f(v:int, q: Queue):
    sleep(v)
    q.put(v)

if __name__ == '__main__':
    q = Queue()
    processes: 'list[Process]' = []
    for i in range(10):
        p = Process(target=f, args=(i, q))
        p.start()
        processes.append(p)
    
    for p in processes:
        print('oi')
        p.join()
    for i in range(10):
        print(q.get())