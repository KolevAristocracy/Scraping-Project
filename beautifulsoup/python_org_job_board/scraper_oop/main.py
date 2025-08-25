from beautifulsoup.python_org_job_board.scraper_oop.soup import Soup
from beautifulsoup.python_org_job_board.scraper_oop.data_extacting import DataExtractor
from beautifulsoup.python_org_job_board.scraper_oop.print_result import PrintResult
from beautifulsoup.python_org_job_board.data_exporting.exportin_data_in_csv import ExportDataInCSV

soup = Soup(python_jobs_filter=False).soup_initiate()  # false is by default
data = DataExtractor(soup)
clean_data = data.extact_data()
final_result = PrintResult(clean_data).print_result()

print(final_result)

csv_exporter = ExportDataInCSV(clean_data)
csv_exporter.saving_data_in_csv()
