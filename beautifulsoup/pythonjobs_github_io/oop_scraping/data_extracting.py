from bs4.element import ResultSet, Tag

from beautifulsoup.pythonjobs_github_io.oop_scraping.soup import Soup


class DataExtractor(Soup):
    def __init__(self, jobs_list: ResultSet[Tag]):
        super().__init__()
        self.jobs_list = jobs_list

    def find_jobs(self) -> list[dict] | str:
        all_jobs_result = []
        for job in self.jobs_list:
            try:
                title_element = job.find("h1").text
                all_span_info = job.find_all("span", class_="info")
                location = all_span_info[0].text.strip()
                posted = all_span_info[1].text.strip()
                role = all_span_info[2].text.strip()
                details = job.find("p", class_="detail").text.strip()
                link = job.find_all("a")[0]["href"]

                job_result = {
                    "Title": title_element,
                    "Location": location,
                    "Posted": posted,
                    "Role": role,
                    "Job Details": details[:100],
                    "Link": self.page_url + link[1:]  # with slicing It removes the "//" from the beginning of the link
                }
                all_jobs_result.append(job_result)

            except Exception as e:
                raise e

        if all_jobs_result:
            return all_jobs_result
        return "No results found."
