# Important note: the code will have to be refactored with the requests module instead of the requests_with_caching
# module A key will have to be obtained from each of the websites used and passed into the dictionary for parameters

import requests_with_caching


def get_movies_from_tastedive(MovieName):
    base_url = "https://tastedive.com/api/similar"
    d = {"q": MovieName, "type": "movies", "limit": 5}
    resp = requests_with_caching.get(base_url, params=d)
    resp_d = resp.json()
    print(resp_d)
    return resp_d


def extract_movie_titles(dicty):
    py_data = dicty
    extract = py_data['Similar']
    movies = []
    for r in extract['Results']:
        movies.append(r['Name'])
    return movies


def get_related_titles(MovieTitles):
    related = []
    for title in MovieTitles:
        comb = extract_movie_titles(get_movies_from_tastedive(title))
        for element in comb:
            if element not in related:
                related.append(element)
            else:
                continue
    return related


def get_movie_data(listy):
    base_url = 'http://www.omdbapi.com/'
    d = {'t': listy, 'r': 'json'}
    res = requests_with_caching.get(base_url, params=d)
    res_d = res.json()
    return res_d


def get_movie_rating(above):
    score = 0
    for element in above['Ratings']:
        if element['Source'] == 'Rotten Tomatoes':
            score = int(element['Value'][:2])
    return score


def get_sorted_recommendations(listy):
    new_d = {}
    new_list = get_related_titles(listy)
    for movie in new_list:
        new_d[movie] = get_movie_rating(get_movie_data(movie))
    sorted_d = sorted(new_d, key=lambda x: (new_d[x], x), reverse=True)
    return sorted_d
