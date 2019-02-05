class Process:
    def __init__(self, ID, AT, BT):
        self.id      = ID
        self.arrival = AT
        self.burst   = BT
        self.execute = 0
        self.close   = None
    
    def process(self, T):
        if self.execute < self.burst:
            self.execute = self.execute+1
            return True
        elif self.execute == self.burst:
            self.close = T
            return False


def sort(POOL):
    return sorted(POOL, key=lambda x:x.arrival, reverse=False)


def simulate(POOL):
    time = 0
    POOL = sort(POOL)
    for proc in POOL:
        while(proc.process(time)):
            time = time+1


if __name__ == '__main__':
    time = 0;
    t_proc = int(input("Total number of process : "))
    pool = list[]
    for proc_id in range(t_proc):
        at, bt = input().split(" ")
        proc = Process(ID, int(at), int(bt))
        pool.append(proc)
    simuate(pool)
