import csv
with open("neu.csv","w") as f:
    w=csv.writer(f,delimiter=",")
    w.writerow(["one","two","three"])
    w.writerow(["four","five","six"])
with open("neu.csv","r") as fu:
    r=csv.reader(fu,delimiter=",")
    for row in r:
        print(",".join(row))
    
