import sys, gzip

inFile = sys.argv[1]
outFile = sys.argv[2]

with gzip.open(inFile, 'r') as iF :
    with gzip.open(outFile, 'w') as oF :
        i = 0
        for line in iF :
            i = i + 1
            if i > 20 :
                break
            oF.write(line)
