import sys

infile = sys.argv[1]
value = sys.argv[2]

with open(infile, 'r') as f:
    first = True
    indeci = 0
    for line in f :
        lineList = line.strip('\n').split('\t')
        if first == True :
            first = False
            for i in range(len(lineList)) :
                if lineList[i] == value :
                    indeci = i
                    print(lineList[0] + "\t" + lineList[i])
        else :
            print(lineList[0] + "\t" + lineList[indeci])
