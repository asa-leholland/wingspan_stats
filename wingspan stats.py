import pandas as pd
import pip
pip.main(["install", "openpyxl"])

pd.options.display.max_columns = None
pd.options.display.max_rows = None

path = 'wingspan.xlsx'


xls = pd.ExcelFile(path)
df1 = pd.read_excel(xls, 0)
df2 = pd.read_excel(xls, 1)
df3 = pd.read_excel(xls, 2)
df4 = pd.read_excel(xls, 3)

datacollection = False
if datacollection:
	for df in (df2, df3):
		print(df)
		[print(col) for col in df.columns]

df2 = df2[['Bonus card', '%', 'VP']]

# is_not_empty =  df2['VP'] == '-'

# df2 = df2[~is_not_empty]

df2 = df2[~df2["VP"].str.contains('per')]
df2 = df2[~df2["VP"].str.contains('-')]
df2 = df2[~df2["%"].astype(str).str.contains('-')]

df2['Low Number'] = df2['VP'].str.extract('^(\d) to', expand=True)
df2['Low Score'] = df2['VP'].str.extract('birds: (\d)', expand=True)
df2['High Number'] = df2['VP'].str.extract('; (\d)', expand=True)
df2['High Score'] = df2['VP'].str.extract('(\d)$', expand=True)

r'^(\d) to (\d) birds: (\d); (\d)\+ birds: (\d)$'


df2['%'] = df2['%'].astype(str).str.replace('.0', '')

df2['%'] = df2['%'].astype(str).str.replace('*', '')


df3 = df2[['Bonus card', '%', 'Low Number', 'Low Score', 'High Number', 'High Score']]

print(df3)

df3.to_csv('goal_output.csv', sep='\t')