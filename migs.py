import csv
import json

with open("sentence_dataset.csv", 'r') as csvfile, open("new.csv", 'w', newline='') as newfile:
    handle = csv.reader(csvfile)
    writer = csv.writer(newfile)

    for row in handle:
        print(row)
        print(row[0])
        jsonrow = json.loads(row[0])
        writer.writerow([jsonrow])