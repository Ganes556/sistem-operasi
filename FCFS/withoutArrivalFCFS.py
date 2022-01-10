print("FCFS Burst Only")

indexLen = int(input("Banyak Proses: "))

keyFlag = "P"

processDict = {}

for i in range(indexLen):
  key = keyFlag + str(i + 1)
  val = int(input("Burst " + key + ": "))
  processDict[key] = val

chart = []
total = 0
for i in range(indexLen):
  if(i == 0):
    chart.append(0)
  else:
    total += processDict[keyFlag + str(i)]
    chart.append(total)

print("Gantt Chart: " + str(chart))

wt = 0
for i in range(indexLen):
  wt += chart[i]

print("WT: " + str(wt))

awt = wt/indexLen

print("AWT: " + str(awt))

