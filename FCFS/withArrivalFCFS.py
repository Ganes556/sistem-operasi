# proses = [ "P" + str(i) for i in range(int(input("jumlah proses : ")))]
arrival = [int(i) for i in input("Arrival : ").split(",")]
burst = [int(i) for i in input("Burst : ").split(",")]

proses = len(arrival)

if proses != len(burst):
    print("Panjang arrival tidak sama dengan burst")
    exit()


arrivalCopy = arrival.copy()
firstArrived = min(arrivalCopy)

ganttChart = []
wt = min(arrival)

for i in range(len(proses)):

    first = arrival.index(firstArrived)
    try:
        # (process,wt)
        ganttChart.append((proses[first], wt))
        wt += burst[first]

        arrivalCopy.remove(firstArrived)

        firstArrived = min(arrivalCopy)

    except Exception:
        # if len(arrivalCopy) == 0:
        #     ganttChart.append((proses[first],wt))
        pass

count = 0
for i in range(0, len(ganttChart)):
    count += ganttChart[i][1] - arrival[proses.index(ganttChart[i][0])]

print(count / len(proses))
