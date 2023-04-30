import statistics as s

print("Enter the number of processes: ")
n=int(input())

p=[]
for i in range(0,n):
    p.append([])
    for j in range(0,3):
        p[i].append(j)
        if j==0 :p[i][j]=i+1
        else: p[i][j]=0

print("Enter Arrival time & burst time: ")
for i in range(0,n):
    for j in range(1,3):
        p[i][j]=int(input())

p_no =[i[0] for i in p] #process number
at =[i[1] for i in p] #arrival time
bt =[i[2] for i in p] #burst time

################################################################
#####SJRF

at_1=at[:n]
time=[0]

for i in range(n):

    process=[]
    for j in range(n):
        if at[j]<=time[-1]:
            process.append([j,at[j],bt[j]])

    process.sort(key=lambda x: x[2])

    if process:
        k=process[0][0]

        while process[0][2]!=0:
            time[-1]+=1
            process[0][2]-=1

            if k!=process[0][0]:
                break

        if process[0][2]==0:
            time.append(time[-1])
        else:
            process.sort(key=lambda x: x[2])
            time.append(time[-1])

    else:
        time.append(time[-1]+1)

del time[0]
print (time)

wt3=[time[i]-at[i]-bt[i] for i in range(n)]
print (wt3)

tat3=[wt3[i]+bt[i] for i in range(n)]
print (tat3)

print ("")
print ("SJRF")
for i in range (n):
    print ("process",i+1,"  WT =",wt3[i],"TRT =",tat3[i])

print("AWT=",round(s.mean(wt3), 2))
print("ATRT=",round(s.mean(tat3), 2))
