import sys, gzip

expression = sys.argv[1]

with gzip.open(expression, 'r') as f :
    lineList = f.readline().strip('\n').split('\t')
    for i in range(len(lineList)) :
        for j in range(len(lineList)) :
            if lineList[i] == lineList[j] and i != j :
                print(lineList[i])
