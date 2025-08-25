from data_extracting import DataExtractor
from beautifulsoup.pythonjobs_github_io.oop_scraping.print_result import PrintResult
from soup import Soup
from database_manager import main

import csv

class ScrapingManager:
    def __init__(self, soup_cls=Soup, extractor_cls=DataExtractor):
        try:
            soup_instance = soup_cls()
            soup = soup_instance.soup_initiate()
            data_extractor = extractor_cls(soup)
            self.data = data_extractor.find_jobs()

        except Exception as e:
            print(f"Error initializing ScrapingManager: {e}")
            self.data = None

    def data_to_csv(self):
        with open("oop_data_iogithub.csv", mode="w") as csvfile:
            fieldnames = self.data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in self.data:
                writer.writerow(row)

    def csv_to_db(self):
        database_manager = main()
        return database_manager

    def print(self):
        print_result = PrintResult(self.data).print_result()

        print(print_result)

if __name__ == '__main__':
    manager = ScrapingManager()
    manager.csv_to_db()

