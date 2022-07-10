import pandas as pd

path = 'dev/'

files = ['Approval_Or_Provisioning_juin.xlsx','Approval_Or_Provisioning_mai.xlsx']

files = [path + file for file in files]

df = pd.concat(pd.read_excel(files[0], sheet_name=None), ignore_index=True)

for index in range(1, len(files)):
    df1 = pd.concat(pd.read_excel(files[index], sheet_name=None), ignore_index=True)
    df = pd.concat([df, df1])

df.sort_values(by=['1', '2'], ascending = [True, True], inplace=True)
print(df.head(10))

#pivot = df.pivot_table(index=['1'], values='2', aggfunc='count')
#print(pivot.head(10))
df['combine'] = df['2'].astype(str) + ' | ' + df['3'].astype(str) + ' | ' + df['4'].astype(str)
df.drop(columns=["2", "3",'4'],inplace=True)
print(df.head(10))
#print(df.groupby('1').tail(1))

df.to_csv(path+'out.csv', index=False)