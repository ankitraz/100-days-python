# csv stands for comma seperated values

import csv

# we cannot use path class to open a file, we have to use open function

with open("file.csv", 'w',encoding='utf') as file:
    writer = csv.writer(file)  # csv.writer take a file object thats why we cannot use a path class
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1001, 2, 15])


# reading a csv file
with open ("file.csv",'r',encoding='utf') as file:
    reader = csv.reader(file)
    # print(list(reader))

    # we can also iterate this reader object
    for row in reader:
        print(row)