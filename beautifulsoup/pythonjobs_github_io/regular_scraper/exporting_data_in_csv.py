import csv

def saving_data_in_csv(result: list[dict]):
    with open("../data.csv", mode="w") as csvfile:
        fieldnames = result[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in result:
            writer.writerow(row)
