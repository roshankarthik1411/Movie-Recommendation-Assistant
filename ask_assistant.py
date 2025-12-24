def ask_assistant(user_query: str):
    query = user_query.lower()

    movies = [
        {
            "movie_title": "Mad Max: Fury Road",
            "genre": "Action",
            "year": 2015,
            "rating": "R",
            "keywords": ["action", "fast", "intense"],
            "response": "Mad Max: Fury Road is a non-stop action spectacle with stunning practical effects and relentless energy."
        },
        {
            "movie_title": "John Wick",
            "genre": "Action",
            "year": 2014,
            "rating": "R",
            "keywords": ["action", "fight", "thriller"],
            "response": "John Wick delivers stylish action with incredible choreography and a gripping revenge story."
        },
        {
            "movie_title": "Knives Out",
            "genre": "Comedy",
            "year": 2019,
            "rating": "PG-13",
            "keywords": ["funny", "comedy", "light"],
            "response": "Knives Out is a clever and funny murder mystery with an amazing ensemble cast."
        },
        {
            "movie_title": "Dune",
            "genre": "Sci-Fi",
            "year": 2021,
            "rating": "PG-13",
            "keywords": ["sci-fi", "space", "future"],
            "response": "Dune is an epic sci-fi experience with breathtaking visuals and deep world-building."
        },
        {
            "movie_title": "Get Out",
            "genre": "Horror",
            "year": 2017,
            "rating": "R",
            "keywords": ["horror", "scary", "thriller"],
            "response": "Get Out is a smart and terrifying horror film with sharp social commentary."
        }
    ]

    for movie in movies:
        if any(keyword in query for keyword in movie["keywords"]):
            return {
                "movie_title": movie["movie_title"],
                "genre": movie["genre"],
                "year": movie["year"],
                "rating": movie["rating"],
                "response": movie["response"]
            }

    return "I'm here to help with movie recommendations! What kind of movie are you in the mood for?"
