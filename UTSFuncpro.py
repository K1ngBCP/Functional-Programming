import csv

dataCovid = "Covid Live.csv"

with open(dataCovid, 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    cek = lambda n : 0 if n in ['N/A', ''] else int(n.replace(',',''))
    data = list(map(lambda row :
    {
      "Country" : row[1],
      "Total Cases" : cek(row[2]),
      "Total Deaths" : cek(row[3]),
      "Total New Death" : cek(row[4]),
      "Total Recovered" : cek(row[5]),
      "Active Cases" : cek(row[6]),
      "Serious Critical" : cek(row[7]),
      "Total Cases 1M / pop" : cek(row[8]),
      "Death 1M / pop" : cek(row[9]),
      "Total Tests" : cek(row[10]),
      "Tests 1M / pop" : cek(row[11]),
      "Population" : cek(row[12]),
    }, csvreader))

# print(data)
#Built-in Function Map
# hasil_ = list(map(lambda x : x["Population"] - x["Total Deaths"], data))
# print(hasil_)
#Built-in Function Filter
# hasil_2 = list(filter(lambda x : x["Total Deaths"] < 10, data))
# print(hasil_2)
#Built-in Function Sorted
hasil_3 = list(sorted(data, key = lambda x : x["Total Deaths"]))
print(hasil_3)



