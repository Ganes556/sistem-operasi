proses = [ "P" + str(i) for i in range(int(input("jumlah proses : ")))]
burst =  [ int(i) for i in input("Burst : ").split(",")]
arrival = [ int(i) for i in input("Arrival : ").split(",")]

arrivalCopy = arrival.copy()
firstArrived = min(arrivalCopy)

ganttChart = []
wt = min(arrival)
temp = 0
for i in range(len(proses)):
    
    first = arrival.index(firstArrived)    
    try:
        # (process,wt)        
        ganttChart.append((proses[first],wt)) 
        wt += burst[first]
                
        arrivalCopy.remove(firstArrived)
        temp = firstArrived
        firstArrived = min(arrivalCopy)
        
    except Exception:      
        # if len(arrivalCopy) == 0:
        #     ganttChart.append((proses[first],wt))        
        pass 

count = 0
for i in range(0,len(ganttChart)):         
    count += ganttChart[i][1]-arrival[proses.index(ganttChart[i][0])]    
    
print(count/len(proses))
        

