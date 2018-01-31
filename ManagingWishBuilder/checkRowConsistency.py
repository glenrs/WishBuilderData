import sys, gzip

genelabels = sys.argv[1]

def isEqual(firstList, secondList) :
    if len(firstList) != len(secondList) :
        return False
    for i in range(len(firstList)) :
        if firstList[i] != secondList[i] :
            return False
    return True

with gzip.open(genelabels, 'r') as f :
    firstLineList = f.readline().decode().strip('\n').split('\t')[1:]
    for line in f :
        otherLineList = line.decode().strip('\n').split('\t')[1:]
        equal = isEqual(firstLineList, otherLineList) 
        if not equal :
            print(line)
