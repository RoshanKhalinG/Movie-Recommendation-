import pickle
import streamlit as st
import requests
from streamlit_option_menu import option_menu

# API Key (please replace with your own API key)
API_KEY = "8265bd1679663a7ea12ac168da84d2e8"

# Function to fetch movie details
def fetch_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch movie details for ID {movie_id}. Error {response.status_code}")
        return None

# Function to fetch movie credits
def fetch_movie_credits(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Failed to fetch movie credits for ID {movie_id}. Error {response.status_code}")
        return None

# Function to fetch movie poster
def fetch_poster(movie_id):
    data = fetch_movie_details(movie_id)
    if data and 'poster_path' in data:
        return f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
    else:
        st.warning(f"Poster not found for movie ID {movie_id}.")
        return None

# Function to fetch profile picture
def fetch_profile_picture(profile_path):
    if profile_path:
        return f"https://image.tmdb.org/t/p/w185/{profile_path}"
    else:
        return None

# Function to fetch movies by genre
def fetch_movies_by_genre(genre_id, year_range, rating):
    url = (f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genre_id}"
           f"&primary_release_date.gte={year_range[0]}-01-01"
           f"&primary_release_date.lte={year_range[1]}-12-31"
           f"&vote_average.gte={rating}")
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    else:
        st.error(f"Failed to fetch movies for genre ID {genre_id}. Error {response.status_code}")
        return []

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_ids = [movies.iloc[i[0]].movie_id for i in distances[1:6]]
    recommended_movie_names = [movies.iloc[i[0]].title for i in distances[1:6]]
    recommended_movie_posters = [fetch_poster(movie_id) for movie_id in recommended_movie_ids]
    return recommended_movie_ids, recommended_movie_names, recommended_movie_posters


# Function to show movie details
def show_movie_details(movie_id):
    data = fetch_movie_details(movie_id)
    credits = fetch_movie_credits(movie_id)
    if data and credits:
        st.markdown("<div class='movie-card'>", unsafe_allow_html=True)

        # Create columns for poster and details
        col1, col2 = st.columns([1, 2])  # Adjust column widths as needed

        # Movie poster
        with col1:
            poster_url = fetch_poster(movie_id)
            if poster_url:
                st.image(poster_url, width=300)

        # Movie details
        with col2:
            st.header(data['title'])
            
            # Overview
            st.subheader("Overview")
            st.write(data['overview'])
            
            # Genres
            st.subheader("Genres")
            genres = ", ".join([genre['name'] for genre in data['genres']])
            st.write(genres)
            
            # Release Date
            st.subheader("Release Date")
            st.write(data['release_date'])
            
            # Rating
            st.subheader("Rating")
            st.write(data['vote_average'])
            
            # Website
            if 'homepage' in data and data['homepage']:
                st.subheader("Official Website")
                st.markdown(f"[Visit Official Website]({data['homepage']})", unsafe_allow_html=True)

        # Display Director
        directors = [member for member in credits['crew'] if member['job'] == 'Director']
        if directors:
            st.subheader("Director")
            director_cols = st.columns(len(directors))
            for director_col, director in zip(director_cols, directors):
                name = director['name']
                profile_path = director.get('profile_path', None)
                profile_url = fetch_profile_picture(profile_path)
                with director_col:
                    if profile_url:
                        st.image(profile_url, width=100)
                    st.write(name)
        
        # Display Top Cast
        top_cast = credits['cast'][:5]  # Top 5 cast members
        if top_cast:
            st.subheader("Top Cast")
            cast_cols = st.columns(len(top_cast))
            for cast_col, cast_member in zip(cast_cols, top_cast):
                name = cast_member['name']
                profile_path = cast_member.get('profile_path', None)
                profile_url = fetch_profile_picture(profile_path)
                with cast_col:
                    if profile_url:
                        st.image(profile_url, width=100)
                    st.write(name)
        
        st.markdown("</div>", unsafe_allow_html=True)

# Function to search movies by actor
def search_movies_by_actor(actor_name):
    url = f"https://api.themoviedb.org/3/search/person?api_key={API_KEY}&query={actor_name}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            actor_id = data['results'][0]['id']
            return fetch_movies_by_actor_id(actor_id)
        else:
            st.warning("No actor found with this name.")
            return []
    else:
        st.error(f"Failed to search actor. Error {response.status_code}")
        return []

def fetch_movies_by_actor_id(actor_id):
    url = f"https://api.themoviedb.org/3/person/{actor_id}/movie_credits?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['cast']
    else:
        st.error(f"Failed to fetch movies by actor. Error {response.status_code}")
        return []

# Page configuration
st.set_page_config(page_title='Movie Recommender System', layout='wide')
st.markdown(
    """
    <style>
    body {
         background-image: url('C:/Users/Acer/Desktop/Movie Recommendation/MRS/frontendMRS/image/back1.jpg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: #f0f0f0;
    }
    .title {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #f39c12;
        text-align: center;
        margin-bottom: 40px;
        font-size: 48px;
        text-shadow: 2px 2px 4px #000000;
    }
    .movie-card {
        background-color: rgba(31, 31, 31, 0.8);
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
    }
    .movie-title {
        font-size: 16px;
        color: #f39c12;
        margin-top: 10px;
        font-weight: bold;
    }
    .button {
        background-color: #f39c12;
        color: white;
        padding: 10px;
        font-size: 18px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        width: 100%;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
    }
    .button:hover {
        background-color: #e67e22;
    }
    .container {
        padding: 10px;
    }
    .header {
        font-size: 24px;
        color: #f39c12;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown(
    """
    <a href='/' style="text-decoration: none;">
        <h1 class='title'>🎬 Movie Recommender System 🍿</h1>
    </a>
    """,
    unsafe_allow_html=True
)

# Sidebar menu
with st.sidebar:
    selected_option = option_menu(
        menu_title=None,
        options=["Get Movie Recommendation", "Filter Search", "Browse Genre", "Search by Actor"],
        icons=["search", "star", "film", "person"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#333"},
            "icon": {"color": "#f39c12", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#444"},
            "nav-link-selected": {"background-color": "#444"},
        }
    )

# Load data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movie_list = movies['title'].values

# Get query params
query_params = st.query_params
movie_id = query_params.get('movie_id', None)

# Main logic
if movie_id:
    show_movie_details(movie_id)
else:    
    if selected_option == "Get Movie Recommendation":
        # Movie selection
        selected_movie = st.selectbox(
            "Type or select a movie from the dropdown",
            movie_list
        )

        # Show recommendations
        if st.button('Show Recommendation', key='recommend_button'):
            st.markdown("<h2 class='header'>Recommended Movies</h2>", unsafe_allow_html=True)
            recommended_movie_ids, recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
            cols = st.columns(5)
            for col, movie_id, name, poster in zip(cols, recommended_movie_ids, recommended_movie_names, recommended_movie_posters):
                with col:
                    st.markdown(f"<div class='movie-card'><a href='?movie_id={movie_id}'><img src='{poster}' width='100%'></a><div class='movie-title'>{name}</div></div>", unsafe_allow_html=True)

    elif selected_option == "Filter Search":
        st.header("Filter Movies")

        # Genre selection
        genre = st.selectbox("Select Genre", ["Action", "Comedy", "Drama", "Horror", "Romance"])
        year_range = st.slider("Select Year Range", 2000, 2024, (2000, 2024))
        rating = st.slider("Select Minimum Rating", 0.0, 10.0, 5.0)
        genre_ids = {"Action": 28, "Comedy": 35, "Drama": 18, "Horror": 27, "Romance": 10749}
        genre_id = genre_ids.get(genre, 0)
        
        # Optional actor search
        actor_name = st.text_input("Enter actor's name (optional)")

        if st.button("Search"):
            if actor_name:
                # Fetch movies by actor
                movies = search_movies_by_actor(actor_name)
                
                # Apply filters manually
                filtered_movies = []
                for movie in movies:
                    try:
                        # Check genre
                        movie_genre_ids = movie.get('genre_ids', [])
                        if genre_id != 0 and genre_id not in movie_genre_ids:
                            continue
                        
                        # Check release date
                        release_date = movie.get('release_date', '')
                        release_year = int(release_date[:4]) if release_date else 0
                        if not (year_range[0] <= release_year <= year_range[1]):
                            continue
                        
                        # Check rating
                        vote_average = float(movie.get('vote_average', 0))
                        if vote_average < rating:
                            continue
                        
                        # If all filters pass, add movie to filtered list
                        filtered_movies.append(movie)
                    except ValueError:
                        # Handle cases where conversion to int or float fails
                        continue
            
            else:
                # Fetch movies by genre
                filtered_movies = fetch_movies_by_genre(genre_id, year_range, rating)
            
            # Display movies in a grid
            cols = st.columns(5)
            for i, movie in enumerate(filtered_movies):
                if i % 5 == 0:
                    cols = st.columns(5)
                with cols[i % 5]:
                    movie_id = movie['id']
                    poster_url = f"https://image.tmdb.org/t/p/w500/{movie['poster_path']}"
                    st.markdown(
                        f"<div class='movie-card'><a href='?movie_id={movie_id}'><img src='{poster_url}' width='100%'></a><div class='movie-title'>{movie['title']}</div></div>",
                        unsafe_allow_html=True
                    )





    elif selected_option == "Browse Genre":
        st.header("Browse Movies by Genre")
        genres = {"Action": 28, "Comedy": 35, "Drama": 18, "Horror": 27, "Romance": 10749}
        genre = st.selectbox("Select Genre", list(genres.keys()))
        genre_id = genres.get(genre, 0)

        if st.button("Browse"):
            movies = fetch_movies_by_genre(genre_id, (2000, 2024), 0)
            cols = st.columns(5)
            for i, movie in enumerate(movies):
                if i % 5 == 0:
                    cols = st.columns(5)
                with cols[i % 5]:
                    movie_id = movie['id']
                    poster_url = f"https://image.tmdb.org/t/p/w500/{movie['poster_path']}"
                    st.markdown(
                        f"<div class='movie-card'><a href='?movie_id={movie_id}'><img src='{poster_url}' width='100%'></a><div class='movie-title'>{movie['title']}</div></div>",
                        unsafe_allow_html=True
                    )

    elif selected_option == "Search by Actor":
        st.header("Search Movies by Actor")
        actor_name = st.text_input("Enter actor's name")
        if st.button("Search"):
            if actor_name:
                movies = search_movies_by_actor(actor_name)
                cols = st.columns(5)
                for i, movie in enumerate(movies):
                    if i % 5 == 0:
                        cols = st.columns(5)
                    with cols[i % 5]:
                        movie_id = movie['id']
                        poster_url = f"https://image.tmdb.org/t/p/w500/{movie['poster_path']}"
                        st.markdown(
                            f"<div class='movie-card'><a href='?movie_id={movie_id}'><img src='{poster_url}' width='100%'></a><div class='movie-title'>{movie['title']}</div></div>",
                            unsafe_allow_html=True
                        )

 