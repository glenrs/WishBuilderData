import sys, gzip

file1 = sys.argv[1]
file2 = sys.argv[2]
variants = sys.argv[3] 


with gzip.open(file1, 'r') as f1 :
    with gzip.open(variants, 'w') as of :
        for linef1 in f1 :
            linef1 = linef1.decode()
            match = False
            with open(file2, 'r') as f2 :
                for linef2 in f2 :
#                    linef2 = linef2.decode()
                    if(match == True) :
                        break
                    if(len(linef2) != len(linef1)) :
                        continue
                    else :
                        for i in range(len(linef2)) :
                            if(linef2[i] != linef1[i]) :
                                break
                            elif(linef2[i] == linef1[i]) and ((len(linef2) - 1) == i) :
                                match = True
            if(match == False) :
                of.write(linef1.encode())
