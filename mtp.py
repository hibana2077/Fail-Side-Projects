import multiprocessing as mp

def task(num):#100-->10000000000000000000000
    for t in range(100000):print('This is Process: ', num)

if __name__=='__main__':
    num_process = mp.cpu_count()
    process_list = []
    for i in range(num_process):
        process_list.append(mp.Process(target = task, args = (i,)))
        process_list[i].start()

    for i in range(num_process):
        process_list[i].join()
'''
我到底幹嘛寫這個==
'''