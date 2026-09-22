import pandas as pn
import numpy as np

data = {
    "nom" : ["ali" , "habib" , "brylo" , "ali"],
    "age" : [19 , 23 , 22 , 19],
    "note" : [20 , 19 , np.nan , 20]
}
df = pn.DataFrame(data)
dfs = pn.Series(data["nom"] , index = ['a' , 'b' , 'c'])
print(df)
# print(dfs)
# print(type(data , ))
# print(df.head(2))
# print(dfs.head(2))


# print(df.tail(2))
# print(dfs.tail(2))

# print(df.shape)
# print(dfs.shape)

# print(df.columns)

# print(df.info())

print(df.describe())

# print(df[["age" , "note"]])

# print(df.loc[0])
# print(df.loc[0,"nom"])

# print(df.iloc[0,2])

# print(df[df["note"] < 20])

# print(df.sort_values("note" , ascending=False))


# df["admin"] = df["note"] >= 10
# print(df)


# df = df.drop(columns=["age"])
# print(df)

# print(df.isnull().sum())

# df = df.dropna()

# df["age"] = df["age"].fillna(20)

# print(df.drop_duplicates())


# print(df.groupby("nom")["note"].mean()) 


# df.to_csv("student_clean.csv" , index=False)

# df = pn.read_csv("ventes.csv")
# print(df)

# data2 = [1,3,4,5]
# dg = pn.DataFrame(data2 , index= ["a","b","c","d"])
# print(dg)