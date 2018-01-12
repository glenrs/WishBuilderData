import sys, gzip

file1 = sys.argv[1]
file2 = sys.argv[2]
variants = sys.argv[3] 

file1IDs = []
with gzip.open(file1, 'r') as f1 :
        firstf1 = True 
        barcodeIndex = 0
        for linef1 in f1 :
            linef1 = linef1.decode()
            linef1List = linef1.strip('\n').split('\t')
            if firstf1 == True :
                firstf1 = False
                barcodeIndex = [i for i in range(len(linef1List)) if linef1List[i] == "Tumor_Sample_Barcode"][0]
            else :
                file1IDs.append(str(("-").join(linef1List[barcodeIndex].split('-')[:4])))

file2IDs = []
with open(file2, 'r') as f2 :
    f2.readline()
    for line in f2 :
        lineList = line.strip('\n').split('\t')
        file2IDs.append(str(lineList[1]))


file1ButNot2 = []
file1ButNot2 = list(file1IDs[i] for i in range(len(file1IDs)) if not file1IDs[i] in file2IDs)
file2ButNot1 = list(file2IDs[i] for i in range(len(file2IDs)) if not file2IDs[i] in file1IDs)
with gzip.open(variants, 'w') as of :
    of.write(("My outFiles but not theirs: \t").encode())
    of.write((str(file1ButNot2) + "\n").encode())
    of.write(("Their outFiles but not mine: \t").encode())
    of.write((str(file2ButNot1) + "\n").encode())
#            match = False
#            with open(file2, 'r') as f2 :
#                for linef2 in f2 :
#                    linef2 = linef2.decode()
#                    print(linef2)
#                    if(match == True) :
#                        break
#                    if(len(linef2) != len(linef1)) :
#                        continue
#                    else :
#                        for i in range(len(linef2)) :
#                            if(linef2[i] != linef1[i]) :
#                                break
#                            elif(linef2[i] == linef1[i]) and ((len(linef2) - 1) == i) :
#                               match = True
#            if(match == False) :
#                of.write(linef1.encode())
