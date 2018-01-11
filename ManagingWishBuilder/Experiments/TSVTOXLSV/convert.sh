#! /bin/bash

softwareFolder=Software
minicondaPath=$softwareFolder/miniconda/bin/

dataOutFilegz="data.tsv.gz"
metadataOutFilegz="metadata.tsv.gz"
xlsxFile="xl.xlsx"

echo "Setting up environment"
cd $minicondaPath
source activate my_xl_env
cd ../../..

python convert.py $metadataOutFilegz $xlsxFile
