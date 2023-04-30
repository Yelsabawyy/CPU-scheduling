import statistics as s

print("Enter the number of processes: ")
n = int(input())

p = []
for i in range(0, n):
    p.append([])
    for j in range(0, 3):
        p[i].append(j)
        if j == 0:
            p[i][j] = i
        else:
            p[i][j] = 0

print("Enter Arrival time & burst time: ")
for i in range(0, n):
    for j in range(1, 3):
        p[i][j] = int(input())

p_no = [] #process number
at = [] #arrival time
bt = [] #burst time
for i in p:
    p_no.append(i[0])
    at.append(i[1])
    bt.append(i[2])

print("Enter quantum time: ")
q = int(input())

last = [0]
for i in range(len(at)):
    que = [[0, 0, 0]]
    for n in range(len(at)):
        que.append([n, at[n], bt[n]])
    del que[0]

    total_time = 0
    k = i

    for j in range(100):

        if que[j][2] > q:
            total_time += q
            que.append([que[j][0], total_time, que[j][2] - q])
            que.sort(key=lambda x: x[1])

        else:
            total_time += que[j][2]

            if k == que[j][0]:
                last.append(total_time)
                break

w4, t4 = [0], [0]
for i in range(len(at)):
    w4.append(last[i] - at[i] - bt[i])
del w4[0]

for i in range(len(at)):
    t4.append(w4[i] + bt[i])
del t4[0]

print("")
print("RR")
for i in range(n):
    print("process", i+1, "  WT =", w4[i], "TRT =", t4[i])

print("AWT =", round(s.mean(w4), 2))
print("ATRT =", round(s.mean(t4), 2))
