import csv


class ExportDataInCSV:
    def __init__(self, clean_data: list[dict]):
        self.clean_data = clean_data

    def saving_data_in_csv(self):
        with open("oop_data.csv", mode="w") as csvfile:
            fieldnames = self.clean_data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in self.clean_data:
                writer.writerow(row)
