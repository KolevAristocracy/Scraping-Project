from beautifulsoup import ResultSet, Tag

from beautifulsoup.python_org_job_board.scraper_oop.soup import Soup


class DataExtractor(Soup):
    def __init__(self, job_containers: ResultSet[Tag] | list[Tag]):
        super().__init__()
        self.job_containers = job_containers

    def extact_data(self) -> list[dict] | str:
        result = []
        for job_container in self.job_containers:
            try:
                title_element = job_container.find("a").text
                location = job_container.find("span", class_="listing-location").text
                job_type = job_container.find("span", class_="listing-job-type").text
                link = job_container.find_all("a")[0]["href"]
                posted_date = job_container.find("span", class_="listing-posted").text
                category = job_container.find("span", class_="listing-company-category").text

                job_results = {
                    # "ID": counter,
                    "Title": title_element,
                    "Location": location,
                    "Looking for": job_type.strip(),
                    "Posted": posted_date[8:],
                    "Category": category,
                    "Link": self.URL + (link[6:]),
                }
                result.append(job_results)
            except AttributeError:
                continue

        if result:
            return result
        return "No results found."
