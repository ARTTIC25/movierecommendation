import pandas as pd
import ast
movies=pd.read_csv("tmdb_5000_movies.csv")
credits=pd.read_csv("tmdb_5000_credits.csv")
#print(movies.columns)
#print(movies.head())
#print(credits.head())
#rint(movies.shape)
#print(credits.shape)

def covert(text):
  result=[]
  for i in ast.literal_eval(text):
    result.append(i["name"])
  return result

movies=movies.merge(credits,on="title")
movies=movies[[
   "movie_id",
    "title",
    "overview",
    "genres",
    "keywords",
    "cast",
    "crew"
]]
print(movies.head())
movies.dropna(inplace=True)
print(movies.isnull().sum())

movies["genres"]=movies["genres"].apply(covert)
print(movies.iloc[0].genres)

movies["keywords"]=movies["keywords"].apply(covert)
print(movies.iloc[0].keywords)
