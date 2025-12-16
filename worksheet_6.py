import pandas as pd

# Question 1
print(pd.__version__)
df1 = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})
print(df1)

# Question 2
S1 = pd.Series([100, 200, 300, 400, 500])
print(S1)
print(S1.iloc[1])
print(S1.iloc[3])
S2 = pd.Series([10, 20, 30, 40, 50])
print(S1 + S2)

# Question 3
print(df1[['Name', 'City']])
df1['Salary'] = [50000, 60000, 70000]
print(df1)
print(df1['Age'].mean())
print(df1['Salary'].sum())

# Question 4
print(df1[df1['Age'] > 28])
df1_indexed = df1.set_index('Name')
print(df1_indexed)
print(df1_indexed.reset_index())

# Question 5
df_csv = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Department': ['Sales', 'Marketing', 'HR'],
    'Salary': [50000, 60000, 55000]
})
print(df_csv)
print(df_csv[df_csv['Salary'] > 55000][['Name', 'Department']])

# Question 6
print(df_csv.groupby('Department')['Salary'].mean())
print(df_csv.groupby('Department')['Salary'].agg(['min', 'max']))

# Question 7
df1_merge = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Department': ['Sales', 'Marketing', 'HR']
})
df2_merge = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Experience Years': [5, 7, 3]
})
merged = pd.merge(df1_merge, df2_merge, on='Name')
print(merged)

# Question 8
print(merged.sort_values('Experience Years', ascending=False))


