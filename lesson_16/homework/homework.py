import pandas as pd
import sqlite3 as sql

#  ******** TASK 1 ******** 
with sql.connect('./data/chinook.db') as connection:
    df_sql = pd.read_sql(
        "SELECT * FROM customers",
        con = connection
    )
    print(df_sql.head(10))
    print("-" *30)

df_iris = pd.read_json('./data/iris.json')
print(df_iris.shape)
print(df_iris.columns)
print("-" *30)

df_excel = pd.read_excel('./data/titanic.xlsx')
print(df_excel.head(5))
print("-" *30)

df_parquet = pd.read_parquet('./data/flights')
df_parquet.info()

df_movie = pd.read_csv('./data/movie.csv')
print(df_movie.sample(10))

# ************** TASK 2 **********
df_iris.columns = [col.lower() for col in df_iris.columns]
print(df_iris[["sepal_length", "sepal_width"]])
print(df_iris.head(10))

print(df_excel[df_excel['Age']>30])
print(df_excel['Pclass'].value_counts())

print(df_parquet[['origin', 'dest', 'carrier']])
print(df_parquet['dest'].nunique())

print(df_movie[df_movie['duration']>120])
print(df_movie.sort_values(by="director_facebook_likes", ascending=False))


# ********** TASK 3 **********
print(df_iris.describe())
print(df_iris.median())

print(df_excel['Age'].min())
print(df_excel['Age'].max())
print(df_excel['Age'].sum())

print(df_movie['director_facebook_likes'].max())
long_movies = df_movie.sort_values(by='duration', ascending=False)
print(long_movies.head(5))

print(df_parquet.isnull().sum())
col = 'dep_delay'
df_parquet[col] = df_parquet[col].fillna(df_parquet[col].mean())
print(df_parquet[col].isnull().sum())





























# import pandas as pd
# import sqlite3 as sql

# # ---------------- Part 1: Reading Files ----------------

# # 1. chinook.db
# connection = sql.connect('./data/chinook.db')
# df_customers = pd.read_sql("SELECT * FROM customers", con=connection)
# connection.close()
# print(df_customers.head(10))   

# # 2. iris.json
# df_iris = pd.read_json('./data/iris.json')
# print(df_iris.shape)
# print(df_iris.columns)

# # 3. titanic.xlsx
# df_excel = pd.read_excel('./data/titanic.xlsx')
# print(df_excel.head())

# # 4. Flights parquet
# df_parquet = pd.read_parquet('./data/flights.parquet')  # papka bo'lsa: './data/flights'
# df_parquet.info()

# # 5. movie.csv
# df_movie = pd.read_csv('./data/movie.csv')
# print(df_movie.sample(n=10))


# # ---------------- Part 2: Exploring DataFrames ----------------

# # 1. iris
# df_iris.columns = [col.lower() for col in df_iris.columns]
# print(df_iris[['sepal_length', 'sepal_width']])   # ustun nomlari izohga qarang

# # 2. titanic
# print(df_excel[df_excel['Age'] > 30])
# print(df_excel['Pclass'].value_counts())          # ustun nomi izohga qarang

# # 3. flights
# print(df_parquet[['origin', 'dest', 'carrier']])
# print(df_parquet['dest'].nunique())

# # 4. movie
# df_long = df_movie[df_movie['duration'] > 120]
# df_long_sorted = df_long.sort_values(by='director_facebook_likes', ascending=False)
# print(df_long_sorted)