#make redirectedTempFolder
redirectedTempFolder=tmp
mkdir -p $redirectedTempFolder

#downloading expression data
url="https://osf.io/2dbhv/download?version=1"
fileName=$redirectedTempFolder/Expression.gz

wget -O $fileName $url
gunzip $fileName

#downloading clinical data
url="https://osf.io/7yztd/download?version=1"
fileName=$redirectedTempFolder/Clinical

wget -O $fileName $url
