def getPriority(priority):    
    prioCopy = priority.copy() 
    indexPriorityFirst = []
    temp = []
    for i in range(len(priority)):
        if len(prioCopy)!=0: 
            minPrio = min(prioCopy)     
            if minPrio in temp:            
                index = priority.index(minPrio,i)
            else:
                index = priority.index(minPrio)

            temp.append(minPrio)
            
            indexPriorityFirst.append(index)
            prioCopy.remove(minPrio)
    # print(indexPriorityFirst)
    return indexPriorityFirst

def checkNull(ganttChart):
    pops = []
    for z in range(len(ganttChart)):
        if ganttChart[z][2] == 0:
            pops.append(ganttChart[z])
            ganttChart.pop(z)
            break

    return ganttChart,pops
