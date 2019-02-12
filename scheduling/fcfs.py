from functools import reduce


class Process:
    def __init__(self, ID, AT, BT):
        self.id = ID
        self.arrival = AT
        self.burst = BT
        self.execute = 0
        self.close = None

    def process(self, t):
        if self.execute < self.burst:
            self.execute = self.execute + 1
            return True
        elif self.execute == self.burst:
            self.close = t
            return False


def read():
    processes = set()
    n = int(input("Enter total no. of processes: "))
    print("SYNTAX: <AT> <BT>")
    for process_id in range(n):
        print(process_id, ":", end=" ")
        at, bt = map(int, input().split(" "))
        processes.add(Process(process_id, at, bt))
    return processes


def simulate(processes):
    time = 0
    completed = list()
    while processes:
        next_process = reduce(lambda x, y: x if x.arrival < y.arrival else y, processes)
        if next_process.arrival > time:
            time += 1
        elif next_process.process(time):
            time += 1
        else:
            processes.remove(next_process)
            completed.append(next_process)
    for process in completed:
        print(process.id, process.close, sep=" ")


if __name__ == '__main__':
    simulate(read())
    exit()
