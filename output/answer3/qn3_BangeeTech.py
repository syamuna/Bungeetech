import sys
import csv
file = open('main3.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
rows = []
#-4 - red ,-5 - yellow
i=0
for row in csvreader:
    rows.append([i,row[0],row[-5],row[-4]])
    i+=1
arr=sorted(rows,key=lambda x:(int(x[3]),int(x[2])),reverse=True)

f = open('output3.csv', 'w')
writer = csv.writer(f)

head=["No.","Team","Yellow Cards","Red Cards"]
writer.writerow(head);
for i in arr:
    writer.writerow([i[0],i[1],i[2],i[3]])
    
file.close()
f.close()

