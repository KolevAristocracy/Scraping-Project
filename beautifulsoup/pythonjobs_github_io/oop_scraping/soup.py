import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag


class Soup:
    page_url = "https://pythonjobs.github.io/"

    def soup_initiate(self) -> ResultSet[Tag]:
        page = requests.get(self.page_url)
        soup = BeautifulSoup(page.content, 'html.parser')

        result = soup.find(id="content")
        job_lists = result.find_all("div", class_="job")
        return job_lists
