import requests
from bs4 import BeautifulSoup, ResultSet, Tag


class Soup:
    URL = 'https://realpython.github.io/fake-jobs/'

    def soup_initiate(self) -> ResultSet[Tag]:
        page = requests.get(self.URL)
        soup = BeautifulSoup(page.content, "html.parser")

        result = soup.find(id='ResultsContainer')
        job_cards = result.find_all("div", class_='card-content')

        return job_cards