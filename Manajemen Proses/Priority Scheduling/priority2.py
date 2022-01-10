from functools import reduce
import getPriority

proses = [ "P" + str(i) for i in range(int(input("jumlah proses : ")))]
burst =  [ int(i) for i in input("Burst : ").split(",")]
arrival = [ int(i) for i in input("Arrival : ").split(",")]
priority = [ int(i) for i in input("Priority : ").split(",")]

arrivalCopy = arrival.copy()
firstArrived = min(arrivalCopy)

ganttChart = []

checkBurst =0
indexBefore =0

urutanProses = []
turn = []

first = getPriority.getPriority(arrival)

for i in range(len(proses)):
        
    indexBefore = first[i] if i ==0 else first[i-1]
    if checkBurst == 0: 
        ganttChart.append([proses[first[i]],arrival[first[i]],burst[first[i]],priority[first[i]]])         
    else:
        if checkBurst > arrival[first[i]]:
            
            indexPriorityFirsts = getPriority.getPriority([x[3] for x in ganttChart]) 
                                      
            ganttChart.append([proses[first[i]],arrival[first[i]],burst[first[i]],priority[first[i]]]) 

            ganttChart[indexPriorityFirsts[0]][2] -= (arrival[first[i]]-arrival[indexBefore])            

            urutanProses.append(proses[indexPriorityFirsts[0]])
        
    checkBurst = burst[first[i]]
            
    get = getPriority.checkNull(ganttChart)
    ganttChart = get[0]        
  
    
    if i == len(proses)-1 :        

        indexPriorityFirsts = getPriority.getPriority([x[3] for x in ganttChart])[0]
        
        proses2 = ganttChart[indexPriorityFirsts][0]
        arrival2 = ganttChart[indexPriorityFirsts][1]
        burst2 = ganttChart[indexPriorityFirsts][2]
        priority2 = ganttChart[indexPriorityFirsts][3]        

        arrivalRound2 = arrival[-1]    
        for z in range(len(ganttChart)):

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
            arrivalRound2 += burst2
            turn.append(arrivalRound2)
            

urutanArival = sorted(arrival + turn)


a = {}
b = {}

temp = ""

for i,j in zip(urutanProses,urutanArival):
    if i == temp:        
        pass
    else:
        a[i]= j
        if arrival[proses.index(i)] == min(arrival):  
            b[i]= arrival[proses.index(i)+1] 
        else:
            b[i]= arrival[proses.index(i)]
    temp = i    

a = reduce(lambda x,y : x+y,[x for x in a.values()])
b = reduce(lambda x,y: x+y,[x for x in b.values()])
print("AWT -> " + str((a-b)/len(proses)))