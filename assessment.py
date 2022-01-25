import csv

# creating a new file to write to
cleanData = open('cleandata.csv', 'w')
# creating a header in new file
cleanData_header = "Text,Target\n"
# writing header to the new file
cleanData.write(cleanData_header)

with open('sentence_dataset.csv', 'r') as data:
    print(type(data))
    # reader method taking in data from csv file
    reader = csv.reader(data)
    # skip header line
    header = next(reader)
    # header data type is a list
    
    
    for row in reader:
        # showing first row in dataset
        sentences = row[0]
        # creating new line for every row of dataset
        line = "{}\n".format(sentences)

        cleanData.write(line)
      

cleanData.close()
