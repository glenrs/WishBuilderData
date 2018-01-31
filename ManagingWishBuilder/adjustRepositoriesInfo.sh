#! /bin/bash

cd WishBuilder

modifyFiles () {
  git checkout $1
  echo "Description is coming... " > $1/description.md
  echo "title: " $2 > $1/config.yaml
  echo "featureDescription: " $3 >> $1/config.yaml
  echo "featureDescriptionPlural: " $4 >> $1/config.yaml
  git add --all
  git commit -m "Readjusted description.md/config.yaml"
  git push origin $1
  git checkout master
}

#modifyFiles BiomarkerBenchmark_GSE10320 "BiomarkerBenchmark GSE10320" gene genes
#modifyFiles CCLE_mRNA_isoform_kallisto_Tatlow "CCLE mRNA isoform kallisto Tatlow" transcript transcripts
#modifyFiles LINCS_PhaseII_Level3 "LINCS PhaseII Level3" gene genes
#modifyFiles LINCS_PhaseII_Level4 "LINCS PhaseII Level4" gene genes
#modifyFiles LINCS_PhaseII_Level5 "LINCS PhaseII Level5" gene genes
#modifyFiles LINCS_PhaseI_Level3 "LINCS PhaseI Level3" gene genes
#modifyFiles LINCS_PhaseI_Level4 "LINCS PhaseI Level4" gene genes
#modifyFiles LINCS_PhaseI_Level5 "LINCS PhaseI Level5" gene genes
#modifyFiles GSE62944_Normal_FeatureCounts "GSE62944 Normal FeatureCounts" gene genes
#modifyFiles GSE62944_Normal_TPM "GSE62944 Normal TPM" gene genes
#modifyFiles GSE62944_Tumor_FeatureCounts "GSE62944 Tumor FeatureCounts" gene genes
#modifyFiles GSE62944_Tumor_TPM "GSE62944 Tumor TPM" gene genes
#modifyFiles CCLE_mRNA_gene_kallisto_Tatlow "CCLE mRNA gene kallisto Tatlow" gene genes
#modifyFiles BiomarkerBenchmark_GSE1456 "BiomarkerBenchmark GSE1456" gene genes
#modifyFiles BiomarkerBenchmark_GSE15296 "BiomarkerBenchmark GSE15296" gene genes
#modifyFiles BiomarkerBenchmark_GSE19804 "BiomarkerBenchmark GSE19804" gene genes
#modifyFiles BiomarkerBenchmark_GSE20181 "BiomarkerBenchmark GSE20181" gene genes
#modifyFiles BiomarkerBenchmark_GSE20189 "BiomarkerBenchmark GSE20189" gene genes
#modifyFiles BiomarkerBenchmark_GSE2109_Breast "BiomarkerBenchmark GSE2109 Breast" gene genes
##modifyFiles BiomarkerBenchmark_GSE2109_Colon "BiomarkerBenchmark GSE2109 Colon" gene genes
#modifyFiles BiomarkerBenchmark_GSE2109_Endometrium "BiomarkerBenchmark GSE2109 Endometrium" gene genes
#modifyFiles BiomarkerBenchmark_GSE2109_Kidney "BiomarkerBenchmark GSE2109 Kidney" gene genes
#modifyFiles BiomarkerBenchmark_GSE2109_Lung "BiomarkerBenchmark GSE2109 Lung" gene genes
#modifyFiles BiomarkerBenchmark_GSE2109_Ovary "BiomarkerBenchmark GSE2109 Ovary" gene genes
#modifyFiles BiomarkerBenchmark_GSE2109_Prostate "BiomarkerBenchmark GSE2109 Prostate" gene genes
#modifyFiles BiomarkerBenchmark_GSE2109_Uterus "BiomarkerBenchmark GSE2109 Uterus" gene genes
#modifyFiles BiomarkerBenchmark_GSE21510 "BiomarkerBenchmark GSE21510" gene genes
#modifyFiles BiomarkerBenchmark_GSE25507 "BiomarkerBenchmark GSE25507" gene genes
#modifyFiles BiomarkerBenchmark_GSE26682_U133A "BiomarkerBenchmark GSE26682 U133A" gene genes
#modifyFiles BiomarkerBenchmark_GSE26682_U133PLUS2 "BiomarkerBenchmark GSE26682 U133PLUS2" gene genes
#modifyFiles BiomarkerBenchmark_GSE27279 "BiomarkerBenchmark GSE27279" gene genes
#modifyFiles BiomarkerBenchmark_GSE27342 "BiomarkerBenchmark GSE27342" gene genes
#modifyFiles BiomarkerBenchmark_GSE27854 "BiomarkerBenchmark GSE27854" gene genes
#modifyFiles BiomarkerBenchmark_GSE30219 "BiomarkerBenchmark GSE30219" gene genes
#modifyFiles BiomarkerBenchmark_GSE30784 "BiomarkerBenchmark GSE30784" gene genes
#modifyFiles BiomarkerBenchmark_GSE32646 "BiomarkerBenchmark GSE32646" gene genes
#modifyFiles BiomarkerBenchmark_GSE37147 "BiomarkerBenchmark GSE37147" gene genes
#modifyFiles BiomarkerBenchmark_GSE37199 "BiomarkerBenchmark GSE37199" gene genes
#modifyFiles BiomarkerBenchmark_GSE37745 "BiomarkerBenchmark GSE37745" gene genes
#modifyFiles BiomarkerBenchmark_GSE37892 "BiomarkerBenchmark GSE37892" gene genes
#modifyFiles BiomarkerBenchmark_GSE38958 "BiomarkerBenchmark GSE38958" gene genes
#modifyFiles BiomarkerBenchmark_GSE39491 "BiomarkerBenchmark GSE39491" gene genes
#modifyFiles BiomarkerBenchmark_GSE39582 "BiomarkerBenchmark GSE39582" gene genes
#modifyFiles BiomarkerBenchmark_GSE40292 "BiomarkerBenchmark GSE40292" gene genes
#modifyFiles BiomarkerBenchmark_GSE4271 "BiomarkerBenchmark GSE4271" gene genes
#modifyFiles BiomarkerBenchmark_GSE43176 "BiomarkerBenchmark GSE43176" gene genes
#modifyFiles BiomarkerBenchmark_GSE46449 "BiomarkerBenchmark GSE46449" gene genes
#modifyFiles BiomarkerBenchmark_GSE46691 "BiomarkerBenchmark GSE46691" gene genes
#modifyFiles BiomarkerBenchmark_GSE46995 "BiomarkerBenchmark GSE46995" gene genes
#modifyFiles BiomarkerBenchmark_GSE48391 "BiomarkerBenchmark GSE48391" gene genes
#modifyFiles BiomarkerBenchmark_GSE5460 "BiomarkerBenchmark GSE5460" gene genes
#modifyFiles BiomarkerBenchmark_GSE5462 "BiomarkerBenchmark GSE5462" gene genes
#modifyFiles BiomarkerBenchmark_GSE58697 "BiomarkerBenchmark GSE58697" gene genes
#modifyFiles BiomarkerBenchmark_GSE63885 "BiomarkerBenchmark GSE63885" gene genes
#modifyFiles BiomarkerBenchmark_GSE6532_U133A "BiomarkerBenchmark GSE6532 U133A" gene genes
#modifyFiles BiomarkerBenchmark_GSE6532_U133PLUS2 "BiomarkerBenchmark GSE6532 U133PLUS2" gene genes
#modifyFiles BiomarkerBenchmark_GSE67784 "BiomarkerBenchmark GSE67784" gene genes
modifyFiles GDSC_Expression "GDSC Expression" gene genes
