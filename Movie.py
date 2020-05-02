class Movies:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched
       # self.director = "Wa"

    def __repr__(self):
        return "<Movie {}>".format(self.name)
    def json(self):
        return {
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }
    @classmethod
    def from_json (cls, json_data):
        return Movies(**json_data)
        #return Movies(genre = json_data['genre'], watched = json_data['watched'], name = json_data['name'], )
       # return Movies(json_data['name'], json_data['genre'], json_data['watched'])