import streamlit as st
import pickle
import requests

movies_list = pickle.load(open('movies.pkl' , 'rb'))
similarity = pickle.load(open('similarity.pkl' , 'rb'))
movies_titles = movies_list['title'].values

def fetch_poster(movie_id) :
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=38e02bca19b613c9e97947a36a95dba6&language=en-US'.format(movie_id))
    movie_data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + movie_data['poster_path']

def recommend_movie(movie) :
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    close_movies = sorted(list(enumerate(similarity[movie_index])) , reverse=True, key=lambda x : x[1])[1:6]

    col1 , col2 , col3 , col4 , col5 = st.columns([1,1,1,1,1])

    with col1 :
        image = fetch_poster(movies_list.iloc[close_movies[0][0]].id)
        st.image(image, width=100 , caption=movies_list.iloc[close_movies[0][0]].title)

    with col2 :
        image = fetch_poster(movies_list.iloc[close_movies[1][0]].id)
        st.image(image, width=100 , caption=movies_list.iloc[close_movies[1][0]].title)

    with col3 :
        image = fetch_poster(movies_list.iloc[close_movies[2][0]].id)
        st.image(image, width=100 , caption=movies_list.iloc[close_movies[2][0]].title)

    with col4 :
        image = fetch_poster(movies_list.iloc[close_movies[3][0]].id)
        st.image(image, width=100 , caption=movies_list.iloc[close_movies[3][0]].title)

    with col5 :
        image = fetch_poster(movies_list.iloc[close_movies[4][0]].id)
        st.image(image, width=100 , caption=movies_list.iloc[close_movies[4][0]].title)


st.title('Which Movies to Watch ?')

#with st.form('my_form') :
st.write('Movies for You!!')
my_movie = st.selectbox('Pick a Movie',movies_titles)
if st.button('Recommend') :
    recommend_movie(my_movie)
