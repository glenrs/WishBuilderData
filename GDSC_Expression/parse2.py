import pandas as pd
import sys, re, math, gzip 

cellLine = sys.argv[1]
doseResponse = sys.argv[2]
screenedComponents = sys.argv[3]
RACS = sys.argv[4]
variants = sys.argv[5]
expressionIn = sys.argv[6]
clinicalOut = sys.argv[7]
expressionOut = sys.argv[8]

def readSheetToMultipleDfs(xl,sheetname, indecisBetweenTables) :
    line = []
    previous = -1 
    tmpDfsList = []
    for i in indecisBetweenTables :
        if i - previous > 2 :
            nrows = xl.book.sheet_by_name(sheetname).nrows
            df = xl.parse(sheetname, skiprows=previous+1, skip_footer = nrows-i-1).dropna(axis=1, how='all')
            tmpDfsList.append(df)
        previous = i
    return tmpDfsList

def readXlToListDf(file) :
    xl = pd.ExcelFile(file)
    dfsList = []
    for sheetname in xl.sheet_names :
        df = xl.parse(sheetname)
        if df.empty == True :
            continue
        elif any(math.isnan(s) for s in list(df[df.columns[0]]) if type(s) is float) :
            indecisBetweenTables = list(s for s in range(len(list(df[df.columns[0]]))) if type(list(df[df.columns[0]])[s]) is float) 
            indecisBetweenTables.append(len(list(df[df.columns[0]])))
            tmpDfsList = readSheetToMultipleDfs(xl,sheetname,indecisBetweenTables)
            for df in tmpDfsList :
                dfsList.append(df)
        else :
            dfsList.append(df)
    return dfsList

def checkIfNan(value) :
    if type(value) == float:
        if math.isnan(value) == True:
            return True
    return False

print("making dataframes from excel")
cellLineDfs = readXlToListDf(cellLine) # 0.Cell line details 1.COSMIC tissue classification 2.TCGA tissue classification 3.Microsatillite instability data 4.Growth media
doseResponseDfs = readXlToListDf(doseResponse) # 0.fitted_dose_response
screenedComponentsDfs = readXlToListDf(screenedComponents) # 0.Screened_Compounds
RACSDfs = readXlToListDf(RACS) # 0.RACS
variantsDfs = readXlToListDf(variants) # 0.WES_variants 1.Legend


##The first three dictionaries are used to decode the MSI, Cancer type, and Screen Medium in the Cell Line file
##The fourth dictionary stores information from the DrugID in the screen compounds file to be used when making the dose response.
print("Making dictionaries")

TCGADict = {}
for i in range(len(cellLineDfs[2][cellLineDfs[2].columns[0]])) :
    TCGADict[cellLineDfs[2][cellLineDfs[2].columns[0]][i]] = cellLineDfs[2][cellLineDfs[2].columns[1]][i]

MIDDict = {}
for i in range(len(cellLineDfs[3][cellLineDfs[3].columns[0]])) :
    MIDDict[cellLineDfs[3][cellLineDfs[3].columns[0]][i]] = cellLineDfs[3][cellLineDfs[3].columns[1]][i]

GMDict = {}
for i in range(len(cellLineDfs[4][cellLineDfs[4].columns[0]])) :
    GMDict[cellLineDfs[4][cellLineDfs[4].columns[0]][i]] = cellLineDfs[4][cellLineDfs[4].columns[1]][i]

DrugIDDict = {}
for i in range(len(screenedComponentsDfs[0][screenedComponentsDfs[0].columns[0]])) :
    drugList = []
    if (type(screenedComponentsDfs[0][screenedComponentsDfs[0].columns[2]][i]) != float) :
        if screenedComponentsDfs[0][screenedComponentsDfs[0].columns[2]][i] == "-":
            if (len(screenedComponentsDfs[0][screenedComponentsDfs[0].columns[2]][i].split(", ")) > 1) :
                drugList = screenedComponentsDfs[0][screenedComponentsDfs[0].columns[2]][i].split(", ")
        else :
            drugList = screenedComponentsDfs[0][screenedComponentsDfs[0].columns[2]][i].split(", ")
    drugList.append(screenedComponentsDfs[0][screenedComponentsDfs[0].columns[1]][i])
    DrugIDDict[screenedComponentsDfs[0][screenedComponentsDfs[0].columns[0]][i]] = drugList

EnsembliIDDict = {}
numberOfCellLineRows = 0
for i in range(len(cellLineDfs[1][cellLineDfs[1].columns[1]])) :
    numberOfCellLineRows = numberOfCellLineRows + 1
    EnsembliIDDict[str(cellLineDfs[1][cellLineDfs[1].columns[1]][i])] = cellLineDfs[1][cellLineDfs[1].columns[0]][i]



##Write out Expression data to data.tsv.gz
headersNotConverted = []
headerValues = 0
indecisOfInterest = []
headersList = []
print("Writing Expression data to data.tsv.gz")
with gzip.open(expressionOut, 'w') as oF :
    with gzip.open(expressionIn, 'r') as iF :
        headersList = iF.readline().strip('\n').split('\t')

        first = True
        for i in range(len(headersList)) :
            if first == True:
                first = False
                indecisOfInterest.append(i)
            else :
                headerValues = headerValues + 1
                try :
                    headersList[i] = str(EnsembliIDDict[headersList[i]])
                    indecisOfInterest.append(i)
                except KeyError :
                    headersNotConverted.append(headersList[i])
        first = True
        printIndecis = []
        for i in indecisOfInterest :
            if first == True :
                first = False
#                oF.write(headersList[i])
                oF.write("Sample")
            else :
                if(headersList[i] == "OACp4C") :
                    printIndecis.append(i)
                    oF.write("\t" + headersList[i])
        oF.write("\n")

        for line in iF :
            lineList = line.strip('\n').split('\t')
            first = True
            for i in indecisOfInterest :
                if first == True :
                    first = False
                    oF.write(lineList[i])
                else :
                    if(any(i == printIndeci for printIndeci in printIndecis)) :
                        oF.write("\t" + str(lineList[i]))
            oF.write("\n")

print("number of values in header: " + str(headerValues))
print("number of cellLineRows: " + str(numberOfCellLineRows))
print("Headers not converted: " + str(headersNotConverted))


