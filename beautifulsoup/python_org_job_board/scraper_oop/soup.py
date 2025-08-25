import requests
from beautifulsoup import BeautifulSoup, ResultSet, Tag


class Soup:
    URL = "https://www.python.org/jobs/"

    def __init__(self, python_jobs_filter: bool = False):
        self.url = self.URL
        self.python_jobs_filter = python_jobs_filter

    def soup_initiate(self) -> ResultSet[Tag] | list[Tag]:
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')

        result = soup.find(id="content")
        if self.python_jobs_filter is False:
            job_containers = result.find_all("li")

            return job_containers
        else:
            python_jobs = result.find_all("a", string=lambda text: 'python' in text.lower())
            python_jobs_containers = [a_element.parent.parent.parent for a_element in python_jobs]

            return python_jobs_containers
