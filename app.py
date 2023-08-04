import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_posters(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=13bd738aac6496ca2d70815f03a815b4'.format(movie_id))
    data=response.json()
    return"https://image.tmdb.org/t/p/w500/" + data['poster_path']

   
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movie_titles, recommended_movie_posters = [], []
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        # fetch poster API
        recommended_movie_titles.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_posters(movie_id))
    return recommended_movie_titles, recommended_movie_posters


movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title("movie recommender system")

selected_movie_name=st.selectbox(
    'which movies wann see?',
    movies['title'].values)


if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:  
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
