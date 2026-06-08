import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend(movie_name):
  if movie_name  not in movies["title_lower"].values:
    print("movie not found")
    return
  movie_index=movies[movies["title_lower"]==movie_name].index[0]
  distance=list(enumerate(similarity[movie_index]))
  distance=sorted(distance,reverse=True,key=lambda x:x[1])
  found=False
  for movie in distance[1:]:
  
    if (movie[1]>0):
     found=True
     print(movies.iloc[movie[0]].title)
  if not found:
    print("no similar movies")

movies=pd.DataFrame({
   "title":["Batman Begins",
        "Toy Story",
        "The Dark Knight",
        "Jumanji"],
  "genre":["Action|Crime|Drama",
        "Animation|Comedy",
        "Action|Crime|Drama",
        "Adventure|Fantasy"]
})
movies["title_lower"]=movies["title"].str.lower()
movies["genre"]=movies["genre"].str.lower()
movies["genre"]=movies["genre"].str.replace("|"," ",regex=False)

cv=CountVectorizer()
vectors=cv.fit_transform(movies["genre"])

similarity=cosine_similarity(vectors)

movie_name=input("Enter the exact movie name:").lower()
recommend(movie_name)