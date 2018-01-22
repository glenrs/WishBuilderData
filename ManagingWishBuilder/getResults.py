import sys

infile = sys.argv[1]

with open(infile, 'r') as f:
    first = True
    indeci = 0
    for line in f :
        lineList = line.strip('\n').split('\t')
        if first == True :
            first = False
            for i in range(len(lineList)) :
                if lineList[i] == "TCGA-Z7-A8R6-01A-11R-A41B-07" :
                    indeci = i
                    print(lineList[0] + "\t" + lineList[i])
        else :
            print(lineList[0] + "\t" + lineList[indeci])
