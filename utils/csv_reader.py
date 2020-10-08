import csv


def get_data(filename):
    data = []
    with open(filename, encoding="utf-8-sig") as csvfile:
        read_data = csv.reader(csvfile, delimiter=',')
        for row in read_data:
            data.append(row)
    return data

