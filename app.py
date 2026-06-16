from dotenv import load_dotenv
from difflib import get_close_matches
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import streamlit as st
import requests
import os


API_KEY = st.secrets["API_KEY"]
movies=pickle.load(open("movies.pkl","rb"))

#Vectorization
tfidf = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

vectors = tfidf.fit_transform(movies["tag"])

def fetch_poster(movie_id):
   url=f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
   data=requests.get(url)
   data=data.json()
   
   poster_path= data.get("poster_path")
   if poster_path:
    poster_url= ("https://image.tmdb.org/t/p/w500/" + poster_path)
   else:
      poster_url= "https://via.placeholder.com/500x750?text=No+Image"
   rating=data.get("vote_average","N/A")
   release_date=data.get("release_date","unknown")
   overview=data.get("overview","no overview available")
   return (poster_url,rating,release_date,overview)

def recommend(movie):
  movie=movie.lower()
  match_movie=get_close_matches(movie,movies["title"].str.lower().tolist(),n=1,cutoff=0.6)

  if len(match_movie)==0:
    #print("NO such movie found")
    return [],[],[],[],[],[]
  movie_index = movies[movies["title"].str.lower() == match_movie[0]].index[0]
  movie_vector = vectors[movie_index]
  similarity_scores = cosine_similarity(movie_vector,vectors).flatten()
  distance = list(enumerate(similarity_scores))
  movie_list=sorted(distance,reverse=True,key=lambda x:x[1])[1:15]
  orginal_genre=movies.iloc[movie_index].genres
  similarity_score=[]
  recommended_movie=[]
  recommended_posters=[]
  recommended_rating=[]
  recommended_overview=[]
  recommended_release_date=[]
  #print("\nTop movie recommendation\n")
  
  for index,movie_data in movie_list:
    if movie_data < 0.15:
       continue
    recommended_genre=movies.iloc[index].genres
    if len(set(orginal_genre) & set(recommended_genre)) > 0:
      movie_id=movies.iloc[index].movie_id
      (poster,rating,release_date,overview)=fetch_poster(movie_id)
      recommended_movie.append(movies.iloc[index].title)
      recommended_posters.append(poster)
      recommended_rating.append(rating)
      recommended_release_date.append(release_date)
      recommended_overview.append(overview)
      similarity_score.append(round(movie_data*100,2))
      if len(recommended_movie)==5:
         break
  return (recommended_movie,recommended_posters,recommended_rating,recommended_overview,recommended_release_date,similarity_score)
st.set_page_config(
    page_title="Movie Recommendation System",
    layout="wide"
)

st.markdown("""
<style>

body {
    background-color: #0E1117;
}

.main {
    background-color: #0E1117;
}

h1 {
    color: white;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""<style>
            .movie-card{
            background:#1c1c1c;
            padding:15px;
            border-radius:15px;
            margin-top:-5px;
            min-height:180px;
            
            }
            .movie-card:hover{
               transform:scale(1.05);
               box-shadow: 0px 0px 15px rgba(255,255,255,0.3);
            }
            </style>""", unsafe_allow_html=True)
            
st.markdown("""<style>
            img {
    border-radius: 15px;
    transition: all 0.3s ease;
}

img:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 20px rgba(255,255,255,0.25);
}</style>""",unsafe_allow_html=True)

st.title("Movie Recommendation System")

movie_list=movies["title"].values
selected_movie=st.text_input("Enter a movie")


if st.button("Recommend"):

    with st.spinner("Finding your recommendation...."):

        (name, poster, rating,overview,date,score) = recommend(selected_movie.lower())

        if len(name) == 0:

            st.warning("No movie found")

        else:
            col=st.columns(5)
            st.caption("Your top recommedation")
            for i in range(len(name)):
               with col[i]:
                  st.image(poster[i], use_container_width=True)
                  st.markdown(f"""
                              
                              <div class="movie-card">
                              <h3>{name[i]}</h3>
                              <p> {score[i]}% Match</p>
                              <p>Rating :{rating[i]}</p>
                              <p>Rel_date:{date[i]}</p>
                              </div>
                              """, unsafe_allow_html=True)
            
st.caption("Movie provided by TMDB")
st.caption("This project  is just made for educational purpose only")
st.caption("Made by Amith P Anil (Data Science 2nd year Btech student)")
            

#st.markdown("""<><>""",unsafe_allow_html=True)
