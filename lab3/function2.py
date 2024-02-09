# Dictionary of movies

movies = [
 {
 "name" : "Usual Suspects" , "imdb" : 7.0, "category" : "Thriller"
 },
    
 {
 "name" : "Hitman", "imdb" : 6.3, "category" : "Action"
 },

 {
 "name" : "Dark Knight", "imdb" : 9.0, "category" : "Adventure"
 },

 {
 "name" : "The Help", "imdb" : 8.0, "category" : "Drama"
 },

 {
 "name" : "The Choice", "imdb" : 6.2, "category" : "Romance"
 },

 {
 "name" : "Colonia", "imdb" : 7.4, "category" : "Romance"
 },

 {
 "name" : "Love", "imdb" : 6.0, "category" : "Romance"
 },

 {
 "name" : "Bride Wars", "imdb" : 5.4, "category" : "Romance"
 },

 {
 "name" : "AlphaJet", "imdb" : 3.2, "category" : "War"
 },

 {
 "name" : "Ringing Crime", "imdb" : 4.0, "category" : "Crime"
 },

 {
 "name" : "Joking muck", "imdb" : 7.2, "category" : "Comedy"
 },

 {
 "name" : "What is the name", "imdb" : 9.2, "category" : "Suspense"
 },

 {
 "name" : "Detective", "imdb" : 7.0, "category" : "Suspense"
 },

 {
 "name" : "Exam", "imdb" : 4.2, "category" : "Thriller"
 },
 
 {
 "name" : "We Two", "imdb" : 7.2, "category" : "Romance"
 }
]
print("1:")
"""
1)Write a function that takes a single movie 
and returns True if its IMDB score is above 5.5
"""
def morethan(movie):
    return [movie["imdb"] > 5.5 for movie in movies]
result = morethan(movies)
print(result)
             
print("2:")

"""
2)
Write a function that returns a sublist of 
movies with an IMDB score above 5.5.
"""
 
def Score(movie_list): 
    return [movie for movie in movies if movie["imdb"] > 5.5]

scorem = Score(movies)
for movie in scorem:
    print(movie["name"])

print("3:")

"""
3)
Write a function that takes a category name 
and returns just those movies under that category.
"""

def Categ(category): 
    category_movies = [movie["name"] for movie in movies if movie["category"] == category]
    return category_movies

cat=input()
result=Categ(cat)
print(result)

print("4:")

"""
4)
Write a function that takes a list of movies 
and computes the average IMDB score.
"""
def calc(movie_list, mov):
    sum = 0
    c = 0

    for movie_name in mov:
        for movie in movie_list:
            if movie["name"] == movie_name:
                sum += movie["imdb"]
                c += 1

    if c > 0:
        average_score = sum / c
        print(average_score)
    else:
        print("No valid movies provided")

mov = [name.strip() for name in input().split(',')]
calc(movies, mov)



print("5:")

"""
5)
Write a function that takes a category and 
computes the average IMDB score.
"""
def category_mm(category): 
    sum = 0
    c = 0

    for movie in movies: 
        if movie["category"].lower() == category.lower(): 
            sum += movie["imdb"]
            c += 1
    
    if c > 0:
        full = sum / c
        return full
    else:
        return None
    
cat = input().strip().lower()
result = category_mm(cat)

if result is not None:
    print(result)
else:
    print("wrong category")
