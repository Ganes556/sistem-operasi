# proses = input("proses = ").split(",")
# burst = [ int(i) for i in input("burst = ").split(",")]
# arrival = [ int(i) for i in input("arrival = ").split(",")]
# priority = [ int(i) for i in input("priority = ").split(",")]

# dictPro = { proses[i] : {"burst": burst[i], "arrival": arrival[i], "priority":priority[i]}  for i in range(len(proses))}
proses = ["p1","p2","p3","p4"]
burst = [10,8,12,6]
arrival = [0,3,5,11]
priority = [2,1,3,2]
dictPro = {'p1': {'burst': 10, 'arrival': 0, 'priority': 2}, 
'p2': {'burst': 8, 'arrival': 3, 'priority': 1}, 
'p3': {'burst': 12, 'arrival': 5, 'priority': 3}, 
'p4': {'burst': 6, 'arrival': 11, 'priority': 2}}


minVal = min(arrival)

ganttChart = {}



temp = 0
temp2 = 0

# while 1:

for i in proses:
    if dictPro[i]["arrival"] == minVal:
        # ganttChart. {minVal: {i : j for i,j in dictPro.items() if j["arrival"] == minVal} }
        if ganttChart == {}:
            temp2 += 1
            ganttChart[dictPro[i]["arrival"]] = {i:{"burst" : dictPro[i]["burst"], "priority":dictPro[i]["priority"]}}
        else:                
            arrivalKeySebelum = list(ganttChart)[temp2-1]            

            ganttChartBaru = {i:{"burst" : dictPro[i]["burst"], "priority":dictPro[i]["priority"]}}
            if dictPro[i]["burst"] > minVal: 
                # getGanttchartPiority = [z for z in ganttChart[arrivalKeySebelum] if z["priority"] == priorityFirst]
                # priorityFirst = [z for z in ganttChart[arrivalKeySebelum]]
                # print(priorityFirst)
                try:
                    indexFirst = []
                    
                    keyFirst = []
                    burstFirst = []
                    # mins = min([j for i in ganttChart[arrivalKeySebelum] for j in i])
                    # for i in ganttChart[arrivalKeySebelum]:
                    gabungan = ganttChart[arrivalKeySebelum] + [ganttChartBaru] 
                    ganttChart[dictPro[i]["arrival"]] = gabungan

                    arrivalKeySaatIni = list(ganttChart)[temp2]
                    
                    priorityFirst = min([j["priority"] for i in ganttChart[arrivalKeySaatIni] for j in i.values()])
                    ganttChartSaatIni = ganttChart[arrivalKeySaatIni]
                    
                    

                    for z in range(len(ganttChartSaatIni)):
                        for o,h in ganttChartSaatIni[z].items():  
                            
                            if h["priority"] == priorityFirst:
                                indexFirst.append(z)
                                keyFirst.append(o)
                                burstFirst.append(h["burst"])
                    # print(arrivalKeySaatIni)
                    # print(ganttChart[arrivalKeySaatIni][indexFirst[0]][keyFirst[0]]["burst"])
                    # exit()
                    if len(indexFirst) > 1:
                        pass
                        # ganttChart[arrivalKeySaatIni][0][list(ganttChart[arrivalKeySaatIni][0].keys())[0]]["burst"] -= minVal                                       
                    else:
                        
                        ganttCopy = ganttChart.copy()
                        
                        # .update({"burst":burst[0]-(minVal-temp)})                         
                        ganttCopy[5][1]["p2"]["burst"] = burstFirst[0]-(minVal-temp)                        
                        # print(ganttCopy,indexFirst,keyFirst)
                        exit()
                        # indexFirst.clear()
                        # keyFirst.clear()
                        
                        
                        
                    # print(list(ganttChart)[temp2])

                except Exception:  
                    ganttChart[dictPro[i]["arrival"]] = [ganttChart[arrivalKeySebelum],ganttChartBaru]
                    arrivalKeySaatIni = list(ganttChart)[temp2]
                                        

                    
            else:
                ganttChart[dictPro[i]["arrival"]] = ganttChart[arrivalKeySebelum] + [ganttChartBaru]
            temp2 += 1
        temp = minVal
        arrival.remove(minVal)    
    try: 
        minVal = min(arrival)    
    except Exception:
        pass
# print(ganttChart)
# for i in ganttChart.values():
#     print(i)

