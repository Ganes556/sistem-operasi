# proses = [ "P" + str(i) for i in range(int(input("jumlah proses : ")))]
# burst =  [ int(i) for i in input("Burst : ").split(",")]
# arrival = [ int(i) for i in input("Arrival : ").split(",")]
from functools import reduce
import getPriority


proses = ["p1","p2","p3","p4"]
burst = [12,10,15,7]
arrival = [0,5,5,8]
priority = [3,2,1,2]


# print(getPriority.getPriority(priority))
# exit()
arrivalCopy = arrival.copy()
firstArrived = min(arrivalCopy)

ganttChart = []


checkBurst =0
indexBefore =0

round2 = 0


urutanProses = []
urutanArival = []

first = getPriority.getPriority(arrival)

for i in range(len(proses)):
    
    # first = arrival.index(firstArrived)
    # print(arrivalCopy)n
    # exit()
    try:        
        if checkBurst == 0: 
            # ganttChart.append([proses[first],arrival[first],burst[first],priority[first]]) 
            ganttChart.append([proses[first[i]],arrival[first[i]],burst[first[i]],priority[first[i]]]) 
            urutanProses.append(ganttChart[0][0])
            urutanArival.append(ganttChart[0][1])
        else:
            if checkBurst > arrival[first[i]]:
                
                indexPriorityFirsts = getPriority.getPriority([x[3] for x in ganttChart]) 
                
                
                # ganttChart[indexPriorityFirsts][2] -= (arrival[first]-arrival[indexBefore])                
                ganttChart[indexPriorityFirsts[0]][2] -= (arrival[first[i]]-arrival[indexBefore])                

                ganttChart.append([proses[first[i]],arrival[first[i]],burst[first[i]],priority[first[i]]]) 
                # print(ganttChart,first,arrivalCopy)
                
                
        checkBurst = burst[first[i]]
        indexBefore = first[i] if i ==0 else first[i-1]
                
                
        # arrivalCopy.remove(firstArrived)
        # firstArrived = min(arrivalCopy)
        
        
    except Exception as e:                 
        
        round2 = 1
        # print(getPriority.getPriority([x[3] for x in ganttChart]))
        pass 

    get = getPriority.checkNull(ganttChart)
    ganttChart = get[0]
    
    try : 
        urutanProses.append(get[1][0][0])
        urutanArival.append(get[1][0][1])
    except Exception:        
        pass
    
    # print("arrival ke-" + str(arrival[i]),ganttChart)       
    exit(print(ganttChart))
    if round2 :        
                     
        # indexPriorityFirsts = getPriority.getPriority([x[3] for x in ganttChart])
        indexPriorityFirsts = getPriority.getPriority([x[3] for x in ganttChart])[0]
        # print(indexPriorityFirsts)

        proses2 = ganttChart[indexPriorityFirsts][0]
        arrival2 = ganttChart[indexPriorityFirsts][1]
        burst2 = ganttChart[indexPriorityFirsts][2]
        priority2 = ganttChart[indexPriorityFirsts][3]        
        
        arrivalRound2 = arrival[-1]
        for z in range(len(ganttChart)):
            # indexPriorityFirsts = getPriority.getPriority([x[3] for x in ganttChart])
            indexPriorityFirsts = getPriority.getPriority([x[3] for x in ganttChart])[0]
            proses2 = ganttChart[indexPriorityFirsts][0]
            arrival2 = ganttChart[indexPriorityFirsts][1]
            burst2 = ganttChart[indexPriorityFirsts][2]
            priority2 = ganttChart[indexPriorityFirsts][3]
            
            ganttChart.pop(indexPriorityFirsts)
            ganttChart.append([proses2,arrival2,0,priority2])

            get = getPriority.checkNull(ganttChart)
            ganttChart = get[0]

            urutanProses.append(get[1][0][0])
            urutanArival.append(arrivalRound2)
            arrivalRound2 += burst2

            # print(ganttChart, get[1][0][0])

# exit()
a = reduce(lambda x,y : x+y, urutanArival)
b = []

print("Proses ganttchart -> " + str(urutanProses))
print("Arrival ganttchart -> " + str(urutanArival))
for i in set(urutanProses):
    if arrival[proses.index(i)] == min(arrival):  
        getArrival = arrival[proses.index(i)+1]
    else:
        getArrival = arrival[proses.index(i)]
    b.append(getArrival)    

awt = (a - reduce(lambda x,y: x+y, b))/len(proses)
print("AWT -> " + str(awt))