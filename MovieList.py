""" 
* Beautiful Soup code to Extract Movie list from https://einthusan.ca website
! This is purely to learn BeautifulSoup
? Definitely not intended for commercial purposes
TODO: Defaulted to extract movie list based on Language & Year, needs to be re-configured for another language or year
"""

import requests
from bs4 import BeautifulSoup


def main():
    # * Pass the basic full URL to pick the pages count and other details using Beautiful soup
    url = "https://einthusan.ca/movie/results/?find=Year&lang=hindi&year=2018"
    # * Call function inside function to get the total number of pages the that BS needs to navigate
    Numb_of_pages_to_loop = int(get_loop_count(get_page(url)))
    # * Now pass the URL by concatenating the Pages in the URL & pass it to get_detail_page for retrieving movie & rating details
    for i in range(1, Numb_of_pages_to_loop + 1):
        url = (
            "https://einthusan.ca/movie/results/?find=Year&lang=hindi&page="
            + str(i)
            + "&year=2018"
        )
        # * Call the function with the updated URL to get the soup & then the movie and rating details
        get_detail_page(get_page(url))


# * Below function is to get the html page details using Beautiful Soup
def get_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


# * Below function is to retrieve the total pages that the movie list exist
def get_loop_count(soup):
    result_page = soup.find(class_="results-info")
    Numb_of_pages_to_loop = result_page.text.strip().split(" ")[4].split("(")[0]
    return Numb_of_pages_to_loop


# * Below function is to get the movie & ratings for each movie
def get_detail_page(soup):
    movies_released = soup.find_all(class_="block2")
    block3 = soup.find_all(class_="average-rating")
    # * Its a 1 line statement to store the details from a for loop in list (trick is to just go in reverse of the for loop)
    movie_names = [
        movies.find(class_="title").text.replace("Must Watch", "")
        for movies in movies_released
    ]
    # * same trick to store for loop output in a list
    rating_movie = [rating.get_text().replace("\ue914", " ") for rating in block3]
    # * zip is a inbuilt function to combine 2 lists with same reference ids, which makes it easier to print 2 lists in 1 loop
    for movie_rating in zip(movie_names, rating_movie):
        print(movie_rating)


# ! Is to declare main function for initialization & execution
if __name__ == "__main__":
    main()
