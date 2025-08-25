import requests
from beautifulsoup import BeautifulSoup, ResultSet, Tag

from beautifulsoup.pythonjobs_github_io.regular_scraper.exporting_data_in_csv import saving_data_in_csv

page_url = "https://pythonjobs.github.io/"

def soup_initiate() -> ResultSet[Tag]:
    url = page_url
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    result = soup.find(id="content")
    job_lists = result.find_all("div", class_="job")
    return job_lists

def find_jobs(job_list: ResultSet[Tag]) -> list[dict] | str:
    all_jobs_result = []
    for job in job_list:
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
                "Link": page_url + link[1:] # with slicing It removes the "//" from te beginning of the link
            }
            all_jobs_result.append(job_result)

        except Exception as e:
            raise e

    if all_jobs_result:
        return all_jobs_result
    return "No results found."

def print_result() -> str:
    result = []
    job_data: list[dict] = find_jobs(soup_initiate())

    if isinstance(job_data, str):
        return job_data

    for job_dict in job_data:
        for key, value in job_dict.items():
            result.append(f"{key}: {value}")

    return '\n'.join(result)

# print(print_result())

saving_data_in_csv(find_jobs(soup_initiate()))
