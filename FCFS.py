print("Enter the number of processes: ")
n = int(input())

processes = []
for i in range(n):
    process = [i+1, 0, 0] # initialize with process number, arrival time, and burst time
    print("Enter Arrival time & burst time for process", i+1)
    process[1] = int(input())
    process[2] = int(input())
    processes.append(process)

# FCFS algorithm
w1 = [0] * n # initialize with 0
t1 = []
sum = 0
for i in range(n):
    sum = max(sum, processes[i][1]) # calculate the actual completion time of the previous process
    w1[i] = sum - processes[i][1]
    sum += processes[i][2]
    t1.append(sum - processes[i][1])

avgw1 = sum(w1) / n
avgt1 = sum(t1) / n

print("\nFCFS")
for i in range(n):
    print("Process", processes[i][0], "WT =", w1[i], "TAT =", t1[i]+w1[i])
print("AWT =", round(avgw1, 2))
print("ATAT =", round(avgt1, 2))
