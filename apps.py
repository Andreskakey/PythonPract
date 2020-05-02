#with open('my_file.txt', 'w') as f:
 #   f.write('hello, world!')
from user import users
import json


#print(user.json())

with open('my_file.txt', 'r') as f:
    json_data = json.load(f)
    user = users.from_json(json_data)
    print(user.json())
    #json.dump(user.json(), f)

"""
user = users.load_from_file('Joe.txt')
print(user.movies)
print(user.name)
"""


"""
user.add_movie("the matrix", "Sci-Fi")
user.add_movie("the interview", "comedy")

user.save_to_file()
"""

"""
from Movie import Movies
from user import users

user = users("Joe")

my_movie = Movies("The matrix", "sci-fi", True)
user.movies.append(my_movie)


print(user.watched_movies())
#print(user)
#print(user.movies)
"""
