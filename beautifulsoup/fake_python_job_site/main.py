from beautifulsoup.fake_python_job_site.data_extractor import HtmlDataExtractor
from beautifulsoup.fake_python_job_site.print_result import PrintResult
from beautifulsoup.fake_python_job_site.soup_class import Soup

soup = Soup().soup_initiate()
extracted_data = HtmlDataExtractor(soup).clean_data_extract()
final_result = PrintResult(extracted_data).print_result()

print(final_result)
