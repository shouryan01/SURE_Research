import csv

def do(file):
    with open("data.txt") as input_file, \
        open("data.csv", "w") as output_file:
        csvwriter = csv.writer(output_file)

        data = input_file.readlines()
        for line in data:
            line = line.replace("NaNmi", "")
            s = line.index("$")
            price = line[s:s+5]
            address = line[:s]
            csvwriter.writerow([address, price])

files = ["px.csv", "wc.csv", "ta.csv", "pp.csv", "cn.csv", "wj.csv"]

for f in files:
