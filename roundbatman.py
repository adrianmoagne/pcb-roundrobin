
from datetime import datetime

from pcb import Pcb


process_queueu = [[Pcb('Adrian',1,1,datetime.now().strftime("%H:%M:%S"),0,10),Pcb('Moagne',2,2,'agora',1,15),Pcb('Nery',3,3,'agora',3,5)],[Pcb('Carvalho',4,4,'agora',5,7)]]



def round(process_queueu,quantum):
    t = 0
    for i in range(len(process_queueu)):
        process_queueu[i].sort(key = lambda x : x.prior, reverse = True)
        remain_burst_time =[0] * len(process_queueu[i])
        for j in range(len(process_queueu[i])):
            remain_burst_time[j] = process_queueu[i][j].burst_time

        

        while(True):
            done = True
            for k in range(len(process_queueu[i])):
                print(remain_burst_time[k])
                if remain_burst_time[k] > 0:
                    done = False

                    if remain_burst_time[k] > quantum:
                        t+= quantum
                        remain_burst_time[k] -= quantum
                    else:
                        t+=remain_burst_time[k]
                        process_queueu[i][k].wating_time = t -  process_queueu[i][k].burst_time
                        process_queueu[i][k].turn_around_time= process_queueu[i][k].wating_time +  process_queueu[i][k].burst_time
                        remain_burst_time[k] = 0

            if done is True:
                break

round(process_queueu=process_queueu, quantum=5)

for i in range(len(process_queueu)):
    for x in range(len(process_queueu[i])):
        print('Waiting Time :' ,process_queueu[i][x].wating_time, 'Turn Around time: ',process_queueu[i][x].turn_around_time)


print(process_queueu[0][2].data_hour)

