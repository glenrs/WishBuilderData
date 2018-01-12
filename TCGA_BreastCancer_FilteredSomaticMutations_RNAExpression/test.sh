#! /bin/bash

#Folders
redirectedTemp=tmp
inFiles=$redirectedTemp/inFiles
outFiles=$redirectedTemp/outFiles
theirOutput=$redirectedTemp/theirOutput
variantsOutput=$redirectedTemp/variants

#outFiles
mutectOut=$outFiles/"TCGA.BRCA.mutect.c6a029e5-0ea3-410d-9e67-360bdfee2914.DR-7.0.somatic_adjusted.maf.gz"
varscanOut=$outFiles/"TCGA.BRCA.varscan.2849f60b-c211-469a-a1ef-4105bb75d3ec.DR-7.0.somatic_adjusted.maf.gz"
museOut=$outFiles/"TCGA.BRCA.muse.d9876b23-3e7d-4d7b-bc1b-3b4393cd2afb.DR-7.0.somatic_adjusted.maf.gz"
somaticsniperOut=$outFiles/"TCGA.BRCA.somaticsniper.8b1474b5-0216-4dbc-bc21-e5c6fcb5600f.DR-7.0_adjusted.somatic.maf.gz"

#theirFiles
theirMutect=$theirOutput/"Mutect2.tsv"
theirVarscan=$theirOutput/"VarScan2.tsv"
theirMuse=$theirOutput/"MUSE.tsv"
theirSomaticSniper=$theirOutput/"SomaticSniper.tsv"

#Variants
mutectVariants=$variantsOutput/"mutectVariants.gz"
varscanVariants=$variantsOutput/"varscanVariants.gz"
museVariants=$variantsOutput/"museVariants.gz"
somaticsSniperVariants=$variantsOutput/"somaticsSniperVariants.gz"


#python test_files.py $mutectOut $theirMutect $mutectVariants

python test2.py $mutectOut $theirMutect $mutectVariants
python test2.py $varscanOut $theirVarscan $varscanVariants
python test2.py $museOut $theirMuse $museVariants
python test2.py $somaticsniperOut $theirSomaticSniper $somaticsSniperVariants

