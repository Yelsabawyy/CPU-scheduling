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

p_no = [i[0] for i in p]  # process number
at = [i[1] for i in p]  # arrival time
bt = [i[2] for i in p]  # burst time

################ SJF

def swap_positions(lst, pos1, pos2):
    get = lst[pos1], lst[pos2]
    lst[pos2], lst[pos1] = get

p_no1 = p_no[1:]
at1 = at[1:]
bt1 = bt[1:]

p_no1_new = [p_no[0]]
at1_new = [at[0]]
bt1_new = [bt[0]]

total_burst_time = bt[0]

def correct_positions(p_no1, at1, bt1, p_no1_new, at1_new, bt1_new, total_burst_time):
    if at1[i] >= total_burst_time:
        p_no1_new.append(p_no1[i])
        at1_new.append(at1[i])
        bt1_new.append(bt1[i])
        total_burst_time += bt1[i]
    else:
        temp = [[0, 0, 0]]  # initial values for temp 0,0,0
        counter = i
        try:
            while at1[counter] < total_burst_time:
                temp.append([p_no1[counter], at1[counter], bt1[counter]])
                counter += 1
        except IndexError:
            temp.pop(0)
        else:
            temp.pop(0)

        first_process_no = temp[0][0]
        first_arrival_time = temp[0][1]
        first_burst_time = temp[0][2]

        if len(temp) > 1:
            temp.sort(key=lambda x: x[2])  # sort according to burst time
            smallest_burst_process_no, smallest_burst_arrival_time, smallest_burst_time = temp[0]

            pos1 = p_no1.index(first_process_no)
            pos2 = p_no1.index(smallest_burst_process_no)

            pos3 = at1.index(first_arrival_time)
            pos4 = at1.index(smallest_burst_arrival_time)

            pos5 = bt1.index(first_burst_time)
            pos6 = bt1
