import csv

with open("sentence_dataset.csv", newline='') as csvfile:
    sentences = csv.reader(csvfile, delimiter=',')
    for row in sentences:
        print(row)