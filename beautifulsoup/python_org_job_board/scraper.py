import requests
from bs4 import BeautifulSoup

from beautifulsoup.python_org_job_board.exporting_data_in_csv import saving_data_in_csv

URL = "https://www.python.org/jobs/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

result = soup.find(id="content")
# job_containers = result.find_all("li")

# showing only positions which contains text: 'word'
python_jobs = result.find_all("a", string=lambda text: 'python' in text.lower())
python_jobs_containers = [a_element.parent.parent.parent for a_element in python_jobs]


def find_jobs(job_containers):
    final_result = []
    # counter = 0
    for job_container in job_containers:
        try:
            title_element = job_container.find("a").text
            location = job_container.find("span", class_="listing-location").text
            job_type = job_container.find("span", class_="listing-job-type").text
            link = job_container.find_all("a")[0]["href"]
            posted_date = job_container.find("span", class_="listing-posted").text
            category = job_container.find("span", class_="listing-company-category").text

            # counter += 1
            job_results = {
                # "ID": counter,
                "Title": title_element,
                "Location": location,
                "Looking for": job_type.strip(),
                "Posted": posted_date[8:],
                "Category": category,
                "Link": URL + (link[6:]),
            }
            final_result.append(job_results)
        except AttributeError:
            continue

    if final_result:
        return final_result

saving_data_in_csv(find_jobs(python_jobs_containers))
