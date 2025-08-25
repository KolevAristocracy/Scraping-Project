from bs4 import ResultSet, Tag

from beautifulsoup.fake_python_job_site.soup_class import Soup


class HtmlDataExtractor(Soup):

    def __init__(self, html_data: ResultSet[Tag]):
        self.data = html_data

    def clean_data_extract(self):
        result = []

        for pj in self.data:  # self.data consists python jobs - pj
            title_element = pj.find("h2", class_='title').text
            company_element = pj.find("h3", class_='company').text
            location_element = pj.find("p", class_='location').text
            link = pj.find_all("a")[1]["href"]

            jobs_result = {
                "Title": title_element.strip(),
                "Company": company_element.strip(),
                "Location": location_element.strip(),
                "Link": link
            }

            result.append(jobs_result)

        # If found jobs, it will return list[dict] which contains details for each job post.
        if result:
            return result
        return "No results found."
