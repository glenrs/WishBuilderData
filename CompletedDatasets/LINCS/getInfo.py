import h5py
import numpy as np
import sys, gzip

sigInfoFile = sys.argv[1]
gctxFileName = sys.argv[2]
metadataOut = sys.argv[3]
dataOut = sys.argv[4]
geneFile = sys.argv[5]
cellInfo = sys.argv[6]
pertInfo = sys.argv[7]
sigMetrics = sys.argv[8]

f = h5py.File(gctxFileName, "r")


grpname = f.require_group('/0')

subgrpMeta = grpname.require_group('/0/META')
colgrp = subgrpMeta.require_group('/0/META/ROW')
rowgrp = subgrpMeta.require_group('/0/META/COL')

subgrpData = grpname.require_group('/0/DATA')
subsubgrpData = subgrpData.require_group('/0/DATA/0')
i = 0
findingId = 0
for id in rowgrp["id"] :
    if id == "LJP005_HA1E_24H:M01" :
        findingId = i
        print(id)
        break
    i = i + 1
print(rowgrp["id"][findingId])
print(subsubgrpData["matrix"][findingId])

