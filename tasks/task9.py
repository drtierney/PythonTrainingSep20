from functools import reduce

inCsv = r"D:\temp\students.csv"
outCsv = r"D:\temp\student_result.csv"

def sum(rec):
    rec1 = rec.split(",")
    total = reduce(lambda x, y: int(x) + int(y), rec1[1:])
    r = "{0},{1}".format(rec1[0], total)
    average(r)

def average(r):
    r1 = r.split(",")
    avg = int(r1[1]) / 5
    percentage = "{0}%".format(avg)
    row = "{0},{1},{2},{3}".format(r1[0], r1[1], avg, percentage)
    out(row)

def out(row):
    with open(outCsv, 'a') as a:
        a.write(row + "\n")

with open(outCsv, 'w') as a:
    a.write('student'+','+'sum'+','+'average'+','+'percentage'+"\n")
    a.close()

with open(inCsv , "r") as f:
    for l in f:
        rec = l.rstrip()
        sum(rec)



