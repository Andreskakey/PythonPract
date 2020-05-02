from Movie import Movies

class users:
    def __init__(self, name):
        self.name = name
        self.movies = []
    def __repr__(self):
        return "<User {}>".format(self.name)

    def add_movie(self, name, genre): #my_user_obj.add_movie(name, genra)
        #movie = Movies(name, genre, False)
        self.movies.append(Movies(name, genre, False))

    def delete_movie(self,name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))

    def watched_movies(self):
        return list(filter(lambda x: x.watched, self.movies))
    def json(self):
        return {
            'name': self.name,
            'movie': [
                movie.json() for movie in self.movies
            ]
        }
    @classmethod
    def from_json(cls, json_data):
        user = users(json_data['name'])
        movies = []
        for movie_data in json_data['movie']:
            movies.append(Movies.from_json(movie_data))
            #movies.append(Movies(movie['name'], movie['genre'], movie['watched']))
        user.movies = movies
        return user
        #json_data['name']

"""
    def save_to_file(self):
        with open("{}.txt".format(self.name), 'w') as f:
            f.write(self.name + "\n")
            for movie in self.movies:
                f.write("{},{},{}\n".format(movie.name, movie.genre, str(movie.watched)))


        # movies_watched = list(filter(lambda x: x.watched, self.movies))
        # return movies_watched
    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as f:
            content = f.readlines()
            username = content[0]
            movies = []
            for line in content[1:]:
                movie_data = line.split(",")
                movies.append(Movies(movie_data[0], movie_data[1], movie_data[2] == "True"))
            user = cls(username)
            user.movies = movies
            return user
        """

"""
        #calc a list of movies that have been watched
        watched_movie_list = []

        for movie in self.movies:
            if movie.watched:
                watched_movie_list.append(movie)
        return watched_movie_list
        """