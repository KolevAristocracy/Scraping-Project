import requests
from beautifulsoup import BeautifulSoup

URL = 'https://realpython.github.io/fake-jobs/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

result = soup.find(id='ResultsContainer')
job_cards = result.find_all("div", class_='card-content')

python_jobs = result.find_all("h2", string=lambda text: "python" in text.lower())
python_job_cards = [h2_element.parent.parent.parent for h2_element in python_jobs]

for pj in python_job_cards: # job_cards - jc
    title_element = pj.find("h2", class_='title')
    company_element = pj.find("h3", class_='company')
    location_element = pj.find("p", class_='location')
    link = pj.find_all("a")[1]["href"]
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print(f"Apply here {link}\n")
    print()



