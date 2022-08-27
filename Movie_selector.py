import random
from turtle import title
import requests
from bs4 import BeautifulSoup


url = 'https://www.imdb.com/chart/top'


def main():
    responce = requests.get(url)
    
    soup = BeautifulSoup(responce.text, 'html.parser')


    movietags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    raitingtags = soup.select('td.posterColumn span[name=ir]')

    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1]
        return year

    years = [get_year(tag) for tag in movietags]
    actors_list = [tag['title'] for tag in inner_movietags]
    titles = [tag.text for tag in inner_movietags]
    raitings = [float(tag['data-value']) for tag in raitingtags]


    n_movies = len(titles)
    print(n_movies)
    
    while(True):    
        indx = random.randrange(0, n_movies)
        
        print(f'{titles[indx]} {years[indx]},  Рейтинг: {raitings[indx]:.1f}, Актори: {actors_list[indx]}')

        user_input = input('Бажаєте вибрати інший фільм (Так/[Ні])? ') 
        if user_input != 'Так':
            break
        


if __name__ == '__main__':
    main()