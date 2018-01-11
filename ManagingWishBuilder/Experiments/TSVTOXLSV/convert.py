import pandas as pd
import sys

tsvFile = sys.argv[1]
xlsxFile = sys.argv[2]


df = pd.DataFrame.from_csv(tsvFile, sep='\t')

#print(df)

writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')

writer.save()
