from multiprocessing import Pool

def job(x):
    return 2*x


if __name__=='__main__':

    p = Pool(processes = 20)
    data = p.map(job, [i for i in range(20)])
    p.close()
    print(data)
    
