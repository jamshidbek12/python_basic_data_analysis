import requests
import random
import json

# API kalitni config.json fayldan o'qish
with open("config.json", "rt") as file:
    reader = json.load(file)
    API_key = reader["api_key_movie"]

# TMDB'dagi janrlar va ularning ID'lari (TMDB hujjatlaridan olingan)
genres = {
    "action": 28,
    "comedy": 35,
    "drama": 18,
    "horror": 27,
    "romance": 10749,
    "thriller": 53,
    "animation": 16,
    "fantasy": 14,
    "science fiction": 878,
    "crime": 80
}

# Foydalanuvchidan janr so'rash
print("Available genres:", ", ".join(genres.keys()))
genre_input = input("Enter a movie genre: ").lower()

if genre_input not in genres:
    print("Genre not found. Please choose from the list above.")
else:
    genre_id = genres[genre_input]
    
    # TMDB API'ga so'rov yuborish
    url = f"https://api.themoviedb.org/3/discover/movie?with_genres={genre_id}&api_key={API_key}"
    response = requests.get(url)
    data = response.json()
    
    movies = data["results"]
    
    if not movies:
        print("No movies found for this genre.")
    else:
        # Tasodifiy bitta filmni tanlash
        random_movie = random.choice(movies)
        
        title = random_movie["title"]
        overview = random_movie["overview"]
        release_date = random_movie["release_date"]
        rating = random_movie["vote_average"]
        
        print(f"\nRecommended movie: {title}")
        print(f"Release date: {release_date}")
        print(f"Rating: {rating}/10")
        print(f"Overview: {overview}")