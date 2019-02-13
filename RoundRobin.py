def takeSecond(e):
    return e[1]


def check(atbt):
    for i in range(len(atbt)):
        if atbt[i][2] != 0:
            return 1
    return 0


def search(atbt, l, i):
    for j in range(l):
        if atbt[j][0] == i:
            return j


def rr(atbt, tq):
    atbt.sort(key=takeSecond)  # sorting according to at
    l = len(atbt)
    # v = []  visited array
    q = [atbt[0][0]]
    v = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # visiting first element in sorted array
    gc = []
    totalbt = 0
    i = 0
    while(check(atbt)):
        flag = 1
        index = search(atbt, l, q[i])
        temp = tq
        if atbt[index][2] <= tq:
            tq = atbt[index][2]
            flag = 0
        for j in range(l):
            if v[j] == 0 and atbt[j][1] > totalbt and atbt[j][1] <= (totalbt + tq):
                q.append(atbt[j][0])
                v[j] = 1
        if flag == 1:
            q.append(q[i])
        totalbt += tq
        atbt[index][2] -= tq
        gc.append([q[i], totalbt])
        tq = temp
        i += 1
    print(q)
    print(gc)

#[process number,arrival time,burst time]
atbt = [[1, 1, 21], [2, 2, 3], [3, 3, 6], [4, 4, 2]]
tq = 5


rr(atbt, tq)
