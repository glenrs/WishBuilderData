import sys, gzip

mutectIn = sys.argv[1]
varscanIn = sys.argv[2]
museIn = sys.argv[3]
somaticsniperIn = sys.argv[4]
outFile = sys.argv[5]

def columnsOfInterest(inFile, mutationDict, duplicationList) :
    with gzip.open(inFile, 'r') as iF :
        first = True
        alleleIndex = 0
        lineCounter = 0

        for line in iF :
            lineCounter = lineCounter + 1
            line = line.decode()
            if(line[0] == '#') :
                continue
            else :
                if first == True :
                    first = False
                    headerList = line.strip('\n').split('\t')
                    barcodeIndex = [i for i in range(len(headerList)) if headerList[i] == "Tumor_Sample_Barcode"][0]
                    hugoSymbolIndex = [i for i in range(len(headerList)) if headerList[i] == "Hugo_Symbol"][0]
                    chromosomeIndex = [i for i in range(len(headerList)) if headerList[i] == "Chromosome"][0]
                    startPositionIndex = [i for i in range(len(headerList)) if headerList[i] == "Start_Position"][0]
                    endPositionIndex = [i for i in range(len(headerList)) if headerList[i] == "End_Position"][0]
                    strandIndex = [i for i in range(len(headerList)) if headerList[i] == "Strand"][0]
                    alleleIndex = [i for i in range(len(headerList)) if headerList[i] == "Allele"][0]
                else : 
                    lineList = line.strip('\n').split('\t')
                    createdId = lineList[0] + "_" + '-'.join(lineList[barcodeIndex].split('-')[:4])
#                    createdId = lineList[0] 
#                    createdId = lineList[0] + "_" + '-'.join(lineList[barcodeIndex].split('-'))
#                    createdId = '-'.join(lineList[barcodeIndex].split('-')[:4]) + "_" + lineList[hugoSymbolIndex] + "_" + lineList[chromosomeIndex] + "_" + lineList[startPositionIndex] + "_" + lineList[endPositionIndex] + "_" + lineList[strandIndex] + "_" + lineList[alleleIndex]
#                    createdId = lineList[hugoSymbolIndex] + "_" + lineList[chromosomeIndex] + "_" + lineList[startPositionIndex] + "_" + lineList[endPositionIndex] + "_" + lineList[strandIndex] + "_" + lineList[alleleIndex]
                    try :
#                        fileList = mutationDict[createdId]
#                        if inFile not in fileList :
#                            mutationDict[createdId].append(inFile)
                        mutationDict[createdId].add(inFile)
#                        else :
#                            raise ValueError("line isn't included because there is already a " + createdId + " in " + inFile) 
                    except KeyError :
                        mutationDict[createdId] = set()
                        mutationDict[createdId].add(inFile)
#                    except ValueError as message :
#                        print(message)
#                        duplicationList.append(createdId + "\t" + inFile)
                        

mutationDict = {}
duplicationList = []
columnsOfInterest(mutectIn, mutationDict, duplicationList)
columnsOfInterest(varscanIn, mutationDict, duplicationList)
columnsOfInterest(museIn, mutationDict, duplicationList)
columnsOfInterest(somaticsniperIn, mutationDict, duplicationList)

with gzip.open(outFile, 'w') as oF :
#    oF.write(("Patient_Id\tHugo_Symbol\tChromosome\tStart_Position\tEnd_Position\tStrand\tAllele\n").encode())
    oF.write(("Patient_Id\tHugo_Symbol\n").encode())
    for createdId, files  in mutationDict.items() :
        if len(files) > 4 : 
            raise ValueError("Duplication in file")
        if len(files) > 2 :
            createdIdList = createdId.split('_')
            oF.write(('\t'.join(createdIdList) + "\n").encode())
#    for element in duplicationList :
#        oF.write((element + "\n").encode())
