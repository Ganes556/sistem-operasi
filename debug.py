a= {0: {'p1': {'burst': 10, 'priority': 2}}, 
    3: [{'p1': {'burst': 10, 'priority': 2}}, {'p2': {'burst': 8, 'priority': 1}}], 
    5: [{'p1': {'burst': 10, 'priority': 2}}, {'p2': {'burst': 6, 'priority': 1}}, {'p3': {'burst': 12, 'priority': 3}}]}
a[5][1]["p2"]["burst"] = 10
print(a)