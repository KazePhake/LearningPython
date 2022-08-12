import pandas as pd

csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'
#df = pd.read_csv(csv_path)

df = pd.read_excel(xlsx_path)
df.head()

#x = df[['Length']]
# x = df['Length']
# print(x)
# x = df[['Artist']]
# print(type(x))
# y = df[['Artist','Length','Genre']]
# print(y)

# x = df.loc[1,'Artist']
# print(x)

x = df.iloc[0:3,0:4]
print(df)