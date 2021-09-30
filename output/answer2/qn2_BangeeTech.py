import sys
import csv
file = open('main.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
rows = []
occ={}
for row in csvreader:
    occ[row[3]]=[sys.maxsize,-sys.maxsize]
    rows.append(row)
    
for row in rows:
    occ[row[3]]=[min(int(row[1]),occ[row[3]][0]),max(int(row[1]),occ[row[3]][1])]
    
ans=[]
for i in sorted(occ):
    ans.append([i,occ[i]])


f = open('output.csv', 'w')
writer = csv.writer(f)

head=["occupation","min","max"]
writer.writerow(head);
for i in ans:
    writer.writerow([i[0],i[1][0],i[1][1]])
f.close()


